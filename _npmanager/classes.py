"""
classes for npmanager
"""
import subprocess
import shlex
import sys
import os

class Package(object):
    COMMAND = ''

    def __init__(self):
        pass

    def write(self):
        pass

    def execute(self):
        gen = self.call()
        while 1:
            gen.next()

    def call(self):
        command = self.COMMAND
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                   stdin=subprocess.PIPE, bufsize=0,
                                   preexec_fn=os.setsid)
        while 1:
            line = ''
            while 1:
                char = process.stdout.read(1)
                line += char
                if char == ':' or char == '?' or char == '\n':
                    break

            sys.stdout.write(line)
            sys.stdout.flush()
            poll = process.poll()
            if poll is None:
                process.wait()
            elif poll is not None:
                raise StopIteration()
            else:
                yield line


