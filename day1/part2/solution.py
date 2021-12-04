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


def find_window_sum(int_a, int_b, int_c):
    window_sum = int_a + int_b + int_c
    return window_sum

# WHAT I NEED THIS TO DO
# Take the sum of the first three numbers. Take the sum of the next three numbers.
# Compare the two. If the second three is greater than the first three, mark it as an increase.
# Forget the first three. Now take the sum of the third three. Compare it with the second three.
# If the third three is greater than the second three, mark it as an increase. Lather, rinse, repeat.
# Return how many times it increases.
# ===OR===
# take the sum of the first three. Plop it into a new list. Take the sum of the next three. Plop it into a list.
# Then run the new list through the count increases.
def idk_what_to_call_this_yet(list_of_sea_depths):
    for depth in range(0, len(list_of_sea_depths)):
        list_of_sea_depths[depth] + list_of_sea_depths[depth + 1] + list_of_sea_depths[depth + 2]



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