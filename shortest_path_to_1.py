'''
Solutions to the problem posed on https://medium.freecodecamp.org/demystifying-dynamic-programming-24fbdb831d3a

Problem: Given an integer n, find the minimum number of steps to reach integer 1.

At each step, you can:
     Substract 1
     Divide by 2 (if it is divisible by 2)
     Divide by 3 (if it is divisible by 3)
'''
import sys


def calculate(n):
    # return BruteForce().calculate(n)
    # return CheckAgainstBestSolutionSoFar().calculate(n)
    # return TopDown().calculate(n)
    # return BottomUp().calculate(n)
    return TopDownAlternativeAlgorithm().calculate(n)


class BruteForce(object):
    '''
        Calculates all the possible paths, and returns the length of the shortest one.

        Performance:
        ------------

        calculated n = 200 in 1.733020689s
    '''

    def calculate(self, n):
        return min(self._calculate_substep(n, 0))

    def _calculate_substep(self, n, num_steps_taken):
        if n <= 1:
            yield num_steps_taken
        else:
            if is_divisible_by(n, 3):
                yield from self._calculate_substep(n / 3, num_steps_taken + 1)
            if is_divisible_by(n, 2):
                yield from self._calculate_substep(n / 2, num_steps_taken + 1)
            yield from self._calculate_substep(n - 1, num_steps_taken + 1)


class CheckAgainstBestSolutionSoFar(object):
    '''
        Bruteforce, but remembers the best solution so far
        and stops calculating if the current solution will end up worse.

        Furthermore, does divisions by 3 before divisions by 2 and before substracting 1,
        that way we find a decent good solution as fast as possible
        (if you calculate substracting 1 first this will suddenly _not_ work well at all).

        Performance:
        ------------

        calculated n = 200 in 5.58-05s
        calculated n = 2000 in 0.00022s
        calculated n = 20000 in 0.0035s
        calculated n = 200000 in 0.025s
        calculated n = 2000000 in 0.075s
        calculated n = 20000000 in 0.89s
        calculated n = 200000000 in 8.06s
    '''

    def __init__(self):
        self.solution = sys.maxsize

    def calculate(self, n):
        self._calculate_substep(n, 0)
        assert self.solution is not sys.maxsize, "Something went wrong"
        return self.solution

    def _calculate_substep(self, n, num_steps_taken):
        if n <= 1:
            self.solution = min(self.solution, num_steps_taken)
        elif num_steps_taken + 1 >= self.solution:
            # Can never beat our solution
            return
        else:
            if is_divisible_by(n, 3):
                self._calculate_substep(n / 3, num_steps_taken + 1)
            if is_divisible_by(n, 2):
                self._calculate_substep(n / 2, num_steps_taken + 1)
            self._calculate_substep(n - 1, num_steps_taken + 1)


class TopDown(object):
    '''
        Dynamic programming, top down.
        Recursively calculates the solution, but stores previous calculated results in a lookup table.

        Performance:
        ------------

        calculated n = 200 in 0.00023s
        stack-overflow for n = 2000

    '''

    def __init__(self):
        self._lookup = {}

    def calculate(self, n):
        self._lookup[1] = 0
        return self._get_substep(n)

    def _get_substep(self, n):
        if n not in self._lookup:
            self._lookup[n] = min(self._calculate_substep(n))
        return self._lookup[n]

    def _calculate_substep(self, n):
        if is_divisible_by(n, 3):
            yield self._get_substep(n / 3) + 1
        if is_divisible_by(n, 2):
            yield self._get_substep(n / 2) + 1
        yield self._get_substep(n - 1) + 1


class BottomUp(object):
    '''
        Dynamic programming, bottom down.
        Calculates solution for 1, then for 2, and so on all the way up to n.

        Performance:
        ------------

        calculated n = 200 in 0.00018s
        calculated n = 2000 in 0.0018s
        calculated n = 20000 in 0.019s
        calculated n = 200000 in 0.18s
        calculated n = 2000000 in 1.85s

    '''

    def __init__(self):
        self._lookup = []

    def calculate(self, n):
        self._lookup = [None] * (n + 1)
        self._lookup[1] = 0

        for i in range(2, n + 1):
            self._lookup[i] = self._calculate(i)
        return self._lookup[n]

    def _calculate(self, n):
        def get_options():
            if is_divisible_by(n, 3):
                yield self._lookup[int(n / 3)] + 1
            if is_divisible_by(n, 2):
                yield self._lookup[int(n / 2)] + 1
            yield self._lookup[int(n - 1)] + 1

        return min(get_options())


class TopDownAlternativeAlgorithm(object):
    '''
        Dynamic programming, top down.

        The reason the normal top-down fails so fast is because it always ends up calculating the sequence where
        we substract by 1 all the time, i.e.
            n - 1 - 1 - 1 - .... 
        This means that for n = 1000, we have a stack depth of 1000,
        which is why Python fails (by default max stack depth is 1000).

        However, if you look at the algorithm you can see that dividing by 3 is always the best solution if it's possible
        (because that takes the biggest jump).

        So we modify the algorithm to:
            Divide by 3 if possible
            else calculate divide by 2 and minus 1

        Performance:
        ------------
        calculated n = 200 in 2.82e-05s
        calculated n = 2000 in 4.94e-05s
        calculated n = 20000 in 8.67e-05s
        calculated n = 200000 in 0.00013s
        calculated n = 2000000 in 0.00015s
        calculated n = 20000000 in 0.00021s
        calculated n = 200000000 in 0.00031s
        calculated n = 2000000000 in 0.00041s
        calculated n = 20000000000 in 0.00047s
        calculated n = 200000000000 in 0.00052s
        calculated n = 2000000000000 in 0.00065s
        calculated n = 20000000000000 in 0.00084s
        calculated n = 200000000000000 in 0.00089s
        calculated n = 2000000000000000 in 0.0011s
        stack-overflow at bigger 'n'
    '''

    def __init__(self):
        self._lookup = {}

    def calculate(self, n):
        self._lookup[1] = 0
        return self._get_substep(n)

    def _get_substep(self, n):
        if n not in self._lookup:
            self._lookup[n] = min(self._calculate_substep(n))
        return self._lookup[n]

    def _calculate_substep(self, n):
        if is_divisible_by(n, 3):
            yield self._get_substep(n / 3) + 1
        else:
            if is_divisible_by(n, 2):
                yield self._get_substep(n / 2) + 1
            yield self._get_substep(n - 1) + 1


def is_divisible_by(n, divider):
    return (n % divider) == 0
