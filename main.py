import json
import sys

import numpy as np
import openai
from openai.embeddings_utils import get_embedding

from hume import HumeBatchClient
from hume import TranscriptionConfig
from configs import HumeAIConfigs, OpenAIConfigs
from LEED import LEED

# Define input data location
data_urls = HumeAIConfigs.DATA_URLS

# Initialize Hume Batch Client
hume_client = HumeBatchClient(api_key=HumeAIConfigs.API_KEY)
leed = LEED()

# Configure prosody and transcription settings
if HumeAIConfigs.HUME_MODEL_TYPE == "prosody":
    from hume.models.config import ProsodyConfig

    model_config = ProsodyConfig()
    transcription_config = TranscriptionConfig(language="en")
    leed_model = LEED.audio_prosody

if HumeAIConfigs.HUME_MODEL_TYPE == "face":
    from hume.models.config import FaceConfig

    model_config = FaceConfig()
    leed_model = LEED.image_face

# Submit job to Hume API
job = hume_client.submit_job(data_urls, [model_config])

print("Running the Hume API ...", job)

# Wait for job completion
job.await_complete()

# Retrieve predictions from job
full_predictions = job.get_predictions()
try:
    # Extract relevant predictions
    print("Job completed with status:", job.get_status())
    predictions = full_predictions[0]["results"]["predictions"][0]["models"][
        HumeAIConfigs.HUME_MODEL_TYPE
    ]["grouped_predictions"][0]["predictions"][0]
except Exception as e:
    print(
        f"An unexpected error occurred with the API (please retry or contact support):\n{e}"
    )
    print(f"API error: {full_predictions[0]['results']['errors']}")
    sys.exit(1)

# Extract emotions
emotions = predictions["emotions"]

# Extract emotion names and scores
emotion_names = [emotion["name"] for emotion in emotions]
emotion_scores = np.array([emotion["score"] for emotion in emotions])

print()
print(
    f"Transforming Hume-{HumeAIConfigs.HUME_MODEL_TYPE.upper()} emotion scores to descriptive language"
)

# Convert expression scores to language-based description
emotion_phrases = [leed.create_leed(emotion_scores)]
neutral_count = emotion_phrases.count("neutral")
if neutral_count > 1:
    emotion_phrases = HumeAIConfigs().keep_first_neutral(emotion_phrases)

if HumeAIConfigs.HUME_MODEL_TYPE == "prosody":
    transcription = predictions["text"]
    leed_result, _ = leed_model(emotion_phrases, transcription)
if HumeAIConfigs.HUME_MODEL_TYPE == "face":
    leed_result, _ = leed_model(emotion_phrases, transcription)

print()
print("LEED")
print(f"{leed_result['text_output'][0]}")

# Extract embeddings using OpenAI
if OpenAIConfigs.EXTRACT_EMBEDDINGS:
    print()
    print("Extracting language embedding with OpenAI")
    # Set OpenAI API key
    openai.api_key = OpenAIConfigs.API_KEY

    embedding = get_embedding(leed_result["text_output"][0], engine=OpenAIConfigs.MODEL)
else:
    embedding = []
    print()
    print("No embeddings stored")

if OpenAIConfigs.PROMPT_CHATGPT:
    expressive_prompt = f"{leed_result['text_output'][0]} {OpenAIConfigs.PROMPT}"
    chat_response = OpenAIConfigs().query_chat_model(expressive_prompt)
    print()
    print("Prompt to ChatGPT")
    print(expressive_prompt)
    print()
    print("Response from ChatGPT")
    print(chat_response)

else:
    expressive_prompt = ""
    chat_response = ""
    print()
    print("No prompt given to ChatGPT")

# Prepare data for JSON
output_data = {
    f"hume_{HumeAIConfigs.HUME_MODEL_TYPE}_outputs": {
        "names": emotion_names,
        "scores": emotion_scores.flatten().tolist(),
    },
    "expression2text": {
        "expressive_prompt": expressive_prompt,
        "text": leed_result["text_output"][0],
        "embedding": embedding,
        "chat-gpt_response": chat_response,
    },
}

# Save output to JSON file
output_file = f"{HumeAIConfigs.HUME_MODEL_TYPE}_Hume-EPE.json"
with open(output_file, "w", encoding="utf8") as f:
    json.dump(output_data, f, indent=4)
print()
print(f"Output saved as: {output_file}")
