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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
