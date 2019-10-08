from dataclasses import dataclass, field, asdict, InitVar
from typing import List

# https://github.com/konradhalas/dacite
# import dacite
# https://github.com/eigenein/protobuf
# import pure-protobuf

# In Python returning `self` in the instance method is one way to implement the fluent pattern.


# FlashCmd ###

@dataclass
class _FlashCmd:
    type: str
    board_id: int = -1


@dataclass
class FlashCmd:
    flash_cmd_type: InitVar[str]
    flash_cmd: _FlashCmd = field(default_factory=dict, init=False)
    type: str = u'FLASH_CMD'

    def __post_init__(self, flash_cmd_type):
        self.flash_cmd = _FlashCmd(flash_cmd_type)

    def set_bid(self, bid):
        self.flash_cmd.board_id = bid
        return self


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


# SdoCmd ###

@dataclass
class _WrSdo:
    name: str
    value: float

@dataclass
class _SdoCmd:
    board_id: int = -1
    rd_sdo: List[str] = field(default_factory=list)
    wr_sdo: _WrSdo = field(default_factory=dict)

    def __post_init__(self):
        self.wr_sdo = [_WrSdo(n, v) for (n, v) in self.wr_sdo.items()]

@dataclass
class SdoCmd:
    rd_sdo: InitVar[List[str]]
    wr_sdo: InitVar[dict]
    slave_sdo_cmd: _SdoCmd = field(default_factory=dict, init=False)
    type: str = u'SLAVE_SDO_CMD'

    def __post_init__(self, _rd_sdo, _wr_sdo):
        self.slave_sdo_cmd = _SdoCmd(rd_sdo=_rd_sdo, wr_sdo=_wr_sdo)

    def set_bid(self, bid):
        self.slave_sdo_cmd.board_id = bid
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

    def set_slave_pos(self, bid):
        self.foe_master.slave_pos = bid
        return self


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



