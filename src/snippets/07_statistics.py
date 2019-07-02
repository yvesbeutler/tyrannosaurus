from collections import Counter
from typing import List
import random
import matplotlib.pyplot as plt

def mean(xs: List[float]) -> float:
    """returns the mean of a list"""
    return sum(xs) / len(xs)

# the underscore indicates that this is a private function
# and should not be called directly
def _median_odd(xs: List[float]) -> float:
    """returns the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """returns the mean of the two middle elements"""
    sorted_xs = sorted(xs)
    upper_middle = len(xs) // 2
    return (sorted_xs[upper_middle - 1] + sorted_xs[upper_middle]) / 2

def median(xs: List[float]) -> float:
    """returns the median of a given list"""
    return _median_even(xs) if len(xs) % 2 == 0 else _median_odd(xs)

# run some checks
assert median([1,10,2,9,5]) == 5
assert median([1,9,2,10]) == (2 + 9) / 2

# generate some random values
num_friends = [random.randrange(0, 30, 1) for _x in range(100)]

friend_counts = Counter(num_friends)
xs = range(31)                         # largest value is 30
ys = [friend_counts[x] for x in xs]    # height is just # of friends
plt.bar(xs, ys)
plt.axis([0, 31, 0, max(ys)+2])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")

# print some statistics first
print(f"The average number of friends is {int(mean(num_friends))}")
print(f"The median number of friends is {int(median(num_friends))}")

plt.show()
