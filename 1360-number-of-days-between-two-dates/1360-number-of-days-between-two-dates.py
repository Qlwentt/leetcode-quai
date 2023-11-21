import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        year1, mo1, day1 = date1.split("-")
        year2, mo2, day2 = date2.split("-")
        
        
        day1 = int(day1)
        day2 = int(day2)
        
        mo1 = self.getDaysFromMo(mo1,year1)
        mo2 = self.getDaysFromMo(mo2,year2)
        
        years = {1970: self.yearDays(1970)}
        for i in range(1971,2101):
            years[i] = years[i-1] + self.yearDays(i)
        
        year1 = years[int(year1)-1]
        year2 = years[int(year2)-1]
        
        return  abs((day1 + mo1 + year1) - (day2 + mo2 + year2))
        
    def getDaysFromMo(self, mo, year):
        months = {
            "0": 31,
            "1": 31,
            "2": 28,
            "3": 31,
            "4": 30,
            "5": 31,
            "6": 30,
            "7": 31,
            "8": 31,
            "9": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }
        days = 0
        for i in range(1,int(mo)):
            days += months[str(i)]
        if self.yearDays(int(year)) == 366 and int(mo) > 2:
            days += 1
        return days        
        
    def yearDays(self,year):
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                return 365
            return 366
        else:
            return 365
            
        
        