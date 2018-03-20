from binascii import hexlify

def unsynch_bits(number):
    number = int(hexlify(number), 16)
    first =  number & 0xff 
    second = (number >> 8) & 0xff
    third = (number >> 16) & 0xff
    fourth = (number >> 32) & 0xff
    return ((fourth & 0x7f) | 
            ((third & 0x7f) << 21) |
            ((second & 0x7f) << 14) |
            ((first & 0x7f) << 7))
