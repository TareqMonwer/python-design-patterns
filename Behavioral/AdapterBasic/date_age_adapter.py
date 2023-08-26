import datetime

from Behavioral.AdapterBasic.age_calculator import AgeCalculator


class DateAgeAdapter:

    @staticmethod
    def _str_date(date: datetime.date):
        return date.strftime("%Y-%m-%d")

    def __init__(self, birdthday):
        birdthday = self._str_date(birdthday)
        self.calculator = AgeCalculator(birdthday)

    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)
