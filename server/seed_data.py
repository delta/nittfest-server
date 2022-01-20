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
                    "domain": "PRC2",
                },
                {
                    "question": "Who would you like to see at "
                    + "NITTFEST this year as a judge or guest?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC2",
                },
                {
                    "question": "What ideas you have for promoting "
                    + "NITTFEST other than sharing online posts?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC2",
                },
                {
                    "question": "What ideas you have for promoting "
                    + "NITTFEST other than sharing online posts?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC2",
                },
                {
                    "question": "Ideate a few tagline suggestions",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC2",
                },
                {
                    "question": "Are you interested in MoCing? "
                    + "(Yes/No/Interested in Trying) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "What do you think are some exciting things we "
                    + "can do to hype up the fest? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "Write a short para (150 words) on how you "
                    + "imagine the general atmosphere of the fest would be? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "What do you think are the qualities of a good "
                    + "Master of Ceremonies (Presenter/Host) of an event? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "Give a clever and apt alternative title to "
                    + "the Fest that captures the spirit of the competition "
                    + "between the departments. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "An imminent personality has come down as "
                    + "a guest. How would you go about preparing "
                    + "for an interview with them? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "PRC1",
                },
                {
                    "question": "What are the clubs/teams you are part of? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "What measures will you take before conducting an "
                    + "offline event to ensure Covid19 protocols are "
                    + "followed? (In detail ) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "Were you part of the pre event? If yes, elaborate "
                    + "on your contributions.",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "How NOC differs from OC of other fests? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "What perks can you gain by being part of NOC? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "Who is better, Jack of All trades or Master of "
                    + "One? State reasons to support your views.",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC2",
                },
                {
                    "question": "Explain NITTFEST using five words. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC1",
                },
                {
                    "question": "Why do you want to be part of OC? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC1",
                },
                {
                    "question": "What can you contribute to the team? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC1",
                },
                {
                    "question": "Suggest a theme for NITTFEST. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC1",
                },
                {
                    "question": "Who is better, Jack of all trades or Master "
                    + "of One? State reason to support your views. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "NOC1",
                },
                {
                    "question": "What do you bring to the marketing team that "
                    + "makes you a valuable asset? (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "List the clubs and teams that you are "
                    + "currently part of. ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "What do you expect to achieve by joining "
                    + "NITTFest Marketing Team ? (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "Select a brand of your choice. Briefly "
                    + "explain how you will market it. (Word Limit: 150) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "How will you sell an umbrella with "
                    + "holes to a person drenched in rain ? (Word Limit: 150) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "If you were given the task of rebranding Starbucks "
                    + "company for the Cryptocurrency industry, what would "
                    + "the headline of the press release be? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "Would you rather be able to see 10 minutes into your own "
                    + "future or 10 minutes into the future of anyone but yourself?"
                    + "Explain your choice. (Word Limit: 100) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING2",
                },
                {
                    "question": "What makes you a good marketing team member ?",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING1",
                },
                {
                    "question": "Write about a time where you worked with a "
                    + "team to complete a task successfully. What were your "
                    + "contributions ? (In 150 words) ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING1",
                },
                {
                    "question": "Name few companies that you would like "
                    + "to see at NITTFEST'22 ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING1",
                },
                {
                    "question": "Give 5 creative ways to use a broken tree branch ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING1",
                },
                {
                    "question": "What do you expect to achieve by joining NMT? ",
                    "is_subjective": True,
                    "options": [],
                    "domain": "MARKETING1",
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
                {
                    "question": "Which teams are you currently a part of?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "DESIGN",
                },
                {
                    "question": "Why do you want to be a part of NITTFEST design team?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "DESIGN",
                },
                {
                    "question": "Which design softwares are you familiar with?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "DESIGN",
                },
                {
                    "question": "What made you choose NITTFEST Events as one of your preferences?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "State an instance wherein you thought on your feet"
                    + " and made quick decisions.",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "From the previous editions of NITTFEST, choose one "
                    + "cluster and explain one or two events under it. ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "Assume you're in charge of an event taking place"
                    + " on the CEESAT ground. "
                    + "A bull enters the ring in the middle of the event. What will you do? ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "A time machine is given to you. You may only use "
                    + "it for silly purposes. "
                    + "What would be the craziest thing you could do with it?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "You accidently ate the sun for breakfast,"
                    + "and now the entire world is blaming you,"
                    + " including the plants, for depriving the globe of its only"
                    + " source of energy, and labelling you a traitor."
                    + " How would you calm the sudden fury and compensate for the sun's absence?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "Why should we induct you into the team?",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS2",
                },
                {
                    "question": "What do you think NITTFEST is? ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
                },
                {
                    "question": "What made you choose NITTFEST Events "
                    + "as one of your preferences? ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
                },
                {
                    "question": "State an instance wherein you thought on "
                    + "your feet and made quick decisions. ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
                },
                {
                    "question": "Ideate an online event that we can have "
                    + "during NITTFEST. ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
                },
                {
                    "question": "A time machine is given to you. You may "
                    + "only use it for silly purposes. What would "
                    + "be the craziest thing you could do with it? ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
                },
                {
                    "question": "Why should we induct you into the team? ",
                    "options": [],
                    "is_subjective": True,
                    "domain": "EVENTS1",
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
