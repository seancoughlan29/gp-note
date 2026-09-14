"""Loading and splitting the MTSamples dataset."""

from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw/mtsamples.csv")

# Specialties whose notes look most like GP consultations.
GP_LIKE_SPECIALTIES = {
    " General Medicine",
    " Consult - History and Phy.",
    " SOAP / Chart / Progress Notes",
}


def load_notes(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load MTSamples and keep only GP-like consultation notes.

    Drops templates and anything without a recognisable complaint or
    history section, since those aren't consultations.
    """
    df = pd.read_csv(path)
    df = df[df["medical_specialty"].isin(GP_LIKE_SPECIALTIES)]
    df = df.dropna(subset=["transcription"])
    df = df[df["transcription"].str.len() > 200]
    df = df[~df["sample_name"].str.contains("Template", case=False, na=False)]
    df = df[
        df["transcription"].str.contains(
            "COMPLAINT|CONSULT|PRESENT ILLNESS", case=False, na=False
        )
    ]
    return df.reset_index(drop=True)


def split_notes(
    df: pd.DataFrame, seed: int = 42
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Shuffle and split 80/10/10 into train, validation and test sets."""
    shuffled = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    n = len(shuffled)
    train_end = int(n * 0.8)
    val_end = int(n * 0.9)
    return (
        shuffled.iloc[:train_end],
        shuffled.iloc[train_end:val_end],
        shuffled.iloc[val_end:],
    )