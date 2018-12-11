import re


class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()
        self.x_list, self.y_list, self.x_speed, self.y_speed = self.parse_content()

    def open_file(self):
        try:
            file_content = open(self.file_path, "r").readlines()
        except IOError:
            print("file not found")
            return 0
        return file_content

    def parse_content(self):
        x_list = []
        y_list = []
        x_speed = []
        y_speed = []

        for i in self.file_content:
            ints_list = [int(d) for d in re.findall(r'-?\d+', i)]
            x_list.append(int(ints_list[0]))
            y_list.append(int(ints_list[1]))
            x_speed.append(int(ints_list[2]))
            y_speed.append(int(ints_list[3]))
        return x_list, y_list, x_speed, y_speed

    def update_list(self):
        for index, item in enumerate(self.x_list):
            self.x_list[index] += self.x_speed[index]
        for index, item in enumerate(self.y_list):
            self.y_list[index] += self.y_speed[index]
