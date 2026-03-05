import random


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def get_correct_answer(number: int) -> str:
    """Return 'yes' if number is even, otherwise 'no'."""
    return "yes" if is_even(number) else "no"


def run_game() -> None:
    """Run the Even Game."""
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds_count = 3
    for _ in range(rounds_count):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ")
        correct_answer = get_correct_answer(number)

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")


def main() -> None:
    """Entry point for the VD-even command."""
    run_game()


if __name__ == "__main__":
    main()
