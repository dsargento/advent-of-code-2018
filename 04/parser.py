import guard
import time


class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()
        self.logs = self.parse_content()
        self.guard_list = self.process_logs()

    def open_file(self):
        try:
            file_content = open(self.file_path, "r").readlines()
        except IOError:
            print("file not found")
            return 0
        return file_content

    def parse_content(self):
        file_content = []
        for log in self.file_content:
            time_date, message = log[:19], log[19:].split()
            file_content.append({
                'timestamp': time_date[1:17],
                'message': message
            })
        file_content.sort(key=lambda x: time.mktime(time.strptime(x['timestamp'], '%Y-%m-%d %H:%M')))
        return file_content

    def process_logs(self):
        guard_list = []
        for log in self.logs:
            if '#' in log:
                print("coucou")
        # guard_list = []
        # current_guard = None
        # working = False
        #
        #
        # for log in self.file_content:
        #     time_date, message = log[:19], log[19:].split()
        #     guard_id = [x[1:] for x in message if x[0] == '#']
        #     if not guard_id:
        #         print("no id")
        #     else:
        #         guard_id_single = int(guard_id[0])
        #         try:
        #             current_guard = guard_list[guard_id_single]
        #         except IndexError:
        #             guard_list.append({
        #                 'id': guard_id_single,
        #                 'guard': guard.Guard
        #             })
        #             current_guard = next(item for item in guard_list if item['id'] == guard_id_single)
        #
        return guard_list
