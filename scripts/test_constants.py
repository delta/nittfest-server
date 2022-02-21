"""
test constants
"""

test_user = {
    "id": 1,
    "name": "Muhesh",
    "email": "1081219067@nitt.edu",
    "mobile_number": "9790546296",
    "gender": "MALE",
}

test_domains = [
    {
        "id": 1,
        "domain": "EVENTS",
        "descriptions": "If you're the type to come",
    },
    {
        "id": 2,
        "domain": "EVENTS",
        "descriptions": "Team Ambience is in charge",
    },
    {
        "id": 3,
        "domain": "MARKETING",
        "descriptions": "NITTFest Marketing Team lays the groundwork",
    },
]

test_prefs = [
    {"id": 1, "user_id": 1, "preference_no": 1, "domain_id": 1},
    {"id": 2, "user_id": 1, "preference_no": 2, "domain_id": 2},
    {"id": 3, "user_id": 1, "preference_no": 3, "domain_id": 3},
]

test_questions = [
    {
        "id": 1,
        "question": "Which is best club in NITT ?",
        "is_subjective": True,
        "options": None,
        "domain_id": 1,
    }
]

test_answers = [
    {"id": 1, "answer": "DeltaForce", "question_id": 1, "user_id": 1}
]
