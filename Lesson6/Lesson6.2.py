num = int(input())
days = 24*60*60
hour = 60*60
minutes = 60
if num < 8640000 and num >= 0:
    #Вычисление времени
    count_days = num//days
    delta_days = num % days
    count_hours = delta_days//hour
    delta_hours = num%hour
    count_minutes = delta_hours//minutes
    count_seconds = delta_hours%minutes

    # Суммирование
    count_hours_string = str(count_hours)
    count_minutes_string = str(count_minutes)
    count_seconds_string = str(count_seconds)
    summ=(count_hours_string.zfill(2)+":"+count_minutes_string.zfill(2)+":"+count_seconds_string.zfill(2))
    d2 = str(count_days)
    # Определение правильного названия дня
    if count_days%10 >=2 and count_days%10<5 and (count_days>20 or count_days<10):
        print(d2+ " дні, "+ summ)
    elif count_days%10==1 and (count_days>20 or count_days<10):
        print(d2+" день, "+summ)
    else:
        print(d2 + " днів, " + summ)
else:
    print("слишком большая секунда")


