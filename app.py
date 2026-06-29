import streamlit as st

from memory import initialize_memory, save_interaction
from agent import run_agent

st.set_page_config(
    page_title="AI Career Mentor Agent",
    page_icon="🤖",
    layout="wide"
)

initialize_memory()

st.title("🤖 AI Career Mentor Agent")
st.caption(
    "An Agentic AI application that uses planning, memory, tools, and Gemini AI to provide personalized career guidance."
)
st.subheader("🔄 Agent Workflow")

st.info("""
User Query
⬇️
Planning
⬇️
Career Roadmap Tool
⬇️
Skill Gap Analysis Tool
⬇️
Memory
⬇️
Gemini AI
⬇️
Final Recommendation
""")

st.write(
    "An Agentic AI application that helps you plan your career using planning, memory, tools, and Gemini."
)

with st.sidebar:

    st.header("Memory")

    st.write("**Current Career Goal:**")
    st.write(st.session_state.career_goal)

    st.write("**Known Skills:**")
    st.write(st.session_state.known_skills)

st.subheader("Career Query")

user_input = st.text_area(
    "What career do you want to pursue?"
)

skills = st.text_input(
    "Enter your current skills (comma separated)"
)

if st.button("Run Agent"):

    if not user_input.strip():

        st.warning("Please enter your career goal.")

    else:

        with st.spinner("Agent is planning and using tools..."):

            result = run_agent(
                user_input,
                skills
            )

        save_interaction(
            user_input,
            result["response"]
        )

        st.success("Agent completed the workflow!")

        st.subheader("🧠 Step 1 - Planning")

        st.success("Planning Complete")

        st.write("**Detected Career Goal:**")

        st.info(result["goal"])

        st.subheader("🛠 Step 2 - Tool Selection")

        st.success("Tools Selected Successfully")

        st.write("The agent decided to use the following tools:")

        for tool in result["tools"]:
          st.write("✅", tool)

        st.subheader("📚 Step 3 - Tool Execution")

        st.success("Career Roadmap Generated")

        st.write("The Career Roadmap Tool generated the following learning path:")

        for step in result["roadmap"]:
            st.write("•", step)

        st.subheader("📈 Step 4 - Skill Gap Analysis")

        st.success("Skill Gap Analysis Completed")

        st.write("The Skill Gap Tool compared your current skills with the career roadmap.")

        if result["missing"]:
            for skill in result["missing"]:
                st.write("❌", skill)
        else:
            st.success("No major skill gaps detected!")

        st.subheader("🧠 Step 5 - Agent Decision")

        st.success("Decision Making Completed")

        st.write(f"**Detected Goal:** {result['goal']}")

        st.write("**Why these tools were selected:**")

        st.write("""
- The Career Roadmap Tool creates a structured learning path.
- The Skill Gap Analysis Tool compares your current skills with the required roadmap.
- Memory stores your career goal and skills for future interactions.
- Gemini combines all this information to generate personalized recommendations.
""")

        st.subheader("🤖 Final AI Recommendation")

        st.markdown(result["response"])

        st.divider()

        st.subheader("Conversation History")

        for chat in reversed(st.session_state.chat_history):

         st.markdown(f"**👤 User:** {chat['user']}")

         st.markdown(f"**🤖 Agent:** {chat['assistant']}")

         st.divider()