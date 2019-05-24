import math

from ecat_repl import MasterCmd, CtrlCmd

controller_type = {
    "00_idle_ctrl":        0x00,
    "3B_motor_pos_ctrl":   0x3B,
    "3C_link_pos_ctrl":    0x3C,
    "D4_impedance_ctrl":   0xD4,
    "71_motor_speed_ctrl": 0x71,
    "CC_current_ctrl":     0xCC,
}

master_cmd_stop = MasterCmd(u'STOP_MASTER')
master_cmd_start = MasterCmd(u'START_MASTER')
master_cmd_get_slave_descr = MasterCmd(u'GET_SLAVES_DESCR')

ctrl_cmd_start = CtrlCmd(u'CTRL_CMD_START')
ctrl_cmd_stop = CtrlCmd(u'CTRL_CMD_STOP')
ctrl_cmd_fan = CtrlCmd(u'CTRL_FAN')
ctrl_cmd_led = CtrlCmd(u'CTRL_LED')
ctrl_cmd_set_home = CtrlCmd(u'CTRL_SET_HOME')
ctrl_cmd_set_zero = CtrlCmd(u'CTRL_SET_ZERO_POSITION')
ctrl_cmd_set_min_pos = CtrlCmd(u'CTRL_SET_MIN_POSITION')
ctrl_cmd_set_max_pos = CtrlCmd(u'CTRL_SET_MAX_POSITION')


def gen_cmds(cmds: list):

    for cmd in cmds:
        if 'board_id_list' in cmd:
            id_list = cmd['board_id_list']
            del cmd['board_id_list']
            for _id in id_list:
                for key in ['ctrl_cmd', 'flash_cmd', 'trajectory_cmd']:
                    if key in cmd:
                        cmd[key]['board_id'] = _id
                        break
                    #else:
                        #print("no board_id key ...")
                yield cmd
        else:
            yield cmd



def flash_cmd_save2flash(bId=-1):
    _flash_cmd_save2flash = {"type": "FLASH_CMD", "flash_cmd": {"type": "SAVE_PARAMS_TO_FLASH", "board_id": -1}}
    if bId > 0:
        _flash_cmd_save2flash["flash_cmd"]["board_id"] = bId
    return _flash_cmd_save2flash
