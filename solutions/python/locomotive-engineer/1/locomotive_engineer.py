"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
        
    Implement a function fix_list_of_wagons() that takes two lists containing wagon IDs.
    It should reposition the first two items of the first list to the end, and insert the values from the second list behind (on the right hand side of) the locomotive ID (1).
    The function should then return a list with the modifications.

    >>> fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
    [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
    """
    first, second, locomotive, *remaining = each_wagons_id
    return [locomotive, *missing_wagons, *remaining, first, second]
    


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
#     add_missing_stops({"from": "New York", "to": "Miami"},
#                       stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
#                       stop_4="Jacksonville", stop_5="Orlando")

# {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}
    stops = list(kwargs.values())
    route["stops"] = stops
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    # for k, v in more_route_information.items():
    #     route[k] = v

    # return route
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return [list(column) for column in zip(*wagons_rows)]
    first, second, third = wagons_rows
    new_f = [first[0], second[0], third[0]]
    new_s = [first[1], second[1], third[1]]
    new_t = [first[2], second[2], third[2]]

    return [new_f, new_s, new_t]

