Part 1 explanation:

Pretty straightforward, the input file is parsed into a list of ints, then we apply the values using a for loop to get
the answer

Part 2 explanation:

We have to find the first repetition, to do that we repeat the sequence until the values matches one stored in the
history (it takes a while)

Part 2 update:

Replaced the history dict by a set, since sets lookups are much faster, and we dont need to use key/value pairs