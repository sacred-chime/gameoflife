import pickle
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
        game_board_0: List[List[Literal[0, 1]]] = pickle.load(f)

    game = Game(x=len(game_board_0))
    game.start_game(type="user", user_input=game_board_0)

    game._tick()
    game_board_1 = game.board.tolist()

    with open(GAMEBOARD_FILE, "wb") as f:
        pickle.dump(game.board.tolist(), f)

    game._tick()
    game_board_2 = game.board.tolist()

    # Arbitrary stopping point so that it doesn't loop forever.
    #   if 1 or 2 steps is the same as the current step, then the game is over.
    if game_board_0 == game_board_1 or game_board_0 == game_board_2:
        return templates.TemplateResponse(
            "/home/partials/finished.html",
            {"request": request, "game_board": game.get_board()},
        )

    return templates.TemplateResponse(
        "/home/partials/running.html",
        {"request": request, "game_board": game.get_board()},
    )
