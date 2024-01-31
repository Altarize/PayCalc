from datetime import datetime, timedelta


def read_txt():
    global data

    with open('C:/Users/armag/Documents/Shifts.txt', 'r') as f:
        for data in f:
            convert_line()


def write_txt():
    global data

    with open('C:/Users/armag/Documents/Shifts_plus.txt', 'w') as f:
        f.write(str(data) + "\n")


def convert_line():
    global data, date, year, month, og_data

    if len(data.strip()) == 4:
        year = data.strip()

    elif len(data.strip()) == 3:
        month = data.strip()

    else:
        og_data = data.strip()
        data = data.strip().split(" ")
        data.insert(0, year), data.insert(1, month)
        date = data[0:4]

        if len(data) == 6:
            solo_shift()
        else:
            split_shift()


def solo_shift():
    global data, date, total

    start = "".join(data[4:5])
    finish = "".join(data[5:6])

    date = " ".join(date)

    date_start = f"{date} {start}"
    date_finish = f"{date} {finish}"

    start_obj = datetime.strptime(date_start, "%Y %b %a %d %H:%M")
    finish_obj = datetime.strptime(date_finish, "%Y %b %a %d %H:%M")

    time_delta = finish_obj - start_obj

    if finish_obj < start_obj:
        time_delta += timedelta(days=1)

    seconds = time_delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    daily_earning = round((hours * hourly_rate) + (minutes * hourly_rate / 60), 2)

    data = f"{og_data} {hours}h {minutes}m £{daily_earning}"

    print(data)

    total += time_delta.seconds


def split_shift():
    global data, date, total

    morning_start = "".join(data[4:5])
    morning_finish = "".join(data[5:6])
    evening_start = "".join(data[6:7])
    evening_finish = "".join(data[7:8])

    date = " ".join(date)

    date_morning_start = date + " " + morning_start
    date_morning_finish = date + " " + morning_finish
    date_evening_start = date + " " + evening_start
    date_evening_finish = date + " " + evening_finish

    morning_start_obj = datetime.strptime(date_morning_start, "%Y %b %a %d %H:%M")
    morning_finish_obj = datetime.strptime(date_morning_finish, "%Y %b %a %d %H:%M")
    evening_start_obj = datetime.strptime(date_evening_start, "%Y %b %a %d %H:%M")
    evening_finish_obj = datetime.strptime(date_evening_finish, "%Y %b %a %d %H:%M")

    time_delta = (morning_finish_obj - morning_start_obj) + (evening_finish_obj - evening_start_obj)

    if evening_finish_obj < evening_start_obj:
        time_delta += timedelta(days=1)

    seconds = time_delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    daily_earning = round((hours * hourly_rate) + (minutes * hourly_rate / 60), 2)

    data = f"{og_data} {hours}h {minutes}m £{daily_earning}"

    print(data)

    total += time_delta.seconds


hourly_rate = 10.48
total: int = 0

read_txt()
print(total / 60 / 60)