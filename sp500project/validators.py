from errors import IncorrectUserInputError
from errors import NotDigitError


def validate_user_choice(user_choice):
    if not user_choice.isdigit():
        raise NotDigitError("Choice must be digit.")

    elif int(user_choice) not in ("1", "5", "2", "3", "4"):
        raise IncorrectUserInputError("Choice must be 1 or 5.")


