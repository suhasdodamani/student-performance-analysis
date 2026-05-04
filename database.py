import sqlite3
import pandas as pd

df = pd.read_csv('../data/cleaned_students.csv')

conn = sqlite3.connect('../database/student.db')
df.to_sql('students', conn, if_exists='replace', index=False)
conn.close()

print("Database created successfully!")
