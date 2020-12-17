#!/usr/bin/env python3
import os
import yaml
import argparse
from subprocess import PIPE, Popen

from ecat_repl import gen_cmds
from ecat_repl import repl_cmd
from ecat_repl import ZmsgIO
from ecat_repl import PipeIO


def repl_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_yaml", dest="repl_yaml", action="store", default="ecat_repl/test/test_repl.yaml")
    parser.add_argument("-c", dest="cmd_exec_cnt", action="store", type=int, default=1)
    args = parser.parse_args()
    dict_opt = vars(args)
    return dict_opt

            
def test_repl():

    opts = repl_option()
    d = yaml.load(open(opts["repl_yaml"], 'r'), Loader=yaml.FullLoader)

    proc = Popen(["repl"], stdout=PIPE, stderr=PIPE)

    if ( d['use_zmq']):
        io = ZmsgIO(d['uri'])
    else:
        io = PipeIO()

    #print(d)

    cnt = opts["cmd_exec_cnt"]
    while cnt:

        print("cmd_exec_cnt", cnt)
        cnt -= 1

        test_dict = {"type": "ECAT_MASTER_CMD", "ecat_master_cmd": {"type": "GET_SLAVES_DESCR"}}
        io.doit(test_dict)
        
        if not 'cmds' in d:
            continue

        for cmd_dict in gen_cmds(d['cmds']):
            io.doit(cmd_dict)
            #time.sleep(0.01)

        #time.sleep(0.05)

    proc.terminate()
    print(proc.stdout.readlines())

    print("Exit")

