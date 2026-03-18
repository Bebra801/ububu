"""Entry point for VD-gcd game."""
from VD_Games import engine
from VD_Games.games import gcd

def main() -> None:
    """Run the GCD game."""
    engine.run_game(gcd)

if __name__ == "__main__":
    main()
