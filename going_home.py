import datetime as dt

now = dt.datetime.now()
now_str = now.strftime('%H:%M:%S')

def datetime_format(today_str):
    time_obj = dt.datetime.strptime(today_str, '%H:%M:%S')
    return time_obj

def friday_check(data_i_vremya):
    if data_i_vremya.strftime('%A') == 'Friday':
        time_to_go_str = '16:45:00'
    else:
        time_to_go_str = '17:45:00'
    time_to_go_obj = datetime_format(time_to_go_str)
    return time_to_go_obj

def check():
    if datetime_format(now_str) >= friday_check(now):
        time_over = datetime_format(now_str) - friday_check(now)
        print('Overtime for', time_over)
    else:
        left_time = friday_check(now) - datetime_format(now_str)
        print('Going home in', left_time)
check()
