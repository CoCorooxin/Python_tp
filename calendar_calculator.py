def is_leap_year(year):
    if year%4 == 0 and year != 0:
        return True
    else:
        return False

def days_in_year_julian(leap):
    if is_leap_year(leap):
        return 366
    else:
        return 365

def days_in_month(mois, bo):
    if mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return 30
    elif mois == 2:
        if bo is True:
            return 29
        else:
            return 28
    else:
        return 31

def julian_to_counter(year, month, day):
    n = 0
    for i in range(year-1):
        n += days_in_year_julian(i)
    for m in range(month-1):
        n += days_in_month(m, is_leap_year(year))
    n += day
    return n - 2

print(julian_to_counter(2,1,1))

def som_4_year(som):
    s = 0
    for i in range(0,som,4):
        s += days_in_year_julian(i)
    return s
    
def julian_to_counter_clever(year, month, day):
    n = 0
    if year%4 == 1:
        n += som_4_year(year-1)
    else:
        n = n + som_4_year(year-1) + (year%4)*365
        
    for m in range(month-1):
        n += days_in_month(m, is_leap_year(year))
    n += day
    return n - 2




def is_leapyear_gregorian(year):
    if year%100 == 0 and (year//100)%4 != 0:
        return False
    elif year%4 == 0 and year != 0:
        return True
    else:
        return False
    
def days_in_year_gregorian(year):
    if is_leapyear_gregorian(year):
        return 366
    else:
        return 365

def gregorian_to_counter(year, month, day):
    n = 0
    for i in range(year-1):
        n += days_in_year_gregorian(i)
    for m in range(month-1):
        n += days_in_month(m, is_leapyear_gregorian(year))
    n += day
    return n

def weekday_of_gregorian(year, month, day):
    weekday = gregorian_to_counter(year, month, day)%7
    return weekday













