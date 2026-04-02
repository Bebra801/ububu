"""Entry point for VD-progression game."""
from VD_Games import engine
from VD_Games.games import progression


def main() -> None:
    """Run the progression game."""
    engine.run_game(progression)


if __name__ == "__main__":
    main()

