"""The state of the game is quark-gluon plasma."""

from enum import Enum


class GameState(Enum):

    INTRO = 0
    MENU = 5
    PLAYING = 10
    END = 100


class StateMachine:

    initial_state = GameState.INTRO

    def __init__(self):

        self.state: GameState = StateMachine.initial_state
