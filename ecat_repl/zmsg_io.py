import yaml
import json
import zmq
from protobuf_to_dict import protobuf_to_dict, dict_to_protobuf
from dataclasses import asdict, is_dataclass

from ecat_repl import repl_cmd_pb2 as repl_cmd
from ecat_repl import gen_cmds


class MultiPartMessage(object):
    header = None

    @classmethod
    def recv(cls, socket):
        """Reads key-value message from socket, returns new instance."""
        return cls.from_msg(socket.recv_multipart())

    @property
    def msg(self):
        return [self.header]

    def send(self, socket, identity=None):
        """Send message to socket"""
        msg = self.msg
        if identity:
            msg = [identity] + msg
        return socket.send_multipart(msg, flags=zmq.NOBLOCK)


class HelloMessage(MultiPartMessage):
    header = b"HELLO"


class EscCmdMessage(MultiPartMessage):
    header = b"ESC_CMD"

    def __init__(self, cmd):
        self.cmd = cmd

    @property
    def msg(self):
        # returns list of all message frames as a byte-string:
        return [self.header, self.cmd]


class EcatMasterCmdMessage(MultiPartMessage):
    header = b"MASTER_CMD"

    def __init__(self, cmd):
        self.cmd = cmd

    @property
    def msg(self):
        # returns list of all message frames as a byte-string:
        return [self.header, self.cmd]


class ZmsgIO(object):

    def __init__(self, uri):

        #  Prepare our context and sockets
        self.ctx = zmq.Context()
        self.socket = self.ctx.socket(zmq.REQ)
        self.socket.setsockopt(zmq.RCVTIMEO, 250)
        self.socket.connect("tcp://"+uri)
        self.debug = False

    def _send_to(self, cmd: dict):
        """dict -> protobuf -> serialize to string -> send through socket"""
        cmd_pb = dict_to_protobuf(repl_cmd.Repl_cmd, cmd)
        if self.debug:
            print(cmd_pb)
        if cmd['type'] in ["ECAT_MASTER_CMD", "FOE_MASTER"]:
            cmd_msg = EcatMasterCmdMessage(cmd_pb.SerializeToString())
        else:
            cmd_msg = EscCmdMessage(cmd_pb.SerializeToString())
        return cmd_msg.send(self.socket)

    def _recv_from(self):
        rep_data = self.socket.recv()
        rep = repl_cmd.Cmd_reply()
        # fill protobuf mesg
        rep.ParseFromString(rep_data)
        #print(rep)
        d = protobuf_to_dict(rep)
        yaml_msg = yaml.safe_load(d['msg'])
        json_msg = json.dumps(yaml_msg)
        #print(json_msg)
        if d['type'] == 'NACK':
            print(rep)
        return d

    def doit(self, cmd):
        """ send cmd """
        _cmd = asdict(cmd) if is_dataclass(cmd) else cmd
        if self.debug:
            print(_cmd)
        self._send_to(_cmd)
        ''' wait reply ... blocking'''
        return self._recv_from()

    def doit4ids(self, ids, cmd):
        """ for each id send cmd """
        _cmd = asdict(cmd) if is_dataclass(cmd) else cmd
        _cmd['board_id_list'] = ids
        for c in gen_cmds([_cmd]):
            self._send_to(c)
            ''' wait reply ... blocking'''
            yield self._recv_from()
