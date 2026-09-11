"""Entry point for the GP note pipeline."""

from gpnote.llm import complete

SAMPLE_NOTE = """
45yo M, chest pain 2 days, worse on exertion, no SOB, smoker 20/day.
BP 150/95, HR 88, chest clear. ECG ordered, GTN spray given, review 1 week.
"""


def main() -> None:
    prompt = (
        "You are a GP documentation assistant. Rewrite the following "
        "consultation notes as a structured clinical note with the headings "
        "Presenting Complaint, History, Examination, Plan.\n\n"
        f"Notes:\n{SAMPLE_NOTE}"
    )
    print(complete(prompt))


if __name__ == "__main__":
    main()