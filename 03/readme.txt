Part 1 explanation:

Read the file and break it down into a list of tuples that contains the id, the x and y position,
 and the x and y surface.

Then proceed to assign the ids to a 2d list, each time we overlap with another existing area, we increment our counter

Part 2 explanation:

Each time we overlap, we add the current coordinates and the overlapped coordinates to a list, comparing it with our
initial coordinates list gives us the only non overlapping surface id