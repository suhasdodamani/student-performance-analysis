import pandas as pd

df = pd.read_csv('../data/students.csv')
df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))

df['Average'] = df[['Math','Science','English']].mean(axis=1)

df['Performance'] = df['Average'].apply(
    lambda x: 'Topper' if x >= 85 else ('Average' if x >= 50 else 'Weak')
)

df.to_csv('../data/cleaned_students.csv', index=False)

print("Data cleaned successfully!")
