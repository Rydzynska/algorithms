from partition import get_partitions
import time

"""
Takes a list of items from a file (pair of name (str) and weight (int))
and applies two algorithms: greedy and brute force to decide
which items to take within weight limit.
Compares time needed for each algorithm.
"""

def load_items(filename):
    """
    Read the contents of the given file.  Assume the file contents contain
    data in the form of comma-separated item name - weight pairs, and return a
    dictionary containing items names as keys and 
    corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Return a dictionary of item name (string), weight (int) pairs
    """

    items_dict = dict()

    file_handler = open(filename, 'r')
    
    for line in file_handler:
        line_data = line.split(',')
        items_dict[line_data[0]] = int(line_data[1])
    return items_dict


def greedy_algorithm(items,limit=10):
    """
    Use a greedy heuristic to determine an allocation of items that attempts 
    to minimize the number of trips needed to transport all the items.

    Parameters:
    items - a dictionary of name (string), weight (int) pairs
    limit - weight limit to carry (int)
    
    Return a list of lists, with each inner list containing the names of items
    transported on a particular trip and the overall list containing all the
    trips
    """
    items_ordered = []
    transport = []

    if not items or limit == 0:
        return []

    for name, weight in items.items():
        items_ordered.append((weight, name))
    items_ordered.sort(reverse=True)

    while items_ordered:
        trip = []
        current_limit = limit
        for item in items_ordered.copy():
            if current_limit - item[0] >= 0:
                trip.append(item[1])
                current_limit -= item[0]
                items_ordered.remove((item[0], item[1]))
        transport.append(trip)

    return transport


def brute_force_algorithm(items,limit=10):
    """
    Find the allocation of items that minimizes the number of trips
    via brute force.

    Parameters:
    items - a dictionary of name (string), weight (int) pairs
    limit - weight limit to carry (int)
    
    Return a list of lists, with each inner list containing the names of items
    transported on a particular trip and the overall list containing all the
    trips
    """
    all_items = []

    for item_name in items:
        all_items.append(item_name)

    transport = []

    for trip in (get_partitions(all_items)):
        transport.append(trip)

    shortest_transport = None
    best_transport = None

    def transport_overweighted(trips):
        for trip in trips:
             total_weight = 0
             for item in trip:
                 total_weight += items[item]
                 if total_weight > limit:
                     return True
        return False

    for trips in transport:
        if transport_overweighted(trips):
            continue
        else:
            if shortest_transport is None or len(trips) < shortest_transport:
                shortest_transport = len(trips)
                best_transport = trips

    return best_transport

       
def compare_transport_algorithms():
    """    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Return:
    Does not return anything.
    """
    items = load_items("objects_to_take.txt")
    limit=10

    start_greedy = time.time()
    greedy = greedy_algorithm(items, limit)
    end_greedy = time.time()
    print('Greedy:\nNumber of trips: {0}\nTime: {1}'.format(len(greedy), 
                                            (end_greedy - start_greedy)))

    print('')
    start_brute = time.time()
    brute = brute_force_algorithm(items, limit)
    end_brute = time.time()
    print('Brute:\nNumber of trips: {0}\nTime: {1}'.format(len(brute), 
                                            (end_brute - start_brute)))


if __name__ == '__main__':
    items = load_items("objects_to_take.txt")
    print(greedy_algorithm(items, 10))
    print(brute_force_algorithm(items, 10))
    compare_transport_algorithms()


