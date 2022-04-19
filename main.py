from timeit import default_timer as timer
from ListeningSessions.ListeningSessionsService import add_from_list_to_listening_sessions
from tracks.TracksEntity import TracksEntity
from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity
from services.PrepareTxtFileToDatabase import PrepareTxtFileToDatabase
from tracks.TracksService import add_from_list_to_tracks
from views.views import print_the_most_popular_artist, print_the_most_popular_tracks

if __name__ == "__main__":
    TracksEntity.create_table()
    ListeningSessionsEntity.create_table()

    TRACKS_PATH = "data/unique_tracks.txt"
    LISTENING_SESSIONS_PATH = "data/triplets_sample_20p.txt"

    if len(TracksEntity.select()) == 0:
        start = timer()
        PrepareTxtFileToDatabase(TRACKS_PATH).prepare(callback=add_from_list_to_tracks)
        end = timer()
        print(f"Import tracks: {round(end - start, 2)}s")

    if len(ListeningSessionsEntity.select()) == 0:
        start = timer()
        PrepareTxtFileToDatabase(LISTENING_SESSIONS_PATH).prepare(callback=add_from_list_to_listening_sessions)
        end = timer()
        print(f"Import listening sessions: {round(end - start, 2)}s")

    print_the_most_popular_artist()
    print("\n")
    print_the_most_popular_tracks()

