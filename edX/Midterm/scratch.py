def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat.

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    # return songs

    sorted_capacity = sorted(songs, key=lambda x: x[2], reverse = True)

    return sorted_capacity



songs_specs = songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 10
print(song_playlist(songs_specs, max_size))