"""The state of the game is quark-gluon plasma."""

from enum import Enum


class GameState(Enum):

    PLAYING = 1
    END = 100


class StateMachine:

    initial_state = GameState.PLAYING

    def __init__(self):

        self.state: GameState = StateMachine.initial_state
