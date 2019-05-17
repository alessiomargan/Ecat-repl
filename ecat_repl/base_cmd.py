import dataclasses


@dataclass
class Cmd:
    type: str
    board_id: int
    value: float


@dataclass
class Repl_cmd:
    type: str
    ctrl_cmd: Cmd
