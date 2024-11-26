def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat.

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """

    # sort the songs details (tuple) according to the size of the individual songs
    sorted_capacity = sorted(songs, key=lambda x: x[2], reverse = False)

    # initialize solution and total cost / value trackes
    solution = []
    total_cost = 0
    total_value = 0

    # iterate over the sorted_capacity list and select locally opitmal choices
    for element in sorted_capacity:
        if total_cost + element[2] <= max_size:
            solution.append(element[0])
            total_cost += element[2]

    # return the result
    return solution



songs_specs = songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 11
print(song_playlist(songs_specs, max_size))

