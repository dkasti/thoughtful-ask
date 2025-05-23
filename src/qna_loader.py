"""Load Q&A pairs from a JSON file."""

import json
import logging

logger = logging.getLogger(__name__)


class QNALoader:
    """
    A class to load Q&A pairs from a JSON file."""

    def __init__(self, filepath):
        self.filepath = filepath
        self.qna = {}

    def load(self):
        """
        Load Q&A pairs from the JSON file."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            logger.error("Q&A file not found: %s", self.filepath)
            raise
        except json.JSONDecodeError as e:
            logger.error("Invalid JSON in Q&A file: %s", e)
            raise

        for item in data.get("questions", []):
            question = item.get("question", "").strip().lower()
            answer = item.get("answer", "").strip()
            if question and answer:
                self.qna[question] = answer
        logger.info(
            "Loaded %d Q&A pairs from %s", len(self.qna), self.filepath
        )
        return self.qna
