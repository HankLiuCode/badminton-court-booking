import requests
import json
from utils import generate_payload
import argparse

class CourtBooker:
    def __init__(self, session_id):
        self.session_id = session_id
        self.URL = 'https://nthualb.url.tw/reservation/api/reserve_field'

    def reserve(self, court, time, date):
        payload = generate_payload(court, time, date)
        response = requests.post(
            self.URL,
            cookies={'PHPSESSID': self.session_id},
            data=json.dumps(payload)
        )
        return response

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Court Booker')
    parser.add_argument('-s', '--session_id', type=str, help='You can get your session_id from chrome dev tools. Search for PHPSESSID and copy the value of', required=True)
    parser.add_argument('-c', '--court', type=str, help='e.g. 場一, 場二...場八' , required=True)
    parser.add_argument('-t', '--timeslot', type=str, help='e.g. 8:00~9:00' , required=True)
    parser.add_argument('-d','--date', type=str, help='format: YYYY-MM-DD', required=True)
    args = parser.parse_args()
    court_booker = CourtBooker(args.session_id)
    response = court_booker.reserve(args.court, args.timeslot, args.date)
    if response.text == 'ok':
        print(f'{args.date} {args.timeslot} {args.court} reservation succeeded')
    else:
        print(f'{args.date} {args.timeslot} {args.court} reservation failed, check if session id is expired')