from unittest import TestCase, mock
import datetime
from src.domain.modules.maintenance_schedule_module.schedule_manager import ScheduleManager


class ScheduleManagerTest(TestCase):

    def setUp(self):
        self.base_times = ScheduleManager(None).get_base_times()

    def test_base_times(self):
        first_day = ScheduleManager.START_TIME
        last_day = ScheduleManager.END_TIME
        interval = ScheduleManager.INTERVAL_IN_MINUTES

        schedule_first_day_and_first_time = datetime.datetime(first_day.year, first_day.month,
                                                              first_day.day, hour=ScheduleManager.OPEN_TIME.hour,
                                                              minute=0)
        schedule_first_day_and_last_time = datetime.datetime(first_day.year, first_day.month,
                                                             first_day.day, hour=ScheduleManager.CLOSE_TIME.hour,
                                                             minute=0)
        schedule_last_day_and_first_time = datetime.datetime(last_day.year, last_day.month,
                                                             last_day.day, hour=ScheduleManager.OPEN_TIME.hour,
                                                             minute=0)
        schedule_last_day_and_last_time = datetime.datetime(last_day.year, last_day.month,last_day.day,
                                                            hour=ScheduleManager.CLOSE_TIME.hour, minute=0)
        schedule_first_day_and_first_interval = datetime.datetime(first_day.year, first_day.month,
                                                                  first_day.day, hour=ScheduleManager.OPEN_TIME.hour,
                                                                  minute=interval)
        schedule_last_day_and_first_interval = datetime.datetime(last_day.year, last_day.month,
                                                                 last_day.day, hour=ScheduleManager.OPEN_TIME.hour,
                                                                 minute=interval)
        self.assertIn(schedule_first_day_and_first_time, self.base_times)
        self.assertIn(schedule_first_day_and_last_time, self.base_times)
        self.assertIn(schedule_last_day_and_first_time, self.base_times)
        self.assertIn(schedule_last_day_and_last_time, self.base_times)
        self.assertIn(schedule_first_day_and_first_interval, self.base_times)
        self.assertIn(schedule_last_day_and_first_interval, self.base_times)

    def test_available_times(self):
        schedule_repo_mock = mock.Mock()
        fake_blocked_times = [
            datetime.datetime(ScheduleManager.START_TIME.year, ScheduleManager.START_TIME.month,
                              ScheduleManager.START_TIME.day, hour=ScheduleManager.OPEN_TIME.hour,
                              minute=ScheduleManager.INTERVAL_IN_MINUTES),
            datetime.datetime(ScheduleManager.START_TIME.year, ScheduleManager.START_TIME.month,
                              ScheduleManager.START_TIME.day + 1, hour=ScheduleManager.CLOSE_TIME.hour,
                              minute=0)
        ]

        sm = ScheduleManager(schedule_repo_mock)
        schedule_repo_mock.get_blocked_times.return_value = fake_blocked_times
        schedule_repo_mock.get_blocked_times(ScheduleManager.START_TIME, ScheduleManager.END_TIME)
        available_times = sm.get_available_times()

        self.assertTrue(all(blocked_time not in available_times for blocked_time in fake_blocked_times),
                        'blocked time exists in available times list')
