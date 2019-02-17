from micro_utils.proto.Song_pb2 import Song

def parse_song(message):
    song = Song()
    song.ParseFromString(message.value)
    return song
