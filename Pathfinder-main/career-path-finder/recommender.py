def recommend_careers(profile):
    # Dummy recommendation logic — replace with your AI/ML model
    skills = profile.get("skills", [])
    interests = profile.get("interests", [])
    goals = profile.get("goals", "")

    return {
        "career_paths": [
            {"title": "Data Scientist", "match_score": 92},
            {"title": "ML Engineer", "match_score": 89},
            {"title": "AI Product Manager", "match_score": 85}
        ],
        "required_skills": ["Python", "Machine Learning", "Data Analysis"]
    }
