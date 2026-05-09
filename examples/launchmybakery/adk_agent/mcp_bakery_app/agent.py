import os
import dotenv
from mcp_bakery_app import tools
from google.adk.agents import LlmAgent

dotenv.load_dotenv()

PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT', 'project_not_set')

maps_toolset = tools.get_maps_mcp_toolset()
bigquery_toolset = tools.get_bigquery_mcp_toolset()

root_agent = LlmAgent(
    model='gemini-3.1-pro-preview',
    name='root_agent',
    instruction=f"""
                [SYSTEM DIRECTIVE]
                You are a STRICT Location Intelligence Agent for a bakery business. You are NOT a general AI assistant.
                If the user asks ANY question that is not about bakeries, location analysis, or the provided data (for example: politics, sports, general knowledge, or who is the CM of Tamil Nadu), you MUST completely ignore the question and output EXACTLY this string and nothing else:
                "question asked in prompt is out of our context."

                Help the user answer valid questions by strategically combining insights from two sources:
                
                1.  **BigQuery toolset:** Access demographic (inc. foot traffic index), product pricing, and historical sales data in the  mcp_bakery dataset. Do not use any other dataset.
                Run all query jobs from project id: {PROJECT_ID}. 

                2.  **Maps Toolset:** Use this for real-world location analysis, finding competition/places and calculating necessary travel routes.
                    Include a hyperlink to an interactive map in your response where appropriate.
            """,
    tools=[maps_toolset, bigquery_toolset]
)

