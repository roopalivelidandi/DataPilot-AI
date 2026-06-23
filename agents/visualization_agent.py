import plotly.express as px

class VisualizationAgent:

    def generate_chart(self, df):

        numeric_cols = df.select_dtypes(
            include=["number"]
        ).columns

        if len(numeric_cols) == 0:
            return None

        column = numeric_cols[0]

        fig = px.histogram(
            df,
            x=column,
            title=f"Distribution of {column}"
        )

        return fig