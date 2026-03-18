"""Entry point for VD-calc game."""
from VD_Games import engine
from VD_Games.games import calc

def main() -> None:
    """Run the calculator game."""
    engine.run_game(calc)

if __name__ == "__main__":
    main()

