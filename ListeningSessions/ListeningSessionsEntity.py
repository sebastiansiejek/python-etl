from peewee import *

db = SqliteDatabase('database.db')


class ListeningSessionsEntity(Model):
    user_id: TextField()
    track_id: TextField()
    listening_date: DateField()

    class Meta:
        database = db
        db_table = 'listening_sessions'
