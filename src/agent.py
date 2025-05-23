"""Load Q&A pairs from a JSON file."""

import difflib
import logging
from pathlib import Path

from .llm_client import LLMClient
from .qna_loader import QNALoader

logger = logging.getLogger(__name__)


class SupportAgent:
    """
    A class to handle Q&A pairs and interact with the LLM."""

    def __init__(self, qna_path: Path):
        loader = QNALoader(qna_path)
        self.qna = loader.load()
        self.llm = LLMClient()

    def get_answer(self, question: str) -> str:
        """
        Get the answer to a question."""
        key = question.strip().lower()
        # Exact match
        if key in self.qna:
            return self.qna[key]
        # Fuzzy match
        match = difflib.get_close_matches(
            key, self.qna.keys(), n=1, cutoff=0.6
        )
        if match:
            return self.qna[match[0]]
        # Fallback to LLM
        if self.llm.enabled:
            prompt = (
                "You are a helpful Thoughtful AI support agent."
                "Answer the question or say 'I'm sorry' if unsure."
                f"\n\nQuestion: {question}\nAnswer:"
            )
            llm_resp = self.llm.ask(prompt)
            if llm_resp:
                return llm_resp
        return "I’m sorry, I don't have an answer to that question."
