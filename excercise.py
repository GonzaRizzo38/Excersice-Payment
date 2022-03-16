from datetime import datetime
file = open('hours.txt', 'r')

def cut_string(string):
    final_string = string[:-1]
    return final_string

def calculate_hours(initial_time, final_time):
    hours_1 = 0
    hours_2 = 0
    hours_3 = 0
    if initial_time < datetime.strptime('09:01', '%H:%M'):
        if final_time < datetime.strptime('09:00', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'):
            dif_time = final_time - initial_time 
            hours_1 = dif_time
        elif final_time < datetime.strptime('18:01', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'):
            dif_time = datetime.strptime('09:00', '%H:%M') - initial_time
            hours_1 = dif_time
            dif_time = final_time - datetime.strptime('09:01', '%H:%M')
            hours_2 = dif_time
        elif final_time <= datetime.strptime('23:59', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'): 
            dif_time = datetime.strptime('09:00', '%H:%M') - initial_time
            hours_1 = dif_time
            dif_time = datetime.strptime('18:00', '%H:%M') - datetime.strptime('09:01', '%H:%M') 
            hours_2 = dif_time
            dif_time = final_time - datetime.strptime('18:01', '%H:%M')
            hours_3 = dif_time
        if final_time == datetime.strptime('00:00', '%H:%M'):
            dif_time = datetime.strptime('09:00', '%H:%M') - initial_time
            hours_1 = dif_time
            dif_time = datetime.strptime('18:00', '%H:%M') - datetime.strptime('09:01', '%H:%M') 
            hours_2 = dif_time
            dif_time = datetime.strptime('23:59', '%H:%M') - datetime.strptime('18:01', '%H:%M')
            dif_time = dif_time + 0.01
            hours_3 = dif_time 
    elif initial_time < datetime.strptime('18:01', '%H:%M'):
        if final_time < datetime.strptime('18:01', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'):
            dif_time = final_time - initial_time
            hours_2 = dif_time
        elif final_time <= datetime.strptime('23:59', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'):
            dif_time = datetime.strptime('18:00', '%H:%M') - initial_time
            hours_2 = dif_time
            dif_time = final_time - datetime.strptime('18:01', '%H:%M')
            hours_3 = dif_time
        if final_time == datetime.strptime('00:00', '%H:%M'):
            dif_time = datetime.strptime('18:00', '%H:%M') - initial_time 
            hours_2 = dif_time
            dif_time = datetime.strptime('23:59', '%H:%M') - datetime.strptime('18:01', '%H:%M')
            dif_time = dif_time + 0.01
            hours_3 = dif_time 
    else:
        if final_time <= datetime.strptime('23:59', '%H:%M') and final_time > datetime.strptime('00:00', '%H:%M'):
            dif_time = final_time - initial_time
            hours_3 = dif_time
        else:
            dif_time = datetime.strptime('23:59', '%H:%M') - initial_time
            dif_time = dif_time + 0.01
            hours_3 = dif_time
    if hours_1 != 0:
        hours_1 = round(((float(hours_1.total_seconds()) / 60) / 60), 2)
    if hours_2 != 0:
        hours_2 = round(((float(hours_2.total_seconds()) / 60) / 60), 2)
    if hours_3 != 0:
        hours_3 = round(((float(hours_3.total_seconds()) / 60) / 60), 2)           
    return [hours_1, hours_2, hours_3]

def calculate_price(journal_hours, day2let):
    if day2let == 'SA' or day2let == 'SU':
        price_1 = journal_hours[0] * 30
        price_2 = journal_hours[1] * 20
        price_3 = journal_hours[2] * 25
        price = price_1 + price_2 + price_3
    else:
        price_1 = journal_hours[0] * 25
        price_2 = journal_hours[1] * 15
        price_3 = journal_hours[2] * 20
        price = price_1 + price_2 + price_3
    return price
    

            
names = []
days = []
name_nbr = 0

for line in file:
    text = line.split('=')
    if len(text) > 1:
        names.append(text[0])
        d = cut_string(text[1])
        days.append(d)

for day in days:
    journals = day.split(',')
    total_price = 0
    for journal in journals:
        day2let = journal[:2]
        hours = journal[2:]
        hour_dif = hours.split('-') 
        initial_time = hour_dif[0]
        final_time = hour_dif[1] 
        initial_time = datetime.strptime(initial_time, '%H:%M')
        final_time = datetime.strptime(final_time, '%H:%M')
        journal_hours = calculate_hours(initial_time, final_time)
        journal_price = calculate_price(journal_hours, day2let)
        total_price += journal_price
    print('The amount to pay ' + names[name_nbr] + ' is: ' + str(total_price) + ' USD')
    name_nbr += 1