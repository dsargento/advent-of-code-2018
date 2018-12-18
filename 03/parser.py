import re


class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()
        self.max_x = 0
        self.max_y = 0
        self.coordinates = self.parse_content()

    def open_file(self):
        try:
            file_content = open(self.file_path, "r").readlines()
        except IOError:
            print("file not found")
            return 0
        return file_content

    def parse_content(self):
        coordinates = []
        for i in self.file_content:
            coordinate_id = int(re.search('#(.+?)@', i).group(1))
            coordinate_x, coordinate_y = [int(x) for x in re.search('@(.+?):', i).group(1).split(',')]
            area_size_x, area_size_y = [int(x) for x in i.split(':', 1)[1].split('x')]
            coordinates.append((coordinate_id, coordinate_x, coordinate_y, area_size_x, area_size_y))
            if coordinate_x + area_size_x > self.max_x:
                self.max_x = coordinate_x + area_size_x
            if coordinate_y + area_size_y > self.max_y:
                self.max_y = coordinate_y + area_size_y
        self.max_x += 1
        self.max_y += 1
        return coordinates
