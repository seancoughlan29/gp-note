from gpnote.data import load_notes, split_notes

df = load_notes()
print(len(df), "notes")
print(df["medical_specialty"].value_counts())
train, val, test = split_notes(df)
print(len(train), len(val), len(test))
print(test.iloc[0]["transcription"][:1500])
df = df[~df["sample_name"].str.contains("Template", case=False, na=False)]
df = df[df["transcription"].str.contains("COMPLAINT|CONSULT|PRESENT ILLNESS", case=False, na=False)]