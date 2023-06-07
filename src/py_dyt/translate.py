from typing import Any
from enum import Enum, auto


class State(Enum):
    WAITING = auto()
    CANCELED = auto()
    IN_VARIABLE = auto()
    IN_CONSTRUCTION = auto()


def translate(string: str, variables: dict[str, Any]) -> str:
    result = ''

    variable = ''
    state = State.WAITING

    for letter in string:
        if letter == "\\":
            state = State.CANCELED
        elif letter == '$':
            match state:
                case State.CANCELED:
                    state = State.WAITING
                    result += letter
                case State.WAITING:
                    state = State.IN_VARIABLE
                case State.IN_VARIABLE:
                    state = State.WAITING

                    result += str(variables[variable])
                    variable = ''

        elif state == State.IN_VARIABLE:
            variable += letter
        else:
            result += letter

    return result
