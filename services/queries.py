import peewee

from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity
from tracks.TracksEntity import TracksEntity


def get_the_most_popular_artist():
    # SQL
    # SELECT
    #     tracks.artist_name AS "Artysta",
    #     COUNT(tracks.artist_name) AS "Liczba odsłuchań"
    # FROM
    #     tracks
    #     JOIN listening_sessions ON listening_sessions.track_id = tracks.track_id
    # GROUP BY
    #     tracks.artist_name
    # ORDER BY
    #     "Liczba odsłuchań" DESC
    # LIMIT 1
    query = (TracksEntity.select(TracksEntity.artist_name.alias("Artist"), peewee.fn.COUNT(TracksEntity.artist_name).alias("Count"))
             .join(ListeningSessionsEntity, on=(ListeningSessionsEntity.track_id == TracksEntity.track_id))
             .group_by(TracksEntity.artist_name)
             .order_by(peewee.fn.COUNT(TracksEntity.artist_name).desc())
             .limit(1))

    return query[0]

def get_the_most_popular_tracks():
    query = (TracksEntity.select(TracksEntity.track_title, peewee.fn.COUNT(TracksEntity.track_title).alias("Count"))
             .join(ListeningSessionsEntity, on=(ListeningSessionsEntity.track_id == TracksEntity.track_id))
             .group_by(TracksEntity.track_title)
             .order_by(peewee.fn.COUNT(TracksEntity.track_title).desc())
             .limit(5))

    return query
