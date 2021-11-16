import sys
import time
import socket
import yaml
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
    ctrl_cmd_test_done,
    ctrl_cmd_test_error,
)
