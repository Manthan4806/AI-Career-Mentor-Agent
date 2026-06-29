import streamlit as st


def initialize_memory():

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "career_goal" not in st.session_state:
        st.session_state.career_goal = ""

    if "known_skills" not in st.session_state:
        st.session_state.known_skills = ""


def save_interaction(user_input, response):

    st.session_state.chat_history.append(
        {
            "user": user_input,
            "assistant": response
        }
    )


def update_goal(goal):

    st.session_state.career_goal = goal


def update_skills(skills):

    st.session_state.known_skills = skills