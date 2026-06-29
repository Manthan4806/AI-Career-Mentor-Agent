def detect_goal(user_input):

    text = user_input.lower()

    if "cyber" in text:
        return "Cybersecurity"

    elif "ai" in text or "machine learning" in text:
        return "AI Engineer"

    elif "data" in text:
        return "Data Science"

    elif "web" in text:
        return "Web Development"

    elif "app" in text or "android" in text:
        return "App Development"

    else:
        return "General Technology"


def choose_tools(goal):

    tools = ["Career Roadmap"]

    if goal != "General Technology":
        tools.append("Skill Gap Analysis")

    return tools