"""Arithmetic progression game module."""
import random

DESCRIPTION = "What number is missing in the progression?"

PROGRESSION_LENGTH = 10


def generate_progression(start: int, step: int, length: int) -> list[int]:
    """Generate an arithmetic progression."""
    return [start + i * step for i in range(length)]


def get_question_and_answer() -> tuple[str, str]:
    """Generate question and correct answer for progression game."""
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)

    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer
