"""Entry point for the GP note pipeline."""

from gpnote.llm import structure_note

SAMPLE_NOTE = """
45yo M, chest pain 2 days, worse on exertion, no SOB, smoker 20/day.
BP 150/95, HR 88, chest clear. ECG ordered, GTN spray given, review 1 week.
"""


def main() -> None:
    note = structure_note(SAMPLE_NOTE)
    print(note.model_dump_json(indent=2))


if __name__ == "__main__":
    main()