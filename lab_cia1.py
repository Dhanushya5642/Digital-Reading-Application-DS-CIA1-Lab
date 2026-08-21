import pandas as pd
import numpy as np
from scipy.stats import binom


df = pd.read_csv("user-activity.csv")
print("Original Dataset")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())
duplicate_count = df.duplicated(subset="user_id").sum()

print("\nDuplicate User Accounts:", duplicate_count)
df = df.drop_duplicates(subset="user_id")
df["activation_date"] = df["activation_date"].fillna("Unknown")
print("\nDataset After Cleaning")
print(df.head())
df["completed"] = df["completed_book"].map({
    "Yes": 1,
    "No": 0
})

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())
print("\nReading Activity Summary")
print("Total Users:", len(df))
print("Average Books Started:", df["books_started"].mean())
print("Average Books Completed:", df["books_completed"].mean())
print("Average Reading Minutes:", df["reading_minutes"].mean())


completed_users = df["completed"].sum()
not_completed_users = len(df) - completed_users
print("\nCompleted Users:", completed_users)
print("Not Completed Users:", not_completed_us\
      ers)

p = completed_users / len(df)
print("\nProbability of Completing a Book")
print("p =", round(p,4))
n = 1
expected_not_completed = len(df) * binom.pmf(0, n, p)
expected_completed = len(df) * binom.pmf(1, n, p)
print("\nExpected Frequencies")
print("Expected Not Completed:",
      round(expected_not_completed,2))
print("Expected Completed:",
      round(expected_completed,2))
comparison = pd.DataFrame({
    "Outcome":[
        "Not Completed",
        "Completed"
    ],
    "Observed":[
        not_completed_users,
        completed_users
    ],
    "Expected":[
        round(expected_not_completed,2),
        round(expected_completed,2)
    ]
})
print("\nObserved vs Expected")
print(comparison)
df.to_csv("cleaned_dataset.csv", index=False)