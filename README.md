<div align="center">

# durak-ai

A Python-based poker hand evaluator and card game AI engine

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/github/license/horse-3903/durak-ai?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/horse-3903/durak-ai?style=flat-square)](../../commits)

</div>

---

## Overview

`durak-ai` is a Python card game engine that implements a full 52-card deck, hand evaluation logic, and a multi-player game simulation. The core engine evaluates poker hands (Nothing, One Pair, Two Pairs, Three of a Kind, Straight, Flush, Full House, Four of a Kind, Straight Flush), deals cards, and determines winners based on hand rank and tie-breaking value.

## Features

- **Full 52-card deck**: all four suits (Clubs, Hearts, Spades, Diamonds) with standard face values
- **Poker hand evaluator**: classifies any 5-card hand into one of 9 hand ranks with tiebreaker scoring
- **Deck shuffling and dealing**: randomised deck with configurable deal counts
- **Multi-player game simulation**: deal cards to multiple players and automatically determine the winner
- **Extensible card and hand classes**, `Card`, `Card_Set`, `Deck`, `Player`, and `Game` classes for easy extension
- **Test suite**: pre-built test cases for all 9 hand types

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/horse-3903/durak-ai.git
   cd durak-ai
   ```

2. No external dependencies are required, the project uses only the Python standard library.

### Usage

Run the test suite to verify hand evaluation:
```bash
python src/test.py
```

To run a game simulation directly, import and use the `Game` class:
```python
from classes import Game

game = Game(["Alice", "Bob", "Charlie"])
game.play()
```

This deals 5 cards to each player, prints all hands, and announces the winner.

## Project Structure

```
durak-ai/
├── src/
│   ├── classes.py   # Core engine: Card, Card_Set, Deck, Player, Game
│   └── test.py      # Test cases for all 9 poker hand types
```

## Hand Rankings

| Rank | Hand |
|------|------|
| 0 | Nothing (high card) |
| 1 | One Pair |
| 2 | Two Pairs |
| 3 | Three of a Kind |
| 4 | Straight |
| 5 | Flush |
| 6 | Full House |
| 7 | Four of a Kind |
| 8 | Straight Flush |

## License

This project is licensed under the [MIT License](LICENSE).
