"""Data model for a structured clinical note."""

from pydantic import BaseModel, Field


class ClinicalNote(BaseModel):
    """A consultation written up in the standard SOAP-style format.

    Every field is a plain string so the note can be dropped straight into
    a patient record system. Sections with nothing to say are left empty
    rather than filled with "not documented".
    """

    presenting_complaint: str = Field(
        description="Why the patient came in, in one or two sentences."
    )
    history: str = Field(
        description="Relevant history: onset, course, associated symptoms, "
        "risk factors, past medical history, medications, allergies, social "
        "and family history. Only what the notes state."
    )
    examination: str = Field(
        description="Findings on examination, including vitals, and the "
        "results of any investigations recorded. Only what the notes state."
    )
    assessment: str = Field(
        description="The clinician's impression, working diagnosis or problem "
        "list, exactly as stated in the notes. Do not add a diagnosis or "
        "diagnostic label that the notes do not use."
    )
    plan: str = Field(
        description="Investigations, treatment, safety-netting and follow-up."
    )