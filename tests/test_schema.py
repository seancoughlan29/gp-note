"""Tests for the ClinicalNote schema."""

import pytest
from pydantic import ValidationError

from gpnote.schema import ClinicalNote


def test_note_accepts_four_sections() -> None:
    note = ClinicalNote(
        presenting_complaint="Chest pain",
        history="2 days, exertional",
        examination="BP 150/95",
        plan="ECG",
    )
    assert note.plan == "ECG"


def test_note_rejects_missing_section() -> None:
    with pytest.raises(ValidationError):
        ClinicalNote(presenting_complaint="Chest pain")  # type: ignore[call-arg]