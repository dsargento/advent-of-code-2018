import guard
import time


class Parser:
    def __init__(self, path):
        self.file_path = path
        self.file_content = self.open_file()
        self.logs = self.parse_content()
        self.guard_dict = self.process_logs()

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
        guard_dict = {}
        current_guard = None
        [print(str(x).zfill(2), end=' ') for x in range(0, 60)]
        print()
        for log in self.logs:
            if log['message'][0] == 'Guard':
                guard_id = log['message'][1][1:]
                try:
                    current_guard = guard_dict[guard_id]
                except KeyError:
                    guard_dict[guard_id] = guard.Guard(guard_id)
                    current_guard = guard_dict[guard_id]
            elif log['message'][0] == 'falls':
                current_guard.sleep_start = log['timestamp']
            elif log['message'][0] == 'wakes':
                current_guard.update_minute_list(log['timestamp'])
                if current_guard is not None and current_guard.guard_id == '239':
                    current_guard.update_minute_list(log['timestamp'], True)
        print()
        [print(str(x).zfill(2), end=' ') for x in guard_dict['239'].minute_list]
        print()
        return guard_dict
