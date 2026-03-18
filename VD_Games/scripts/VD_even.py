"""Entry point for VD-even game."""
from VD_games import engine
from VD_games.games import even


def main() -> None:
    """Run the even game."""
    engine.run_game(even)


if __name__ == "__main__":
    main()
