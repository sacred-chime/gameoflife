[![MIT License][license-shield]][license-url]

## About The Project

[![Conway's Game of Life Screen Shot][product-screenshot]](https://github.com/sacred-chime)

My implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). Built with Python, FastAPI, and HTMX. The purpose of this project is to create a demo that uses FastAPI and HTMX for the sake of learning.

The technologies that are new to me within this project:

- [![htmx][htmx.com]][HTMX-url]
- GitHub Actions
- mypy
- pytest

## Project Status

This project is currently in development. The backend logic is currently functional. My intention is to create a front-end which will let the user visualise and interact with the game.

## Installation and Setup Instructions

Installation:

1. Clone the repo

```bash
git clone https://github.com/sacred-chime/gameoflife

```

2. Install Python requirements

```bash
cd gameoflife
pip install -r requirements.txt
```

3. Start Web Server

```bash
uvicorn main:app --reload --port 11111
```

To run the test suite:

```bash
pytest tests.py
```

<!-- MARKDOWN LINKS & IMAGES -->

[license-shield]: https://img.shields.io/github/license/sacred-chime/gameoflife.svg?style=for-the-badge
[license-url]: https://github.com/sacred-chime/gameoflife/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[htmx.com]: https://img.shields.io/badge/HTMX-20232A?style=for-the-badge&logo=amazonapigateway&logoColor=61DAFB
[htmx-url]: https://htmx.org/
