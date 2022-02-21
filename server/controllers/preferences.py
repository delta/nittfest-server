"""
Preferences Controller
"""

from server.schemas.domains import Domains


def get_preferences_by_id(preferences: list, database) -> list:
    """
    Method for getting preferences by its id in preferences table
    """
    size = len(preferences)
    pref_ids: list = [None] * size
    for i in range(1, size + 1):
        pref = (
            database.query(Domains)
            .filter_by(domain=preferences[i - 1])
            .first()
        )
        if pref:
            pref_ids[i - 1] = pref.id
    return pref_ids


def validate_preferences(preferences: list) -> bool:
    """
    Method for checking if prior preferences is NONE
    """
    is_prev_none = False
    for pref in preferences:
        if is_prev_none:
            break
        if not pref:
            is_prev_none = True
            continue
    return is_prev_none


def check_duplicate_preferences(preferences: list) -> bool:
    """
    Method for checking duplicates in preferences
    """
    ids = set()
    for pref in preferences:
        if pref in ids:
            return True
        ids.add(pref)
    return False
