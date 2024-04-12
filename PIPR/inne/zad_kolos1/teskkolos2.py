def time_description(hours, minutes):
    if hours > 12 or minutes > 60:
        return "Incorrect input data!"

    dict = {
        0: '',
        1: 'one',
        2: "two",
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelf',
        20: 'twenty',
        30: 'thirty',
        40: 'fourty',
        50: 'fifty',
    }

    if minutes == 0:
        return f"{dict[hours]} o' clock"
    elif minutes == 15:
        return f"quarter past {dict[hours]}"
    elif minutes == 45:
        return f"quarter to {dict[(hours+1)%12]}"
    else:
        if minutes < 30:
            return f"{dict[minutes // 10]}"\
                f" {dict[minutes % 10]} past {dict[hours]}"
        else:
            return f"{dict[minutes // 10]}"\
                f" {dict[minutes % 10]} to {dict[hours]}"


print(time_description(8, 15))
print(time_description(11, 13))
print(time_description(12, 30))
print(time_description(6, 37))
print(time_description(3, 45))
print(time_description(15, 5))
