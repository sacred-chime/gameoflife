## Conway's Game of Life

Conway's Game of Life

My implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Built with Python, FastAPI, and HTMX. The purpose of this project is to create a demo that uses FastAPI and HTMX for the sake of learning.

The technologies that are new to me within this project:

- GitHub Actions
- mypy
- pytest
- HTMX

## Project Status

This project is currently in development. The backend logic is currently functional. My intention is to create a front-end which will let the user visualise and interact with the game.

## Installation and Setup Instructions

Installation:

```bash
git clone https://github.com/sacred-chime/gameoflife
cd gameoflife
```

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 11111
```

### OR

`If you have VS Code, run the "Server Start" task.`

To run the test suite:

```bash
pytest tests.py
```
