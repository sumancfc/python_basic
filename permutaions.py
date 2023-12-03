'''
According to Wolfram MathWorld:
A permutation, also called an "arrangement number" or "order," is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.

For example, there are six permutations of ABC: ABC, ACB, BAC, BCA, CAB, and CBA.

If a set has N elements, then the number of permutations of them is N! (N factorial).

For the ABC string, the permutations are 3! = 3 * 2 * 1 = 6. Let's see this in Python:
'''

from itertools import permutations

print(list(permutations('ABC')))
print(tuple(permutations('ABC')))