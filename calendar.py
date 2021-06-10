
import calendar
def check_valid_date(d,m,y,l):
    if l:
        if m==2:
            if d<30:
                return True
            else:
                return False
        if m<8:
            if m%2==1:
                if d<32:
                    return True
                else:
                    return False
            if m%2==0:
                if d<31:
                    return True
                else:
                    return False
        else:
            if m%2==1:
                if d<31:
                    return True
                else:
                    return False
            if m%2==0:
                if d<32:
                    return True
                else:
                    return False
    else:
        if m==2:
            if d<29:
                return True
            else:
                return False
        if m<8:
            if m%2==1:
                if d<32:
                    return True
                else:
                    return False
            if m%2==0:
                if d<31:
                    return True
                else:
                    return False
        else:
            if m%2==1:
                if d<31:
                    return True
                else:
                    return False
            if m%2==0:
                if d<32:
                    return True
                else:
                    return False
def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
    else:
        if y%4==0:
            return True
        else:
            return False
        
while(1):
    year=int(input("enter the year starting from 1970   "))
    if year<1970:
        print("enter valid year")
    else:
        break
while(1):
    month=int(input("enter month"))
    if month>0 and month<=12:
        break
    else:
        print("enter valid month")
leap=check_leap(year)
while(1):
    date=int(input("enter date"))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("enter valid date")
print(year,month,date)
day=calendar.weekday(year, month, date) 
if day==6:
 print("sunday")  
elif day==0:
 print("monday")
elif day==1:
 print("tuesday")
elif day==2:
 print("wednesday")
elif day==3:
 print("thursday")
elif day==4:
 print("friday")
elif day==5:
 print("saturday")
   
        