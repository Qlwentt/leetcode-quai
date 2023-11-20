import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year1,mo1,day1 = date1.split("-")
        year2,mo2,day2 = date2.split("-")
        
        return (abs(date(int(year1), int(mo1), int(day1))-date(int(year2), int(mo2), int(day2)))).days