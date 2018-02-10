import datetime
from unittest import TestCase

from src.infra.crosscutting.common.date_time_util import DateTimeUtil


class DateTimeUtilTest(TestCase):

    def test_add_a_month(self):
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 2, 10), 1), datetime.date(2018, 3, 10))

    def test_add_13_months(self):
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 2, 10), 13), datetime.date(2019, 3, 10))

    def test_add_a_months_ago(self):
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 2, 10), -1), datetime.date(2018, 1, 10))

    def test_add_last_day_of_a_month(self):
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 1, 31), 1), datetime.date(2018, 2, 28))
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 3, 31), 1), datetime.date(2018, 4, 30))
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 7, 31), 1), datetime.date(2018, 8, 31))
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 9, 30), 1), datetime.date(2018, 10, 30))
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2018, 9, 30), 1), datetime.date(2018, 10, 30))

    def test_add_leap_year_month(self):
        self.assertEqual(DateTimeUtil.add_months(datetime.date(2020, 1, 31), 1), datetime.date(2020, 2, 29))

