"""
Nerdle Guess Validation Controller
"""

from functools import lru_cache
from server.models.nerdle import WinningGuessModel
from scripts.constants import valid_guesses


def validate_guess_controller(
    answer: str,
    unvalidated_guess: str,
) -> WinningGuessModel:
    """
    Controller to Validate Guess
    """
    validated_guess: list = []
    correct_letters = 0
    unvalidated_guess = unvalidated_guess.lower()
    answer = answer.lower()
    for i in range(5):
        if unvalidated_guess[i] == answer[i]:
            validated_guess.append([unvalidated_guess[i], "G"])
            correct_letters += 1
        elif unvalidated_guess[i] in answer:
            validated_guess.append([unvalidated_guess[i], "Y"])
        else:
            validated_guess.append([unvalidated_guess[i], "B"])
    is_win = correct_letters == 5
    return WinningGuessModel(
        validated_guess=validated_guess, is_win=is_win
    )


@lru_cache()
def is_valid_word(word: str) -> bool:
    """
    Check if word is valid
    """
    if len(word) != 5:
        return False
    return word in valid_guesses
