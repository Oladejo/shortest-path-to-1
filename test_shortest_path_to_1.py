import timeit
import unittest

import shortest_path_to_1


class TestShortestPathTo1(unittest.TestCase):

    def _test_print_solutions(self):
        for n in range(1, 200):
            print("        {}: {},".format(n, shortest_path_to_1.calculate(n)))

        self.assertEqual(True, False)

    def test_algorithm_works(self):
        for n in range(1, 150):
            expected_steps = solutions[n]
            actual_steps = shortest_path_to_1.calculate(n)
            self.assertEqual(
                expected_steps, actual_steps,
                "For n = {} expected {} got {}".format(n, expected_steps, actual_steps)
            )

    def test_timeit(self):
        ''' Times 200, 2000, 20000, ... until one takes more than 1 second '''
        n = 200

        while True:
            time = timeit.timeit(lambda: shortest_path_to_1.calculate(n), number=1)
            print("calculated n = {} in {}s".format(n, time))

            if time > 1:
                return

            if n > 1000000000000000:
                break

            n = n * 10


# n, steps pairs
solutions = {
    1: 0,
    2: 1,
    3: 1,
    4: 2,
    5: 3,
    6: 2,
    7: 3,
    8: 3,
    9: 2,
    10: 3,
    11: 4,
    12: 3,
    13: 4,
    14: 4,
    15: 4,
    16: 4,
    17: 5,
    18: 3,
    19: 4,
    20: 4,
    21: 4,
    22: 5,
    23: 6,
    24: 4,
    25: 5,
    26: 5,
    27: 3,
    28: 4,
    29: 5,
    30: 4,
    31: 5,
    32: 5,
    33: 5,
    34: 6,
    35: 7,
    36: 4,
    37: 5,
    38: 5,
    39: 5,
    40: 5,
    41: 6,
    42: 5,
    43: 6,
    44: 6,
    45: 5,
    46: 6,
    47: 7,
    48: 5,
    49: 6,
    50: 6,
    51: 6,
    52: 6,
    53: 7,
    54: 4,
    55: 5,
    56: 5,
    57: 5,
    58: 6,
    59: 7,
    60: 5,
    61: 6,
    62: 6,
    63: 5,
    64: 6,
    65: 7,
    66: 6,
    67: 7,
    68: 7,
    69: 7,
    70: 8,
    71: 9,
    72: 5,
    73: 6,
    74: 6,
    75: 6,
    76: 6,
    77: 7,
    78: 6,
    79: 7,
    80: 6,
    81: 4,
    82: 5,
    83: 6,
    84: 5,
    85: 6,
    86: 7,
    87: 6,
    88: 7,
    89: 8,
    90: 5,
    91: 6,
    92: 7,
    93: 6,
    94: 7,
    95: 8,
    96: 6,
    97: 7,
    98: 7,
    99: 6,
    100: 7,
    101: 8,
    102: 7,
    103: 8,
    104: 7,
    105: 8,
    106: 8,
    107: 9,
    108: 5,
    109: 6,
    110: 6,
    111: 6,
    112: 6,
    113: 7,
    114: 6,
    115: 7,
    116: 7,
    117: 6,
    118: 7,
    119: 8,
    120: 6,
    121: 7,
    122: 7,
    123: 7,
    124: 7,
    125: 8,
    126: 6,
    127: 7,
    128: 7,
    129: 7,
    130: 8,
    131: 9,
    132: 7,
    133: 8,
    134: 8,
    135: 6,
    136: 7,
    137: 8,
    138: 7,
    139: 8,
    140: 9,
    141: 8,
    142: 9,
    143: 10,
    144: 6,
    145: 7,
    146: 7,
    147: 7,
    148: 7,
    149: 8,
    150: 7,
}
