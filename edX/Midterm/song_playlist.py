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

def song_playlist(songs, max_size):
    """
    Selects a subset of songs to fit within the given maximum size.

    Parameters:
    songs: list of tuples, where each tuple is ('song_name', song_len, song_size)
    max_size: float, the maximum total size of songs allowed

    Returns:
    list: A subset of songs (by name) that fit in the given max_size, in the order chosen.
    """
    if not songs or songs[0][2] > max_size:
        return []  # If no songs or the first song doesn't fit, return an empty list

    # Initialize playlist with the first song
    playlist = [songs[0][0]]
    current_size = songs[0][2]

    # Remove the first song from consideration
    remaining_songs = songs[1:]

    # Sort the remaining songs by file size (ascending order)
    remaining_songs.sort(key=lambda x: x[2])

    # Add songs to the playlist based on size
    for song in remaining_songs:
        if current_size + song[2] <= max_size:
            playlist.append(song[0])
            current_size += song[2]
        else:
            break  # Stop if adding the song would exceed the maximum size

    return playlist


songs_specs = songs = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]
max_size = 11
print(song_playlist(songs_specs, max_size))

