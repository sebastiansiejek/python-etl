from tracks.TracksEntity import TracksEntity
from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity

if __name__ == "__main__":
    TracksEntity.create_table()
    ListeningSessionsEntity.create_table()
