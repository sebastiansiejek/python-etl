from ListeningSessions.ListeningSessionsService import add_from_list_to_listening_sessions
from tracks.TracksEntity import TracksEntity
from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity
from services.PrepareTxtFileToDatabase import PrepareTxtFileToDatabase
from tracks.TracksService import add_from_list_to_tracks

if __name__ == "__main__":
    TracksEntity.create_table()
    ListeningSessionsEntity.create_table()

    PrepareTxtFileToDatabase("data/unique_tracks.txt").prepare(callback=add_from_list_to_tracks)
    PrepareTxtFileToDatabase("data/triplets_sample_20p.txt").prepare(callback=add_from_list_to_listening_sessions)
