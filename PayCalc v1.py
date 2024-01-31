def convert_line():
    global data, date

    if data == "\n":
        data = "..."
        print(data)
    else:
        data = data.strip().split(" ")
        date = data[0] + " " + data[1]

        if len(data) == 4:
            solo_shift()
        else:
            split_shift()


def solo_shift():
    global data, date, total

    start_time = data[2]
    finish_time = data[3]
    a = start_time.split(":")
    b = finish_time.split(":")

    hours_total = int(b[0]) - int(a[0])  # finish hour - start hour
    minutes_total = int(b[1]) - int(a[1])  # finish min - start min

    if minutes_total <= -1:
        hours_total -= 1
        minutes_total += 60
    else:
        pass

    if int(b[0]) >= int(a[0]):  # finish hour > start hour
        pass
    else:
        hours_total += 24  # converts 00:00 into 24:00

    total += hours_total + (minutes_total / 60)
    pay = (hours_total * hourly_rate) + (minutes_total * (hourly_rate / 60))
    data = str(date), str(start_time) + "-" + str(finish_time), str(hours_total) + "h" + str(
        minutes_total) + "m", "£" + str(round(pay, 2))
    data = " ".join(data)
    print(data)


def split_shift():
    global data, date, total

    start_time_1 = data[2]
    finish_time_1 = data[3]
    start_time_2 = data[4]
    finish_time_2 = data[5]
    a = start_time_1.split(":")
    b = finish_time_1.split(":")
    y = start_time_2.split(":")
    z = finish_time_2.split(":")

    hours_1 = int(b[0]) - int(a[0])
    minutes_1 = int(b[1]) - int(a[1])
    hours_2 = int(z[0]) - int(y[0])
    minutes_2 = int(z[1]) - int(y[1])
    hours_total = hours_1 + hours_2
    minutes_total = minutes_1 + minutes_2

    if minutes_total <= -61:
        hours_total -= 2
        minutes_total += 120
    elif minutes_total <= -1:
        hours_total -= 1
        minutes_total += 60
    elif minutes_total >= 60:
        hours_total += 1
        minutes_total -= 60
    else:
        pass

    if int(z[0]) >= int(y[0]):
        pass
    else:
        hours_total += 24

    total += hours_total + (minutes_total / 60)
    pay = (hours_total * hourly_rate) + (minutes_total * (hourly_rate / 60))
    data = str(date), str(start_time_1) + "-" + str(finish_time_1), str(start_time_2) + "-" + str(finish_time_2), str(
        hours_total) + "h" + str(minutes_total) + "m", "£" + str(round(pay, 2))
    data = " ".join(data)
    print(data)


def read_txt_file():
    with open('C:/Users/armag/Documents/Shifts.txt', 'r') as f:
        global data
        for data in f:
            convert_line()
            write_txt_file()


def write_txt_file():
    with open('C:/Users/armag/Documents/Shifts_plus.txt', 'a') as f:
        global data
        f.write(data + "\n")


hourly_rate = 10.48
total = 0

read_txt_file()
print(str(total), "hours worked", "£" + str(total * hourly_rate))
