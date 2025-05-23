"""Load Q&A pairs from a JSON file."""

import logging
import os
from typing import Optional

try:
    import openai
    from openai import OpenAIError
except ImportError:
    openai = None

logger = logging.getLogger(__name__)


class LLMClient:
    """
    A class to interact with OpenAI's GPT-3 API."""

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if openai and self.api_key:
            openai.api_key = self.api_key
            self.enabled = True
        else:
            self.enabled = False
            if not openai:
                logger.warning(
                    "OpenAI package not installed; LLM fallback disabled."
                )
            elif not self.api_key:
                logger.warning(
                    "OPENAI_API_KEY not set; LLM fallback disabled."
                )

    def ask(self, prompt: str) -> Optional[str]:
        """
        Ask a question to the LLM and return the answer."""
        if not self.enabled:
            return None
        try:
            response = openai.chat.ChatCompletion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except OpenAIError as e:
            logger.error("OpenAI API error: %s", e)
            return None
