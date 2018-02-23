"""
This file is used to generate ID3 Header
"""

from sys import getsizeof
from struct import pack

# ID3 Declaration 
tag_header = 'ID3' 

version = 0x03
rev = 0x00

# Flags
sync = 0x80
extended = 0x40
experimental = 0x10

# Declared Frames

frames = { 
    'title' : 'TIT2',
    'track_no' :'TRCK',
    'year' : 'TYER',
    'length' : 'TLEN',
    'artist' : 'TOPE'
}

class ID3(object):

    def __init__(self, *args, **kwargs):
       super(ID3, self).__init__()
       self.args = args
       self.kwargs = kwargs
       self.size = 0
   
    def generate_header(self, sync, extended, experimental):
        '''
        Headers consists of
            file identifier   'ID3'
            version           $xx xx
            flags             %abc00000
            size              4 * %0xxxxxxx
        '''
        self.size += 10
        hdr = tag_header + chr(version) + chr(rev)
        flag = 0
        if(sync): 
            flag = flag | sync
        if(extended):
            flag = flag | extended
        if(experimental):
            flag = flag | experimental
        return hdr + chr(flag) + pack('B', self.size) + str(size).zfill(8)

    def generate_frame(self, tag, value, flags): 
        '''
        Frame header consists of 
            Frame ID $xx xx xx xx
            Size     $xx xx xx xx
            Flags    $xx xx
        '''
        return tag + str(getsizeof(value)).rjust(8, '\0') + chr(flags)+ value

    def calc_size(self):
        pass

    def get_tag(self):
        tag = self.generate_header(False, False, False, 0) 
        for key, value in self.kwargs.items():
            tag += self.generate_frame(frames[key], value, 0)
        return tag


