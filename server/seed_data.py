"""
Seed Question data
"""

from server.config.logger import logger
from server.config.database import SessionLocal
from server.schemas.questions import Questions


async def seed():
    """
    Seed the database with questions
    """
    try:
        database = SessionLocal()
        if database.query(Questions).count() == 0:
            logger.info("Seeding database with questions")
            data = [
                {
                    "question": "Are you interested in MoCing ?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC",
                },
                {
                    "question": "Who would you like to see at "
                    + "NITTFEST this year as a judge or guest?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC",
                },
                {
                    "question": "What ideas you have for promoting "
                    + "NITTFEST other than sharing online posts?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC",
                },
                {
                    "question": "What ideas you have for promoting "
                    + "NITTFEST other than sharing online posts?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC",
                },
                {
                    "question": "Ideate a few tagline suggestions",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC",
                },
                {
                    "question": "What are the clubs/teams you are part of? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "What measures will you take before conducting an "
                    + "offline event to ensure Covid19 protocols are "
                    + "followed? (In detail ) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "Were you part of the pre event? If yes, elaborate "
                    + "on your contributions.",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "How NOC differs from OC of other fests? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "What perks can you gain by being part of NOC? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "Who is better, Jack of All trades or Master of One? State"
                    + "reasons to support your views.",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC",
                },
                {
                    "question": "What do you bring to the marketing team that "
                    + "makes you a valuable asset? (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "List the clubs and teams that you are "
                    + "currently part of. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "What do you expect to achieve by joining "
                    + "NITTFest Marketing Team ? (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "Select a brand of your choice. Briefly "
                    + "explain how you will market it. (Word Limit: 150) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "How will you sell an umbrella with "
                    + "holes to a person drenched in rain ? (Word Limit: 150) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "If you were given the task of rebranding Starbucks "
                    + "company for the Cryptocurrency industry, what would "
                    + "the headline of the press release be? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "Would you rather be able to see 10 minutes into your own "
                    + "future or 10 minutes into the future of anyone but yourself?"
                    + "Explain your choice. (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING",
                },
                {
                    "question": "Tell about yourself in one sentence",
                    "options": [],
                    "is_subjective": True,
                    "domain": "AMBIENCE",
                },
                {
                    "question": "what are your Strengths and weaknesses?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "AMBIENCE",
                },
                {
                    "question": "which quality of You think ,that will suit ambience work ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "AMBIENCE",
                },
                {
                    "question": "Do you have any previous experience on Arts&crafts"
                    + " ,if yes , explain in brief.",
                    "options": [],
                    "is_subjective": True,
                    "domain": "AMBIENCE",
                },
                {
                    "question": "Interesting quality or fact about u .",
                    "options": [],
                    "is_subjective": True,
                    "domain": "AMBIENCE",
                },
                {
                    "question": "On a scale of 10 , Rate your patience and hardwork respectively",
                    "options": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                    "is_subjective": False,
                    "domain": "AMBIENCE",
                },
            ]
            logger.info(database)
            for quest in data:
                question = Questions(
                    question=quest["question"],
                    is_subjective=quest["is_subjective"],
                    domain=quest["domain"],
                    options=quest["options"],
                )
                database.add(question)
            database.commit()
            logger.info("Successfully seeded database with questions")
            database.close()
    except Exception as exception:
        logger.error(exception)
        database.rollback()
        database.close()
        raise exception
