import pandas as pd

class ProfileAgent:

    def analyze(self, df):

        rows = len(df)
        cols = len(df.columns)

        missing = int(df.isnull().sum().sum())
        duplicates = int(df.duplicated().sum())

        quality_score = max(
            0,
            100 - (missing * 2) - (duplicates * 5)
        )

        profile = {
            "rows": rows,
            "columns": cols,
            "missing_values": missing,
            "duplicates": duplicates,
            "quality_score": quality_score,
            "column_names": list(df.columns)
        }

        return profile