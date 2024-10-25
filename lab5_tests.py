import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
        def test_time_add_1(self):
        time1 = data.Time(7, 20, 1)
        time2 = data.Time(4, 19, 45)
        expected = "Hours: 11, Minutes: 39, Seconds: 46"
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)

    def test_time_add_2(self):
        time1 = data.Time(7, 20, 1)
        time2 = data.Time(4, 41, 59)
        expected = "Hours: 12, Minutes: 2, Seconds: 0"
        actual = lab5.time_add(time1, time2)
        self.assertEqual(expected, actual)


    # Part 4
    def test_is_descending_1(self):
        numbers_list = [3.3, 2.2, 1.1]
        expected = True
        actual = lab5.is_descending(numbers_list)
        self.assertEqual(expected, actual)

    def test_is_descending_2(self):
        numbers_list = [-3.3, 2.2, 1.1]
        expected = False
        actual = lab5.is_descending(numbers_list)
        self.assertEqual(expected, actual)


    # Part 5
    def test_largest_between_1(self):
        integers_list = [1, 2, 3, 4, 5]
        lower = 1
        upper = 3
        expected = 3
        actual = lab5.largest_between(integers_list, lower, upper)
        self.assertEqual(expected, actual)

    def test_largest_between_2(self):
        integers_list = [1, 2, 3, 4, 5]
        lower = 3
        upper = 1
        expected = "Invalid input. Lower index must be less than upper index."
        actual = lab5.largest_between(integers_list, lower, upper)
        self.assertEqual(expected, actual)


    # Part 6
    def test_furthest_from_origin_1(self):
        list_of_points = [data.Point(1,2), data.Point(5,6), data.Point(3,4)]
        expected = 1
        actual = lab5.furthest_from_origin(list_of_points)
        self.assertEqual(expected, actual)

    def test_furthest_from_origin_2(self):
        list_of_points = [data.Point(1,2), data.Point(3,4), data.Point(5,-6)]
        expected = 2
        actual = lab5.furthest_from_origin(list_of_points)
        self.assertEqual(expected, actual)





if __name__ == '__main__':
    unittest.main()
