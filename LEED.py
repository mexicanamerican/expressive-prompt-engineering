import numpy as np
from configs import HumeAIConfigs


class LEED:
    def __init__(self):
        self.emotion_ranges = HumeAIConfigs().EMOTION_RANGES
        self.adverbs = HumeAIConfigs().RANGE_ADVERBS
        self.adjectives = HumeAIConfigs().EMOTIONS_ADJECTIVES

    def create_leed(self, emotion_scores):
        """
        Converts emotion scores to a descriptive text expression.

        Args:
            emotion_scores (list or numpy array): A list of emotion scores.

        Returns:
            str: The descriptive text expression for the given emotion scores.
        """
        if all(
            emotion_score < self.emotion_ranges[0][0]
            for emotion_score in emotion_scores
        ):
            expression_text = "neutral"
        else:
            phrases = [""] * len(emotion_scores)
            for i, (range_min, range_max) in enumerate(self.emotion_ranges):
                indices = [
                    index
                    for index, emotion_score in enumerate(emotion_scores)
                    if range_min < emotion_score < range_max
                ]
                for index in indices:
                    phrases[index] = f"{self.adverbs[i]} {self.adjectives[index]}"

            sorted_indices = np.argsort(emotion_scores)[::-1]
            phrases = [phrases[i] for i in sorted_indices if phrases[i] != ""]

            if len(phrases) > 1:
                expression_text = ", ".join(phrases[:-1]) + ", and " + phrases[-1]
            else:
                expression_text = phrases[0]
        return expression_text

    def audio_prosody(phrases, transcription):
        """
        Generates a text output based on the prosody model outputs.

        Args:
            phrases (list): A list of descriptive phrases related to audio prosody.
            transcription (str): The audio transcription.

        Returns:
            dict: A dictionary containing the text output under the key 'text_output'.
            str: The text output.
        """
        phrases_joined = ", ".join(phrases)
        result = f"They said '{transcription}' and they sounded {phrases_joined}."
        dict_res = {"text_output": [result]}
        return dict_res, result

    def image_face(phrases):
        """
        Generates a text output based on the facial expression model outputs.

        Args:
            phrases (list): A list of descriptive phrases related to facial expressions.

        Returns:
            dict: A dictionary containing the text output under the key 'text_output'.
            str: The text output.
        """
        phrases_joined = ", ".join(phrases)
        result = f"They looked {phrases_joined}."
        dict_res = {"text_output": [result]}
        return dict_res, result
