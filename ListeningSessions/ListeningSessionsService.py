from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity


def add_from_list_to_listening_sessions(row):
    ListeningSessionsEntity.create(user_id=row[0], track_id=row[1], listening_date=row[2])