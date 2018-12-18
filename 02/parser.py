import re


class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()
        self.lines = self.parse_content()

    def open_file(self):
        try:
            file_content = open(self.file_path, "r").readlines()
        except IOError:
            print("file not found")
            return 0
        return file_content

    def parse_content(self):
        lines = []

        for i in self.file_content:
            lines.append(i)
        return lines
