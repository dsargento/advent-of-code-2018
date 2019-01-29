class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()

    def open_file(self):
        try:
            file_content = open(self.file_path, "r").readlines()
        except IOError:
            print("file not found")
            return 0
        return file_content
