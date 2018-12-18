import parser
import pprint

my_parser = parser.Parser('./input.txt')

my_array = []
invalid_list = []
for i in range(my_parser.max_y + 1):
    my_array.append(['.'] * (my_parser.max_x + 1))
pp = pprint.PrettyPrinter(indent=4)

for coordinate in my_parser.coordinates:

    # Axe Y
    for y in range(coordinate[2], coordinate[2] + coordinate[4]):
        # Axe X
        for x in range(coordinate[1], coordinate[3] + coordinate[1]):
            # On invalide l'id de la surface qui se trouvait la avant, et celle qui la recouvre
            if my_array[x][y] != '.':
                if my_array[x][y] != 'x':
                    invalid_list.append(my_parser.coordinates[my_array[x][y] - 1])
                    my_array[x][y] = 'x'
                invalid_list.append(coordinate)
            else:
                my_array[x][y] = coordinate[0]

print("Total overlapping surface:", sum(row.count('x') for row in my_array))
print("Non-overlapping surface ID: ", [x for x in my_parser.coordinates if x not in set(invalid_list)][0][0])
