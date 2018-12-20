from datetime import datetime, timedelta
from dateutil import rrule


class Guard:
    def __init__(self, guard_id):
        self.guard_id = guard_id
        self.downtime = 0
        self.uptime = 0
        self.sleep_start = ''
        self.minute_list = [0] * 60

    def update_minute_list(self, sleep_end, debug=False):
        start = datetime.strptime(self.sleep_start, '%Y-%m-%d %H:%M')
        end = datetime.strptime(sleep_end, '%Y-%m-%d %H:%M')
        end = end.replace(minute=end.minute - 1)
        tmp_list = ['..'] * 60
        for dt in rrule.rrule(rrule.MINUTELY, dtstart=start, until=end):
            tmp_list[dt.minute] = "XX"
            self.minute_list[dt.minute] += 1
            self.downtime += 1
        if debug:
            [print(x, end=' ') for x in tmp_list]
            print()

    def get_most_slept_minute(self):
        return [self.minute_list.index(max(self.minute_list)), max(self.minute_list)]
