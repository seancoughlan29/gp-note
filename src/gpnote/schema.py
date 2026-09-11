"""Data model for a structured clinical note."""

from pydantic import BaseModel, Field


class ClinicalNote(BaseModel):
    """A consultation written up in the standard four-section format.

    Every field is a plain string so the note can be dropped straight into
    a patient record system. Sections with nothing to say are left empty
    rather than filled with "not documented".
    """

    presenting_complaint: str = Field(
        description="Why the patient came in, in one or two sentences."
    )
    history: str = Field(
        description="Relevant history: onset, course, associated symptoms, "
        "risk factors, medications. Only what the notes state."
    )
    examination: str = Field(
        description="Findings on examination, including vitals. Only what "
        "the notes state."
    )
    plan: str = Field(
        description="Investigations, treatment, safety-netting and follow-up."
    )