import requests
import MySQLdb


# Retrieve stop list in order from MySQL database:
def get_stop_list(route, direction):
    """Pass in route and direction, and the function will return the list of stops in that route, in order, from start to end stop."""
    # Open connection to database and execute query
    db = MySQLdb.connect(user='lucas', db='summerProdb', passwd='hello_world', host='csi6220-3-vm3.ucd.ie')
    cursor = db.cursor()
    cursor.execute('SELECT stop_id FROM ' + direction + '_' + route)
    rows = cursor.fetchall()

    # Close connection
    db.close()

    # Create and populate a list with all the bus stop ids retrieved from the database
    stop_list = []
    for i in rows:
        stop_list.append(i[0])
    return stop_list

# Retrieve Route Information from the API, was replaced by def get_stop_list which queries from the database. Left it here in case we need to go back to it.
# def get_stop_ids(stop_id, route_id):
#     '''Takes in the route and returns all the bus stop ids for that route, in a list.'''
#     base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/routeinformation?routeid='+ route_id + '&operator=bac&format=json'
#     response = requests.get(base_url)
#     results = response.json()
#
#     # Populate the list to with the stop ids of that route
#     for k in range(0, 2):
#         found = False
#         # Create empty list to hold the stop ids
#         stop_ids = []
#         for i in results['results'][k]['stops']:
#             stop_ids.append({'stopid':i['stopid'], 'latitude':i['latitude'], 'longitude':i['longitude'], 'fullname':i['fullname']})
#             if stop_id == i['stopid']:
#                 found = True
#         if found:
#             return stop_ids
#     return stop_ids


# Retrieve real time data for the next 3 inbound buses
def get_due_time(stop_id, route_id):
    """Receives stop id of SRC stop and the route id and returns the first 3 inbound buses at that stop for that route in a list."""
    # REquest data from Dublin Bus API
    base_url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=' + stop_id + '&routeid=' + route_id + '&maxresults&operator&format=json'
    response = requests.get(base_url)
    results = response.json()

    # Create a counter to filter only the next 3 inbound buses
    counter = 0

    # Empty list to put the buses in
    first_3_buses = []

    # Populate the list with the next 3 inbound buses
    for i in results['results']:
        if counter == 3:
            # Stop populating list
            break
        # Append bus to list
        first_3_buses.append({'duetime':i['duetime'], 'scheduledarrivaldatetime':i['scheduledarrivaldatetime'], 'arrivaldatetime':i['arrivaldatetime'],
                              'direction':i['direction'], 'origin':i['origin'], 'destination':i['destination']})
        counter += 1

    # Returns the next 3 buses in a list
    return first_3_buses


# Receives the 3 bus list, and filters it to just the first one. Useful various functions.
def filter_buses(list_of_buses):
    """Receives bus list and returns only the first bus on that list."""
    for bus in list_of_buses:
        return bus


