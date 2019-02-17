from multiprocessing import Process

from kafka import KafkaConsumer

from micro_utils.proto.SimpleSong_pb2 import SimpleSong
from micro_utils.proto.Song_pb2 import Song

from micro_statistics import db
from micro_statistics.config import KAFKA_SERVER
from micro_statistics.models import TrackSelectedCount, GenreSelected, TrackPlayedCount

def collect_selected_songs(app):
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVER['address'],
        group_id='track_selected'
    )
    consumer.subscribe(topics=('track_selected',))
    while True:
        for message in consumer:
            song = SimpleSong()
            song.ParseFromString(message.value)

            with app.app_context():
                add_object(
                    TrackSelectedCount,
                    id=song.song_id,
                    author=song.author,
                    name=song.name,
                )
                add_object(GenreSelected, name=song.genre)

def collect_played_songs(app):
    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_SERVER['address'],
        group_id='song_played'
    )
    consumer.subscribe(topics=('song_played',))
    while True:
        for message in consumer:
            song = Song()
            song.ParseFromString(message.value)

            with app.app_context():
                add_object(
                    TrackPlayedCount,
                    name=song.name,
                )

def add_object(model, **kwargs):
    obj = model.query.filter_by(**kwargs).first()
    if obj is None:
        obj = model(count=1, **kwargs)
    else:
        obj.count = obj.count + 1
    db.session.add(obj)
    db.session.commit()


def start_selection_listening(app):
    Process(target=collect_selected_songs, args=(app,)).start()
    Process(target=collect_played_songs, args=(app,)).start()
