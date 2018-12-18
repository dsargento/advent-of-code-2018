Part 1 explanation:

Check if each line contains 3 or/and 2 of the same letter, increment counters each time it happens, then multiply them

Part 2 explanation:

We iterate through all lines then compare them against every other line though a clusterfuck of for loops,
we compare the amount of letters in common, if that amount is the same as the length of the string minus one, then we
have found our box id, we remove the differing letter from both strings to get the answer
