from os import path
from binascii import hexlify, unhexlify

from common import unsynch_bits

class ID3Reader(object):

    def __init__(self, path):
        with open(path, 'rb') as f:
            self.file = f.read()
            

    def read_header(self):
        self.version = hexlify(self.file[3:5])
        self.flags = hexlify(self.file[6:7])
        self.size = unsynch_bits(str(self.file[7:10]))
        print self.size, hex(self.size)

    def collect_frames(self):
        pass

    def get_frames():
        pass

read = ID3Reader('feel.mp3')
read.read_header()

