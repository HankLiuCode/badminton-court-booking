source .venv/bin/activate

session_id="<your session id>"
python reserve.py -s "$session_id" -c 場一 -t 8:00~9:00 -d 2023-11-24 &
python reserve.py -s "$session_id" -c 場一 -t 9:00~10:00 -d 2023-11-24 &