#!/usr/bin/python3

import calendar

class LeapYear:

    @staticmethod
    def is_leap_year(year):
        return calendar.isleap(year)

print(LeapYear.is_leap_year(2000))