# This function finds where a bus is. It uses a binary search algorithm to allow for more efficiency (less API calls). It needs a low bound,
# a high bound and a pointer that moves between them.
def get_closest_bus_stop(due_time, stop_src, stop_ids, route_id):
    """Receives the due time of that bus at the stop, the stop id of source stop, the list of stop of ids on the route and the route id. It retuns an integer (called pointer)
    that is the index position in the stop_ids list. This tells us what stop the bus is at."""

    # Get index of where the SRC stop is in the tupple to serve as the high-bound, and store that position in original. Also, store the original due time, as it will be needed
    high_bound = 0
    original = 0
    original_due_time = due_time
    for i in range(0, len(stop_ids)):
        if str(stop_ids[i]) == stop_src:
            high_bound = i
            original = i
            break

    # Innitialize pointer to be halfway between the lowbound (set to 0 index) and the highbound (the SRC stop).
    pointer = original//2
    low_bound = 0

    # Optimally we want to find the stop where our bus is just 1 minute away, for better accuracy. But sometimes that is not possible, so we will
    # need to look for a bus further away. This variable, arrival_within_minutes, starts with 1 minutes, and will be increased as necessary.
    arrival_within_minutes = 1

    # Search until we find where the bus is
    while True:
        last_due_time = 0
        # Search while our due time is not 'Due' or within the specified minutes
        while due_time != 'Due' or int(due_time) > arrival_within_minutes:
            # Once more, get the buses for the stop we are currently looking at
            first_3_buses = get_due_time(str(stop_ids[pointer]), route_id)

            # Get just the first bus, since we already have the 3 buses from our SRC stop (this one is just looking for where one of those 3 buses is)
            possible_stop = filter_buses(first_3_buses)

            # Store the new due time, from the bus stop our binary algorithm selected
            new_due_time_due = possible_stop['duetime']

            # If the new due_time is the same as the last_due_time it means the algorithm got stuck without finding a better value, and we need to break, and change our
            # arrival_within_minutes for a longer time
            if new_due_time_due == last_due_time:
                break

            # If we found a 'Due' or within the arrival_within_minutes, return that index. That is the index of the stop where our bus is at/close to.
            if possible_stop['duetime'] == 'Due' or int(possible_stop['duetime']) <= arrival_within_minutes:
                print('Found the bus with', due_time, 'due time')
                return pointer
            else:
                # If the due time at the possible stop is less than the one at SRC, we're on the right path, and need to look for a stop farther from the SRC
                if int(possible_stop['duetime']) < int(due_time):
                    # Store the new, better due time
                    due_time = possible_stop['duetime']
                    # Change the highbound to the pointer and reduce our pointer again to halfway between lowbound and highbound
                    high_bound = pointer
                    pointer -= ((high_bound - low_bound)//2)
                else:
                    # If the due time at the possible stop is bigger than the one at SRC, we've gone too far, and need to look for a stop closer to the SRC
                    # The lowbound becomes the pointer and we move the pointer, again, to halfway between the lowbound and the highbound
                    low_bound = pointer
                    pointer += ((high_bound - low_bound)//2)
            # If we found a better (shortter) due time, we store this one for the next iteration and keep looking for an even better one
            last_due_time = new_due_time_due

        # If the algorithm comes to this part, it means we didn't find a stop where our bus was due wihin 1 (or more) minutes. So we need to increase the
        # arrival_within minutes to keep searching.
        arrival_within_minutes += 1

        # Reset our lowbound, highbound and pointer to restart the search
        low_bound = 0
        high_bound = original
        pointer = original // 2

        # If we start looking for a stop, previous to the SRC, were our bus has MORE duetime, we've gonne too far. Possibly, there are two buses running very close to one another,
        # and they may be due to our SRC stop at the same time (seen before too many times with the 17). In this case, we need to increase the original bound to take the stop where
        # we found the previous bus.
        if arrival_within_minutes > int(original_due_time):
            high_bound += 1
            return high_bound

    # Just a token return
    return 0

# Everything runs from this function. It does not require any input.
def main():
    # In the future, the data for these two variables will have to come from the website
    at_stop_id = '768'
    bus_route = '46A'

    # Get direction: inbound or outbound
    direction = (get_due_time(at_stop_id, bus_route)[0]['direction']).lower()

    # Get stop list for the specified route in the inbound/outbound direction
    stop_ids = get_stop_list(bus_route, direction)

    # Get due times for first 3 buses at chosen origin, for specified route
    first_3_buses = get_due_time(at_stop_id, bus_route)

    # Find where the buses are
    for i in first_3_buses:
        # If the bus is due at the SRC stop, no need to look for it
        print('Original due time is', i['duetime'])
        if i['duetime'] == 'Due' or int(i['duetime']) <= 2:
            print('The bus it at', at_stop_id)
            continue

        # But if its not, we will need to go into the bus finder algorithm
        pointer = get_closest_bus_stop(i['duetime'], at_stop_id, stop_ids, bus_route)
        print('The bus is at', stop_ids[pointer])

        # Next we reduce the pointer (our index) by one, so we don't risk getting the same bus again (except detailed exception as explained previously)
        at_stop_id = str(stop_ids[pointer - 1])

if __name__ == '__main__':
    main()
