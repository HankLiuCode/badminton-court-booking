import datetime

court_to_id = {
    '場一': '0',
    '場二': '1',
    '場三': '2',
    '場四': '3',
    '場五': '4',
    '場六': '5',
    '場七': '6',
    '場八': '7'
}
time_to_id = {
    '7:00~8:00': '0',
    '8:00~9:00': '1',
    '9:00~10:00': '2',
    '10:00~11:00': '3',
    '11:00~12:00': '4',
    '12:00~13:00': '5',
    '13:00~14:00': '6',
    '14:00~15:00': '7',
    '15:00~16:00': '8',
    '16:00~17:00': '9',
    '17:00~18:00': '10',
    '18:00~19:00': '11',
    '19:00~20:00': '12',
    '20:00~21:00': '13',
    '21:00~22:00': '14',
    '22:00~23:00': '15'
}

def generate_payload(court, time, date):
    try:
        year, month, day = date.split('-')
        year, month, day = int(year), int(month), int(day)
    except Exception as e:
        raise Exception("Invalid date format. Please use YYYY-MM-DD format.")

    timeId = time_to_id[time]
    fieldId = court_to_id[court]
    return {
        'time': timeId,
        'field': fieldId,
        'date': datetime.datetime(year, month, day, 0, 0, 0).strftime('%s')
    }