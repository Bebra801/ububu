"""Even game module."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def get_question_and_answer() -> tuple[str, str]:
    """Generate question and correct answer for even game."""
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer
