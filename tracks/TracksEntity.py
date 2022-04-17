from peewee import *

db = SqliteDatabase('database.db')


class TracksEntity(Model):
    performance_id = TextField()
    track_id = TextField()
    artist_name = TextField()
    track_title = TextField()

    class Meta:
        database = db
        db_table = 'tracks'
