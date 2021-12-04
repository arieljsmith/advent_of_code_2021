# =============================================================================
# F U N C T I O N S
# =============================================================================

def create_depth_list(file_of_sea_depths):
    """
    Function that takes a file of numbers and creates a list with each number
    as its own element.

    :param file_of_sea_depths: file - file containing numbers we want to make a list of
    :return new_list_of_sea_depths: list - list of sea depths
    """

    list_of_sea_depths = file_of_sea_depths.readlines()
    new_list_of_sea_depths = []
    for depth_entry in list_of_sea_depths:
        if depth_entry != list_of_sea_depths[-1]:
            new_list_of_sea_depths.append(depth_entry[:-1])
        new_list_of_sea_depths.append(depth_entry)

    return new_list_of_sea_depths


def count_increases(list_of_sea_depths):
    """
    Function that takes a list of depths and tracks (and reeturns) the number of times the
    depth increased from one element to the next.

    :param list_of_sea_depths: list - list of depths
    :return increase_count: int - the total number of times the depth increased
    """
    increase_count = 0
    current_depth = int(list_of_sea_depths[0])

    for depth in list_of_sea_depths:
        if int(depth) != 155:
            if int(depth) > current_depth:
                increase_count += 1
            current_depth = int(depth)
    return increase_count


# =============================================================================
# W H E R E  S H I R T  H A P P E N S
# =============================================================================

with open("input.txt", "r") as file_of_sea_depths:
    list_of_sea_depths = create_depth_list(file_of_sea_depths)
    count_increases(list_of_sea_depths)
