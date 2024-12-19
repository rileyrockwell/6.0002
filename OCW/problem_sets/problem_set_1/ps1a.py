###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    with open(filename, 'r') as file:
        for line in file:
            name, weight = line.strip().split(',')
            cows[name] = int(weight)
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    sorted_cows = sorted(cows.items(), key=lambda item: item[1], reverse=True)

    # list to hold all trips
    trips = []
    # will be modifying remaining cows
    remaining_cows = sorted_cows[:]


    while remaining_cows:
        trip = []
        total_weight = 0

        # try to add cows to the current trip
        for cow, weight in remaining_cows[:]:
            if total_weight + weight <= limit:
                trip.append(cow)
                total_weight += weight
                remaining_cows.remove((cow, weight))

        trips.append(trip)

    return trips
    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    best_partition = None

    # iterate over all partitions of the cow list
    for partition in get_partitions(cows.keys()):
        valid_partition = True

        # ensure each trip in the current partition meets the weight limit
        for trip in partition:
            total_weight = sum(cows[cow] for cow in trip)
            if total_weight > limit:
                valid_partition = False
                break

        if valid_partition:
            if best_partition is None or len(partition) < len(best_partition):
                best_partition = partition

    return best_partition



        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows(filename)
    
    a = time.time()
    greedy_cow_transport(cows, limit = 10)
    b = time.time()

    c = time.time()
    brute_force_cow_transport(cows)
    d = time.time()

    print('Greedy:', round(b - a, 10))
    print('Brute:', round(c - d, 10))

    return ''



if __name__ == "__main__":    
    filename = '/workspaces/6.0002/OCW/problem_sets/problem_set_1/ps1_cow_data.txt'
    cows = load_cows(filename)

    print(compare_cow_transport_algorithms())