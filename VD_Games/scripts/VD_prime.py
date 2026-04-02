"""Entry point for VD-prime game."""
from VD_Games import engine
from VD_Games.games import prime


def main() -> None:
    """Run the prime game."""
    engine.run_game(prime)


if __name__ == "__main__":
    main()
