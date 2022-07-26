def is_year_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    return leap

def days_in_month(year, month):
    day=[31,28,31,30,31,30,31,31,30,31,30,31]
    months=[1,2,3,4,5,6,7,8,9,10,11,12]
    if is_year_leap(year) == True :
        if month == 2 :
            return 29
        else :
            return day[month-1]
    elif month in months : 
        return day[month-1]
    else :
        return None
def day_of_year(year, month, day):
    days = 0
    if month <=12 and day <= 31 :
        for i in range(1,month):
            days += days_in_month(year,i)
        print("Total days in Year ",year," Month ",month," Day ",day," is ")
        return days + day
    else :
        return None
print(day_of_year(2001, 11, 31))
