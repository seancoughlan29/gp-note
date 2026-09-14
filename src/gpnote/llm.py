"""Thin wrapper around the Anthropic API."""

import os

from anthropic import Anthropic, APIError
from dotenv import load_dotenv
from pydantic import ValidationError

from gpnote.schema import ClinicalNote

load_dotenv()

MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = (
    "You are a documentation assistant for general practitioners. "
    "Convert raw consultation notes into a structured clinical note. "
    "Use only information present in the notes. Do not add findings, "
    "diagnoses or advice that are not written there. If a section has no "
    "supporting information, leave it as an empty string. "
    "Preserve the spelling and terminology used in the source notes."
)

_client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def structure_note(raw_text: str, max_tokens: int = 4096) -> ClinicalNote | None:
    """Turn raw consultation text into a validated ClinicalNote.

    Returns None if the API call failed or the output could not be parsed,
    so callers can count failures instead of crashing.
    """
    try:
        response = _client.messages.parse(
            model=MODEL,
            max_tokens=max_tokens,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": f"Consultation notes:\n{raw_text}"}],
            output_format=ClinicalNote,
        )
    except (APIError, ValidationError) as exc:
        print(f"structure_note failed: {exc}")
        return None
    return response.parsed_output