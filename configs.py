import os
import requests

class OpenAIConfigs:
    API_KEY = os.environ.get("OPENAI_API_KEY")
    MODEL = "text-embedding-ada-002"
    EXTRACT_EMBEDDINGS = False
    PROMPT_CHATGPT = False
    PROMPT = "How do you think they might react if you were to ask them their name?"

    def __init__(self) -> None:
        pass

    def query_chat_model(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {os.environ.get("OPENAI_API_KEY")}',
        }

        data = {
            "model": "gpt-4-0314",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=60
        )
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"]

class HumeAIConfigs:
    API_KEY = os.environ.get("HUME_API_KEY")
    HUME_MODEL_TYPE = "prosody"  # Options: "face", "prosody"

    def __init__(self) -> None:
        pass

    if "prosody" in HUME_MODEL_TYPE:
        DATA_URLS = [
            "https://storage.googleapis.com/hume-test-data/audio/speech_sample_1.wav"
        ]
    elif "face" in HUME_MODEL_TYPE:
        DATA_URLS = [
            "https://storage.googleapis.com/hume-test-data/image/goofy-smile.png"
        ]

    RANGE_ADVERBS = ["slightly", "somewhat", "moderately", "quite", "very", "extremely"]
    EMOTION_RANGES = [
        (0.26, 0.35),
        (0.35, 0.44),
        (0.44, 0.53),
        (0.53, 0.62),
        (0.62, 0.71),
        (0.71, 10),
    ]

    EMOTIONS = [
        "Admiration",
        "Adoration",
        "Aesthetic Appreciation",
        "Amusement",
        "Anger",
        "Anxiety",
        "Awe",
        "Awkwardness",
        "Boredom",
        "Calmness",
        "Concentration",
        "Contemplation",
        "Confusion",
        "Contempt",
        "Contentment",
        "Craving",
        "Determination",
        "Disappointment",
        "Disgust",
        "Distress",
        "Doubt",
        "Ecstasy",
        "Embarrassment",
        "Empathic Pain",
        "Entrancement",
        "Envy",
        "Excitement",
        "Fear",
        "Guilt",
        "Horror",
        "Interest",
        "Joy",
        "Love",
        "Nostalgia",
        "Pain",
        "Pride",
        "Realization",
        "Relief",
        "Romance",
        "Sadness",
        "Satisfaction",
        "Desire",
        "Shame",
        "Surprise (negative)",
        "Surprise (positive)",
        "Sympathy",
        "Tiredness",
        "Triumph",
    ]

    EMOTIONS_ADJECTIVES = [
        "admiring",
        "adoring",
        "appreciative",
        "amused",
        "angry",
        "anxious",
        "awestruck",
        "uncomfortable",
        "bored",
        "calm",
        "focused",
        "contemplative",
        "confused",
        "contemptuous",
        "content",
        "hungry",
        "determined",
        "disappointed",
        "disgusted",
        "distressed",
        "doubtful",
        "euphoric",
        "embarrassed",
        "disturbed",
        "entranced",
        "envious",
        "excited",
        "fearful",
        "guilty",
        "horrified",
        "interested",
        "happy",
        "enamored",
        "nostalgic",
        "pained",
        "proud",
        "inspired",
        "relieved",
        "smitten",
        "sad",
        "satisfied",
        "desirous",
        "ashamed",
        "negatively surprised",
        "positively surprised",
        "sympathetic",
        "tired",
        "triumphant",
    ]
    # 
    def keep_first_neutral(self, lst):
        found_neutral = False
        result = []

        for item in lst:
            if item == "neutral" and not found_neutral:
                found_neutral = True
                result.append(item)
            elif item != "neutral":
                result.append(item)

        return result
