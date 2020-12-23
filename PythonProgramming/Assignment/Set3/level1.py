#lex_auth_012693797166096384149

def find_leap_years(given_year):

    l =[]
    for i in range(1,16):
        while True :
            if (given_year %4 ==0 and given_year % 100 !=0) or given_year % 400 ==0 :
                l.append(given_year)
                given_year +=1
                break
            else :
                given_year += 1
    
#    ((year % 4 == 0) && (year % 100!= 0)) || (year%400 == 0)

    return l

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
