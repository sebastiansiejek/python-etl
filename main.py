from timeit import default_timer as timer
from ListeningSessions.ListeningSessionsService import add_from_list_to_listening_sessions
from services.queries import get_the_most_popular_artist
from tracks.TracksEntity import TracksEntity
from ListeningSessions.ListeningSessionsEntity import ListeningSessionsEntity
from services.PrepareTxtFileToDatabase import PrepareTxtFileToDatabase
from tracks.TracksService import add_from_list_to_tracks

if __name__ == "__main__":
    TracksEntity.create_table()
    ListeningSessionsEntity.create_table()

    if len(TracksEntity.select()) == 0:
        start = timer()
        PrepareTxtFileToDatabase("data/unique_tracks.txt").prepare(callback=add_from_list_to_tracks)
        end = timer()
        print(f"Import tracks: {round(end - start, 2)}s")

    if len(ListeningSessionsEntity.select()) == 0:
        start = timer()
        PrepareTxtFileToDatabase("data/triplets_sample_20p.txt").prepare(callback=add_from_list_to_listening_sessions)
        end = timer()
        print(f"Import listening sessions: {round(end - start, 2)}s")

    the_most_popular_artist = get_the_most_popular_artist()
    print("Artysta z największą ilością odtworzeń\n", the_most_popular_artist.Artist, " ", the_most_popular_artist.Count)
