import pickle
from copy import copy
from typing import List, Literal

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from conway import Game

GAMEBOARD_FILE = "game_board.pkl"

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_render_home(request: Request):
    return templates.TemplateResponse("/home/index.html", {"request": request})


@app.post("/game/start", response_class=HTMLResponse)
async def post_startgame(request: Request):
    game = Game(x=25)
    game.start_game(type="random")

    with open(GAMEBOARD_FILE, "wb") as f:
        pickle.dump(game.board.tolist(), f)

    return templates.TemplateResponse(
        "/home/partials/running.html",
        {"request": request, "game_board": game.get_board()},
    )


@app.get("/game/running", response_class=HTMLResponse)
async def get_tickgame(request: Request):
    with open(GAMEBOARD_FILE, "rb") as f:
        game_board: List[List[Literal[0, 1]]] = pickle.load(f)

    game = Game(x=len(game_board))
    game.start_game(type="user", user_input=game_board)
    game._tick()
    new_game_board = game.board.tolist()

    with open(GAMEBOARD_FILE, "wb") as f:
        pickle.dump(game.board.tolist(), f)

    future_game = copy(game)
    future_game._tick()
    future_game_board = future_game.board.tolist()

    if game_board == new_game_board or game_board == future_game_board:
        return templates.TemplateResponse(
            "/home/partials/finished.html",
            {"request": request, "game_board": game.get_board()},
        )

    return templates.TemplateResponse(
        "/home/partials/running.html",
        {"request": request, "game_board": game.get_board()},
    )
