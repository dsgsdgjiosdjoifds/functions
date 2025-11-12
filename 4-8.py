def convert_to_12h(hours):
    smth = "am"
    if hours >= 12 and hours <= 23:
        if hours != 12:
            hours -= 12
        smth = "pm"
    elif hours == 0:
        hours = 12
    return hours, smth

def time_string(hours, minutes, _format):
    if _format == '24':
        print(f"{hours:02d}:{minutes:02d}")
    else:
        hours, suffix = convert_to_12h(hours)
        print(f"{hours:02d}:{minutes:02d}{suffix}")


time_string(15, 38, '24')
time_string(8, 3, '24')
time_string(0, 5, '24')
time_string(11, 15, '12')
time_string(0, 7, '12')
time_string(7, 30, '12')
time_string(12, 46, '12')
time_string(13, 10, '12')
time_string(19, 2, '12')
