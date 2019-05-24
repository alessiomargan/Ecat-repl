from dataclasses import dataclass, field, asdict, InitVar

# https://github.com/konradhalas/dacite
# import dacite
# https://github.com/eigenein/protobuf
# import pure-protobuf

# In Python returning `self` in the instance method is one way to implement the fluent pattern.


# CtrlCmd ###

@dataclass
class _Gains:
    type: str
    kp: float
    ki: float
    kd: float
    kkp: float = 0.0
    kki: float = 0.0
    kkd: float = 0.0


@dataclass
class _CtrlCmd:
    type: str
    board_id: int = -1
    value: float = 0.0
    gains: _Gains = field(default_factory=dict, init=False)


@dataclass
class CtrlCmd:
    ctrl_cmd_type: InitVar[str]
    ctrl_cmd: _CtrlCmd = field(default_factory=dict, init=False)
    type: str = u'CTRL_CMD'

    def __post_init__(self, ctrl_cmd_type):
        self.ctrl_cmd = _CtrlCmd(ctrl_cmd_type)

    def set_bid(self, bid):
        self.ctrl_cmd.board_id = bid
        return self

    def set_value(self, value):
        self.ctrl_cmd.value = value
        return self

    def set_gains(self, *gains):

        self.ctrl_cmd.gains = _Gains(*gains)
        return self

# FoeMaster ###

@dataclass
class _FoeMaster:
    filename: str
    password: int
    mcu_type: str
    slave_pos: int = -1


@dataclass
class FoeMaster:
    foe_master_init: InitVar[dict]
    foe_master: _FoeMaster = field(default_factory=dict, init=False)
    type: str = u'FOE_MASTER'

    def __post_init__(self, foe_master_init):
        if isinstance(foe_master_init, dict):
            self.foe_master = _FoeMaster(**foe_master_init)
        else:
            self.foe_master = _FoeMaster(*foe_master_init)


# MasterCmd ###

@dataclass
class _MasterCmd:
    type: str


@dataclass
class MasterCmd:
    master_cmd_type: InitVar[str]
    ecat_master_cmd: _MasterCmd = field(default_factory=dict, init=False)
    type: str = u'ECAT_MASTER_CMD'

    def __post_init__(self, master_cmd_type):
        self.ecat_master_cmd = _MasterCmd(master_cmd_type)



