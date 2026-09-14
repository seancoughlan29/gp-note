"""Entry point for the GP note pipeline."""

from gpnote.data import load_notes, split_notes
from gpnote.llm import structure_note


def main(n: int = 5) -> None:
    """Structure the first n test-set notes and print input alongside output."""
    df = load_notes()
    _, _, test = split_notes(df)

    failures = 0
    for i, row in test.head(n).iterrows():
        raw = row["transcription"]
        note = structure_note(raw)
        if note is None:
            failures += 1
            continue

        print("=" * 80)
        print(f"NOTE {i}  |  {row['medical_specialty'].strip()}  |  {row['sample_name']}")
        print("-" * 80)
        print("INPUT:")
        print(raw)
        print("-" * 80)
        print("OUTPUT:")
        print(note.model_dump_json(indent=2))

    print(f"\n{n - failures}/{n} notes structured successfully")


if __name__ == "__main__":
    main()