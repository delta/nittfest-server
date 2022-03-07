"""
test constants
"""

test_user = {
    "id": 1,
    "name": "Muhesh",
    "email": "108121999@nitt.edu",
    "mobile_number": "9790546296",
    "gender": "MALE",
    "department_id": 2,
}

test_domains = [
    {
        "id": 1,
        "domain": "EVENTS",
        "descriptions": "If you're the type to come",
    },
    {
        "id": 2,
        "domain": "AMBIENCE",
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
        "is_subjective": bool(True),
        "options": None,
        "domain_id": 1,
        "year": 1,
    }
]

test_answers = [
    {"id": 1, "answer": "DeltaForce", "question_id": 1, "user_id": 1}
]

test_clusters = [
    {
        "id": 1,
        "name": "Arts",
        "image_link": "http://",
    },
]

test_events = [
    {
        "id": 1,
        "name": "dominoes",
        "description": "abc",
        "cluster_id": 1,
        "rules": "abc",
        "is_reg_completed": False,
        "is_event_completed": False,
        "form_link": "http://",
        "event_link": "http://",
        "start_time": "9.00",
        "end_time": "21.03.2022",
        "date": "20.03.2022",
        "image_link": "http://",
    },
]

test_points = [
    {
        "id": 1,
        "point": 20,
        "position": 1,
        "event_id": 1,
        "department_id": 2,
    },
]

test_departments = [
    {
        "id": 1,
        "name": "cse",
        "description": "cse",
    },
    {
        "id": 2,
        "name": "archi",
        "description": "archi",
    },
    {
        "id": 3,
        "name": "eee",
        "description": "eee",
    },
]
