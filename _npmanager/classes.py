# pylint: disable=C0111,R0201,C0325
"""
classes for npmanager
"""
import shlex
import sys
import select
import os
from functools import wraps
from subprocess import call, Popen, PIPE, STDOUT

from _npmanager.utils import commandutils as cmdutils
from _npmanager.utils import screen

class Package(object):
    COMMAND = ''
    SERVICE = ''
    SELECT = {}

    def __init__(self):
        self.process = None

    def select(self):
        val = screen.select(self.SELECT)
        if val == len(self.SELECT['options']):
            sys.exit(0)
        return val

    def write(self, inp):
        assert self.process
        self.process.stdin.write(inp)
        inp = inp.replace('\n', '\\n')
        sys.stdout.write(' \033[1m[send a key: {}]\033[0m'.format(inp))
        sys.stdout.flush()

    def lprint(self, text):
        cols, _ = cmdutils.termsize()
        print('-' * cols)
        print(text)
        print('-' * cols)

    def line_receiver(self, line):
        raise NotImplementedError('`line_receiver` method should be implemented!')

    def execute(self):
        self.lprint('Info: execute the following command: {}'.format(self.COMMAND))
        
        try:
            gen = self.call()
            while 1:
                line = gen.next()
                try:
                    self.line_receiver(line)
                except NotImplementedError as exc:
                    print('Error: {}'.format(exc))
                    self.process.terminate()
                    raise StopIteration()
        except KeyboardInterrupt:
            self.process.terminate()
        except StopIteration:
            pass

    def call(self):
        command = self.COMMAND
        self.process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, \
            stderr=STDOUT, close_fds=True)
        
        while 1:
            line = ''
            while 1:
                if self.process.poll() is not None:
                    raise StopIteration()
                char = self.process.stdout.read(1)
                line += char
                if char == ':' or char == '?' or char == '\n':
                    break

            sys.stdout.write(line)
            sys.stdout.flush()
            poll = self.process.poll()
            if poll is not None:
                raise StopIteration()
            else:
                yield line

    def start(self):
        _ = call('{} {}'.format(self.SERVICE, 'start'), shell=True)

    def stop(self):
        _ = call('{} {}'.format(self.SERVICE, 'stop'), shell=True)

    def reload(self):
        _ = call('{} {}'.format(self.SERVICE, 'reload'), shell=True)

    def restart(self):
        _ = call('{} {}'.format(self.SERVICE, 'restart'), shell=True)
