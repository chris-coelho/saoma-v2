import datetime


class ScheduleManager:
    TODAY = datetime.date.today()
    OPEN_TIME = datetime.time(8, 0)
    CLOSE_TIME = datetime.time(17, 0)
    INTERVAL_IN_MINUTES = 30
    SCHEDULE_DAYS = 2

    # starts tomorrow
    START_TIME = datetime.datetime(TODAY.year, TODAY.month, TODAY.day,
                                   hour=OPEN_TIME.hour,
                                   minute=OPEN_TIME.minute) + datetime.timedelta(days=1)
    # open schedule for SCHEDULE_DAYS next
    END_TIME = datetime.datetime(TODAY.year, TODAY.month, TODAY.day,
                                 hour=CLOSE_TIME.hour,
                                 minute=CLOSE_TIME.minute) + datetime.timedelta(days=SCHEDULE_DAYS)

    def __init__(self, schedule_repo):
        self._schedule_repo = schedule_repo

    def get_available_times(self):
        base_times = self.get_base_times()
        blocked_times = self._schedule_repo.get_blocked_times(ScheduleManager.START_TIME,
                                                              ScheduleManager.END_TIME)
        if not blocked_times:
            return base_times
        return [available_time for available_time in base_times if available_time not in blocked_times]

    def get_base_times(self):
        base_times = []
        time_schedule = ScheduleManager.START_TIME
        elapsed_days = 0
        while time_schedule <= ScheduleManager.END_TIME:
            base_times.append(time_schedule)
            time_schedule += datetime.timedelta(minutes=ScheduleManager.INTERVAL_IN_MINUTES)

            if time_schedule.time() > ScheduleManager.CLOSE_TIME:
                elapsed_days += 1
                time_schedule = ScheduleManager.START_TIME + datetime.timedelta(days=elapsed_days)
        return base_times

