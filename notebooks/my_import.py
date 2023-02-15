import sys
import time
import socket
import yaml
import math
from  pprint import pprint as pp
from dataclasses import asdict
import ipywidgets.widgets as widgets
from IPython.display import display

print(sys.executable)

from ecat_repl import ZmsgIO
from ecat_repl import FoeMaster
from ecat_repl import CtrlCmd
from ecat_repl import SdoCmd
from ecat_repl import SdoInfo

from ecat_repl import (
    master_cmd_stop,
    master_cmd_start,
    master_cmd_get_slave_descr,
    #
    flash_cmd_load_default,
    flash_cmd_save_flash,
    flash_cmd_load_flash,
    #
    ctrl_cmd_start,
    ctrl_cmd_stop,
    ctrl_cmd_fan,
    ctrl_cmd_led,
    ctrl_cmd_run_torque_calib,
    ctrl_cmd_set_home,
    ctrl_cmd_set_zero,
    ctrl_cmd_set_min_pos,
    ctrl_cmd_set_max_pos,
    ctrl_cmd_set_position,
    ctrl_cmd_set_gains,
    ctrl_cmd_set_velocity,
    ctrl_cmd_set_torque,
    ctrl_cmd_set_current,
    ctrl_cmd_dac_tune,
    ctrl_cmd_get_adc,
    ctrl_cmd_set_dac,
    ctrl_cmd_set_dac_flash,
    ctrl_cmd_test_done,
    ctrl_cmd_test_error,
)

status_cmds = {
    'FAN_ON':           0x0026,
    'FAN_OFF':			0x0062,
    'LED_ON':           0x0019,
    'LED_OFF':          0x0091,
    'RELEASE_BRAKE':    0x00BD,
    'ENGAGE_BRAKE':     0x00DB,
}
reply_cmds = {
    'CMD_DONE':         0x7800,
    'CMD_WORKING':		0xD000,
    'CMD_ERROR':		0xAA00,
    'CMD_NOCOND':       0xBB00,
}

# set default uri
uri = socket.gethostname()+".local:5555"
_io = ZmsgIO(uri)

def set_uri(uri):
    global _io
    print('new uri {}'.format(uri))
    _io = ZmsgIO(uri)
    return _io

def reply_cmd(cmd):
    reply = _io.doit(cmd)
    yaml_msg = yaml.safe_load(reply['msg'])
    return yaml_msg

def ctrl_status_cmd(ctrl_cmd: int, bid: int):
    msg = reply_cmd(SdoCmd(rd_sdo=[],wr_sdo={'ctrl_status_cmd': ctrl_cmd}).set_bid(bid))
    msg = reply_cmd(SdoCmd(rd_sdo=['ctrl_status_cmd_ack'],wr_sdo={}).set_bid(bid))
    print(hex(msg['ctrl_status_cmd_ack']))
    return msg['ctrl_status_cmd_ack'] == ctrl_cmd + reply_cmds['CMD_DONE']

def ctrl_status_cmd_str(ctrl_cmd: str, bid: int):
    return ctrl_status_cmd(status_cmds[ctrl_cmd], bid) 

def sdo_filter(snames:list, sdos:dict):
    return {key:sdos[key] for key in snames}

def read_sdo(rd_sdos:list, ids:list):
    d = dict()
    for iD in ids:
        yaml_msg = reply_cmd(SdoCmd(rd_sdo=rd_sdos,wr_sdo={}).set_bid(iD))
        d[iD] = yaml_msg
    return d

def write_sdo(wr_sdo:dict, ids:list):
    d = dict()
    wr_keys = list(wr_sdo.keys())
    for iD in ids:
        yaml_msg = reply_cmd(SdoCmd(rd_sdo=wr_keys,wr_sdo=wr_sdo).set_bid(iD))
        d[iD] = yaml_msg
    return d