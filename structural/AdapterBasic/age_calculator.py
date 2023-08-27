class AgeCalculator:
    def __init__(self, birthday):
        self.day, self.month, self.year = (
            int(x) for x in birthday.split('-'))

    def calculate_age(self, date):
        day, month, year = (
            int(x) for x in date.split('-'))
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


if __name__ == "__main__":
    calc = AgeCalculator("30-03-2000")
    print(calc.calculate_age("08-27-2023"))
