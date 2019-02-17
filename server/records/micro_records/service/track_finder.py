import os

from micro_records import celery

@celery.task
def walk_directory(root, extensions=['.mp3']):
    pass
