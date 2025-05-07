from flask import Blueprint, request, jsonify
from services.recommender import recommend_careers

career_bp = Blueprint('career', __name__)

@career_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    user_profile = {
        "skills": data.get("skills", []),
        "interests": data.get("interests", []),
        "goals": data.get("goals", "")
    }
    recommendations = recommend_careers(user_profile)
    return jsonify(recommendations)
