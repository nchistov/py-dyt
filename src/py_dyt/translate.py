from typing import Any
from enum import Enum, auto


class State(Enum):
    WAITING = auto()
    IN_VARIABLE = auto()


def translate(string: str, variables: dict[str, Any]) -> str:
    result = ''

    variable = ''
    state = State.WAITING

    for letter in string:
        if state == State.WAITING and letter == '$':
            state = State.IN_VARIABLE
        elif state == State.IN_VARIABLE:
            if letter == '$':
                state = State.WAITING

                result += str(variables[variable])
                variable = ''
            else:
                variable += letter
        else:
            result += letter

    return result
