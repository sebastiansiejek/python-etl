from services.queries import get_the_most_popular_artist, get_the_most_popular_tracks
from timeit import default_timer as timer


def print_the_most_popular_artist():
    start = timer()
    the_most_popular_artist = get_the_most_popular_artist()
    end = timer()
    print("Artysta z największą ilością odtworzeń:\n", the_most_popular_artist.Artist, ",", the_most_popular_artist.Count)
    print(f"Time: {round(end - start, 2)}s")


def print_the_most_popular_tracks():
    start = timer()
    the_most_popular_tracks = get_the_most_popular_tracks()
    print("Najbardziej pupularne utwory:")
    for track in the_most_popular_tracks:
        print(track.track_title.replace("\n", ""), track.Count)
    end = timer()
    print(f"Time: {round(end - start, 2)}s")
