from agents.profile_agent import ProfileAgent
from agents.visualization_agent import VisualizationAgent

class ManagerAgent:

    def run(self, df):

        logs = []

        logs.append("Manager Agent Started")

        profiler = ProfileAgent()
        profile = profiler.analyze(df)

        logs.append("Profile Agent Completed")

        viz_agent = VisualizationAgent()
        chart = viz_agent.generate_chart(df)

        logs.append("Visualization Agent Completed")

        return profile, chart, logs