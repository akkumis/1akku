import datetime 
def season_events(number_of_month): 
    months = ('January','February','March','April','May','June','July','August','September','October','November','December') 
 
    if number_of_month > 12: 
        return "You need to enter the real number of the month" 
    elif number_of_month == 12 or number_of_month <= 2: 
        return "You were born in " + months[number_of_month-1] + ", when white snow fell outside the window." 
    elif number_of_month > 2 and number_of_month <= 5: 
        return "You were born in " + months[number_of_month-1] + ", when birds sang beautiful songs." 
    elif number_of_month > 5 and number_of_month <= 8: 
        return "You were born in " + months[number_of_month-1] + ", when the sun shone brighter than ever." 
    else: 
        return "You were born in " + months[number_of_month-1] + ", when the harvest was incredible." 
 
month_number = int(input("month number: ")) 
print(season_events(month_number)) 
print(season_events(12)) 
print(season_events(1)) 
print(season_events(4)) 
print(season_events(8)) 
print(season_events(11)) 
print(season_events(15)) 
print("\n")
