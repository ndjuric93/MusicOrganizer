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

# Declared Existing Frames
frames = { 
    'title' : 'TIT2',
    'track_no' :'TRCK',
    'year' : 'TYER',
    'length' : 'TLEN',
    'artist' : 'TOPE'
}

class ID3Writer(object):

    def __init__(self, *args, **kwargs):
        '''
        The constructor
        '''
        super(ID3Writer, self).__init__()
        self.args = args
        self.kwargs = kwargs
        self.size = 0
   
    def generate_header(self, _sync, _extended, _experimental, size):
        '''
        Headers consists of
            file identifier   'ID3'
            version           $xx xx
            flags             %abc00000
            size              4 * %0xxxxxxx
        '''
        hdr = tag_header + chr(version) + chr(rev)
        flag = 0
        if(_sync): 
            flag = flag | sync
        if(_extended):
            flag = flag | extended
        if(_experimental):
            flag = flag | experimental
        return hdr + chr(flag) + '0' + str(size).zfill(8)

    def generate_frame(self, tag, value, flags): 
        '''
        Frame header consists of 
            Frame ID $xx xx xx xx
            Size     $xx xx xx xx
            Flags    $xx xx
        '''
        return tag + str(getsizeof(value)).rjust(8, '\0') + chr(flags)+ value

    def create_size(self):
        size = len(self.frames)
        border = 0x7f
        size = size | border

    def get_tag(self):
        self.frames = ''.join([self.generate_frame(frames[key], value, 0) for key, value 
            in self.kwargs.items()])
        return self.generate_header(False, False, False, 0) + self.frames

id3 = ID3Writer(artist='The Clash', title='London Calling')
with open('file.txt', 'wb') as f:
    f.write(id3.get_tag())
id3.create_size()
