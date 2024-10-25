import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
# adds 2 times
# input: 2 Time parameters
# output: Time object that is the sum of the two input times
def time_add(time1: data.Time, time2: data.Time) -> str:
    hours_sum = time1.hour + time2.hour
    minutes_sum = time1.minute + time2.minute
    seconds_sum = time1.second + time2.second
    if seconds_sum >= 60:
        seconds_sum = seconds_sum - 60
        minutes_sum = time1.minute + time2.minute + 1
    else:
        minutes_sum = time1.minute + time2.minute
    if minutes_sum >= 60:
        minutes_sum = minutes_sum - 60
        hours_sum = hours_sum + 1
    return "Hours: {}, Minutes: {}, Seconds: {}".format(hours_sum, minutes_sum, seconds_sum)

# Part 4
# answers true or false to "the list of float numbers is descending"
# input: a list of float numbers
# output: boolean, True if elements in list are descending
def is_descending(numbers_list: list[float]) -> bool:
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] < numbers_list[i +1]:
            return False
        else:
            return True

# Part 5
# find the index of the largest integer between a given lower and upper index
# input: a list of integers, a lower index, an upper index
# output: the index of the largest number between the lower and upper indices
def largest_between(integers_list:list[int], lower:int, upper:int):
    largest_between_idx = 0
    if lower > upper:
        return "Invalid input. Lower index must be less than upper index."
    else:
        for i in range(upper - lower):
            if integers_list[lower] < integers_list[lower + i + 1]:
                largest_between_idx = lower + i + 1
            else:
                largest_between_idx = lower
        return largest_between_idx

# Part 6
# find the point furthest from the origin given a list of points
# input: a list of Points
# output: the index of the point furthest from the origin
def furthest_from_origin(list_of_points: list[data.Point]) -> int:
    distance_from_origin = []
    furthest_from_origin_idx = 0
    for i in range(len(list_of_points)):
        distance_from_origin.append((list_of_points[i].x**2 + list_of_points[i].y**2)**(1/2))
    for j in range(len(list_of_points) - 1):
        if distance_from_origin[j] < distance_from_origin[j + 1]:
            furthest_from_origin_idx = j + 1
        else:
            furthest_from_origin_idx = j
    return furthest_from_origin_idx
