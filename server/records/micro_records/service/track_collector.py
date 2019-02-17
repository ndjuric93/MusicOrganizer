import os
import base64
import eyed3 as id_reader

from micro_utils.db.utils import get_or_create

from micro_records.config import MUSIC_ROOT
from micro_records.models import Artist, Album, Track
from micro_records import db

_collected_artists = {}
_collected_albums = {}
_collected_tracks = set()

def encode_no_image():
    with open("/micro_records/static/no_image.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string


def collect_tracks():
    # TODO Update so it collect pictures of the bands, albums etc. and to use Celery
    collected_tracks = {}
    for path in os.listdir(MUSIC_ROOT):
        if path.endswith('.mp3'):
            path = os.path.join(MUSIC_ROOT, path)
            track = id_reader.load(path).tag
            if track.artist not in _collected_artists:
                artist = add_artist(name=track.artist, image=encode_no_image())
                _collected_artists[track.artist] = artist.id
            if track.album not in _collected_albums:
                album = add_album(
                    artist_id=_collected_artists[track.artist],
                    name=track.album, image=encode_no_image()
                )
                _collected_albums[track.album] = album.id
            add_track(
                album_id=_collected_albums[track.album],
                name=track.title,
                track_number=track.track_num[0],
                genre = track.genre.name,
                path=path
            )
            _collected_tracks.add(track.title)
    return collected_tracks


def add_artist(**kwargs):
    return get_or_create(db.session, Artist, **kwargs)


def add_album(**kwargs):
    return get_or_create(db.session, Album, **kwargs)


def add_track(**kwargs):
    return get_or_create(db.session, Track, **kwargs)
