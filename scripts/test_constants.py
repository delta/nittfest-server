"""
test constants
"""

test_user={
    "id":1,
    "name":"Muhesh",
    "email":"1081219067@nitt.edu",
    "mobile_number":"9790546296",
    "gender":"MALE"
}

test_domains =[
    {
        "id":1,
        "domain":"EVENTS",
        "descriptions": 'If you\'re the type to come up with the wildest ideas and live to see them realised, you\'d be a great fit for the NITTFEST Events Team. Our team prides in organising multiple offline and online events to keep the fest buzz going. Our main goal is to make the battle of departments a fair and enjoyable experience.\n\nApart from having the creative space to ideate, learning event management, and managing people, this team is a place to have fun, think out of the box and grow. NET looks for people with great creativity yet practicality, sheer dedication and hardwork.',     
    },
    {
        "id":2,
        "domain":"EVENTS",
        "descriptions": 'Team Ambience is in charge of creating a joyous feel for Nittfest by combining art and technology to create an elegant atmosphere.\n\nWith our stunning displays and unique characters that add charm to the fest, we light up the campus with our gorgeous lamps and recreate the place to enjoy.\n\nWe Ideate, Collaborate, Design, model, and Install on site in and around campus during the fest.\n\nWe add an experienced palette to all the happening spaces within the campus through setting the ambience of the overall mood to Nittfest.\n\nIf you are one with an artistic flair and a creative mind then Ambience is the place for you.\n\n',
    },
    {
        "id":3,
        "domain":"MARKETING",
        "descriptions": 'NITTFest Marketing Team lays the groundwork for NITTFest, seeking to raise the bar with each edition.\n\n We are responsible for increasing overall brand awareness, while also driving potential and recurring companies towards NITTFest. With coverts of corporate giants like Puma, The Princeton Review, Nestle, NMT retains them, and helps NITTFest attain the monetary funds required for a successful fest.\n\nThe NITTFest Marketing Team gives you the chance to show off your ingenuity and creativity while making vital contacts with the business sector, where you may polish your talents and find your niche. If you enjoy interacting with businesses and cooperating with them on a regular basis, the NITTFest Marketing Team is the place for you.\n\n',
    }
]

test_prefs=[
    {
        "id":1,
        "user_id":1,
        "preference_no":1,
        "domain_id":1
    },
    {
        "id":2,
        "user_id":1,
        "preference_no":2,
        "domain_id":2
    },
    {
        "id":3,
        "user_id":1,
        "preference_no":3,
        "domain_id":3
    }
]

test_questions=[{
  "id":1,
  "question":"Which is best club in NITT ?",
  "is_subjective":True,
  "options": None,
  "domain_id":1

}]

test_answers=[{
    "id":1,
    "answer":"DeltaForce",
    "question_id":1,
    "user_id":1
}]
