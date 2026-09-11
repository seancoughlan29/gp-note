"""Thin wrapper around the Anthropic API."""

import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-sonnet-4-6"

_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def complete(prompt: str, max_tokens: int = 1024) -> str:
    """Send a single prompt to Claude and return the text of the reply."""
    response = _client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text