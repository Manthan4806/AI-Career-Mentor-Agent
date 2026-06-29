ROADMAPS = {

    "AI Engineer": [
        "Learn Python",
        "Master NumPy & Pandas",
        "Study Machine Learning",
        "Build AI Projects",
        "Learn Deep Learning",
        "Apply for AI Internships"
    ],

    "Cybersecurity": [
        "Learn Networking",
        "Learn Linux",
        "Study Python",
        "Practice Ethical Hacking",
        "Build Security Projects",
        "Prepare for Security Certifications"
    ],

    "Data Science": [
        "Learn Python",
        "Learn Statistics",
        "Master Pandas",
        "Learn SQL",
        "Build Data Science Projects",
        "Practice Machine Learning"
    ],

    "Web Development": [
        "Learn HTML",
        "Learn CSS",
        "Learn JavaScript",
        "Learn React",
        "Build Projects",
        "Deploy Websites"
    ],

    "App Development": [
        "Learn Java/Kotlin",
        "Learn Android Studio",
        "Understand APIs",
        "Build Android Apps",
        "Publish Projects"
    ]
}


def career_roadmap(goal):

    return ROADMAPS.get(
        goal,
        ["Explore programming fundamentals"]
    )


def skill_gap(goal, skills):

    roadmap = career_roadmap(goal)

    skills = [
        skill.strip().lower()
        for skill in skills.split(",")
    ]

    missing = []

    for item in roadmap:

        found = False

        for skill in skills:

            if skill in item.lower():
                found = True
                break

        if not found:
            missing.append(item)

    return missing