#!/usr/bin/python3

class LeapYear:

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(LeapYear.is_leap_year(2000))