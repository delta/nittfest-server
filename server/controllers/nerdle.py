"""
Nerdle Guess Validation Controller
"""

from server.models.nerdle import WinningGuessModel


def validate_guess_controller(
    answer: str,
    unvalidated_guess: str,
) -> WinningGuessModel:
    """
    Controller to Validate Guess
    """
    validated_guess: list = []
    correct_letters = 0
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
