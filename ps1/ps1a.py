#https://towardsdatascience.com/two-simple-method-to-sort-a-python-dictionary-a7907c266dba

###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators: Peter Domitrovich
# Time: 90 min

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
    a dictionary of cow names (string) and weights (int), as a key-value pair
    """
    #  Method 1
    f = open(filename)

    key = []
    value = []
    for line in f:
        key.append([line.split(',')[0]][0])
        value.append([line.split(',')[1]][0][0])

    f.close()

    # Method 2
    with open(filename) as f:
        key = []
        value = []
        for line in f:
            key.append([line.split(',')[0]][0])
            value.append([line.split(',')[1]][0][0])

    return dict(zip(key, value))



# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy algorithm to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy algorithm should follow the following method:

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
    # TODO: Your code here

    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    sorted_cows1 = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))


    trip_list = []


    while True:
        # check the entire dictionary to ensure that they are all '-1', in which case break
        # out of the while loop and return the value of trip_list
        a = True
        for i in sorted_cows1:
            if sorted_cows1[i] != str(-1):
                a = False
        # if 'a' is True (i.e., all the cows have been shipped then break out of the loop and return
        # the value of trip_list
        if a:
            break
        current_list = []
        beef = 0
        for i in sorted_cows1:
            if sorted_cows1[i] == str(-1):
                continue
            else:
                # may need to change the following depending upon what cow characteristic to output
                beef += int(sorted_cows1[i])
                if beef <= limit:
                    current_list.append(i)
                    sorted_cows1[i] = str(-1)
                elif beef > limit:
                    beef -= int(sorted_cows1[i])
                    break



        trip_list.append(current_list)

    print(sorted_cows)

    return trip_list


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

    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    print(sorted_cows)

    a = list(cows.keys())
    print(a)

    print()

    counter = 0
    for partition in get_partitions(a):
        if counter <= 100000:
            ok = True
            a = len(partition)
            b = []
            for i in partition:
                cumulative_sum = 0
                for j in i:
                    cumulative_sum += int(cows[j])
                if cumulative_sum > limit:
                    ok = False
                    break
                elif cumulative_sum <= limit:
                    b.append(i)
                    print(i, "it works correctly")
                    print(counter)
            if ok:
                print("Finished")
                print(b)
                break
        else:
            print("breaking out")
            break
        counter += 1









        
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
    # TODO: Your code here
    cows = load_cows('ps1_cow_data.txt')

    a = time.time()
    greedy_cow_transport(cows, limit=10)
    b = time.time()

    c = time.time()
    brute_force_cow_transport(cows, limit=10)
    d = time.time()

    print("Greedy Cow Transport: ", round(b-a, 6))
    print("Brute Force Cow Transport: ", round(d-c, 6))



if __name__ == "__main__":
    cows = load_cows('ps1_cow_data.txt')
    limit = 10
    print(cows)
    print(greedy_cow_transport(cows, limit))
    print(brute_force_cow_transport(cows, limit))
    # print(compare_cow_transport_algorithms())

    '''
    # 1. enumerate possible ways that the cows can be ... to help you

    
    a = [i for i in range(1, 4)]
    for partition in get_partitions(a):
        print(partition)
    

    for partition in get_partitions(cows.items()):
        print(partition)
    

    print(cows)
    print(sorted(cows.items(), key=lambda x: x[1], reverse=True))

    sorted_cows = sorted(cows.items(), key=lambda x: x[1], reverse=True)

    # incorporate limit value from parameter
    
    for partition in get_partitions(sorted_cows):
        print(partition)
    

    a = [i for i in range(1, 4)]
    for partition in get_partitions(a):
        print(partition)
    '''