from tracks.TracksEntity import TracksEntity


def add_from_list_to_tracks(row):
    TracksEntity.create(performance_id=row[0], track_id=row[1], artist_name=row[2], track_title=row[3])
