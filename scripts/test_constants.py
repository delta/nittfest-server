"""
test constants
"""

from datetime import datetime


test_user = {
    "id": 1,
    "name": "Muhesh",
    "email": "108121999@nitt.edu",
    "mobile_number": "9790546296",
    "gender": "MALE",
    "department_id": 2,
    "fcm_token": "123",
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

test_departments = [
    {"id": 1, "name": "MME", "description": "Gods"},
    {"id": 2, "name": "EEE", "description": "some generic description"},
    {"id": 3, "name": "ICE", "description": "some generic description"},
]

test_clusters = [
    {
        "name": "Arts",
        "image_link": "http://genericlink.com/route",
    },
    {
        "name": "Gaming",
        "image_link": "http://genericlink.com/route",
    },
]

test_events = [
    {
        "name": "Art Event 1",
        "description": "Art Something",
        "cluster_id": 1,
        "rules": "free play",
        "form_link": "http://genericlink.com/route",
        "event_link": "http://genericlink.com/route",
        "image_link": "http://genericlink.com/route",
        "start_time": datetime(2012, 3, 3, 10, 10, 10),
        "end_time": datetime(2012, 3, 3, 10, 10, 10),
        "is_reg_completed": False,
        "is_event_completed": False,
    },
    {
        "name": "Art Event 2",
        "description": "Art Something",
        "cluster_id": 1,
        "rules": "free play",
        "form_link": "http://genericlink.com/route",
        "event_link": "http://genericlink.com/route",
        "image_link": "http://genericlink.com/route",
        "start_time": datetime(2012, 3, 3, 10, 10, 10),
        "end_time": datetime(2012, 3, 3, 10, 10, 10),
        "is_reg_completed": False,
        "is_event_completed": False,
    },
    {
        "name": "Gaming Event 1",
        "description": "Game Something",
        "cluster_id": 2,
        "rules": "free play",
        "form_link": "http://genericlink.com/route",
        "event_link": "http://genericlink.com/route",
        "image_link": "http://genericlink.com/route",
        "start_time": datetime(2012, 3, 3, 10, 10, 10),
        "end_time": datetime(2012, 3, 3, 10, 10, 10),
        "is_reg_completed": False,
        "is_event_completed": False,
    },
    {
        "name": "Gaming Event 2",
        "description": "Game Something",
        "cluster_id": 2,
        "rules": "free play",
        "form_link": "http://genericlink.com/route",
        "event_link": "http://genericlink.com/route",
        "image_link": "http://genericlink.com/route",
        "start_time": datetime(2012, 3, 3, 10, 10, 10),
        "end_time": datetime(2012, 3, 3, 10, 10, 10),
        "is_reg_completed": False,
        "is_event_completed": False,
    },
]

test_points = [
    {
        "point": 10,
        "position": 1,
        "event_id": 1,
        "department_id": 1,
    },
    {
        "point": 9,
        "position": 2,
        "event_id": 1,
        "department_id": 2,
    },
    {
        "point": 0,
        "position": 3,
        "event_id": 1,
        "department_id": 3,
    },
    {
        "point": 20,
        "position": 1,
        "event_id": 2,
        "department_id": 3,
    },
    {
        "point": 10,
        "position": 2,
        "event_id": 2,
        "department_id": 2,
    },
    {
        "point": 5,
        "position": 3,
        "event_id": 2,
        "department_id": 1,
    },
    {
        "point": 10,
        "position": 1,
        "event_id": 3,
        "department_id": 1,
    },
    {
        "point": 9,
        "position": 2,
        "event_id": 3,
        "department_id": 2,
    },
    {
        "point": 8,
        "position": 3,
        "event_id": 3,
        "department_id": 3,
    },
    {
        "point": 10,
        "position": 1,
        "event_id": 4,
        "department_id": 3,
    },
    {
        "point": 9,
        "position": 2,
        "event_id": 4,
        "department_id": 1,
    },
    {
        "point": 5,
        "position": 3,
        "event_id": 4,
        "department_id": 2,
    },
]
