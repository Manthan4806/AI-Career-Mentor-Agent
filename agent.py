import google.generativeai as genai
import os
from dotenv import load_dotenv

from planner import detect_goal, choose_tools
from tools import career_roadmap, skill_gap
from memory import update_goal, update_skills

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def run_agent(user_input, skills):

    # Step 1 - Planning
    goal = detect_goal(user_input)

    update_goal(goal)
    update_skills(skills)

    tools_used = choose_tools(goal)

    # Step 2 - Tool 1
    roadmap = career_roadmap(goal)

    # Step 3 - Tool 2
    missing_skills = skill_gap(goal, skills)

    # Step 4 - Final Prompt
    prompt = f"""
You are an AI Career Mentor.

User Goal:
{goal}

Known Skills:
{skills}

Career Roadmap:
{roadmap}

Missing Skills:
{missing_skills}

Give:
1. Career Summary
2. Personalized Advice
3. Recommended Learning Path
4. Projects to Build
5. Internship Preparation Tips
"""

    response = model.generate_content(prompt)

    return {
        "goal": goal,
        "tools": tools_used,
        "roadmap": roadmap,
        "missing": missing_skills,
        "response": response.text
    }