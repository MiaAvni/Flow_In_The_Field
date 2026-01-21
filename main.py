import requests
from stats import compute_participant_stats
from models import ParticipantInfo, Round, Session
from dataclasses import asdict

URL = "https://recruitment.sandboxnu.com/api/eyJkYXRhIjp7ImNoYWxsZW5nZSI6IkZsb3ciLCJlbWFpbCI6ImF2bmkubUBub3J0aGVhc3Rlcm4uZWR1IiwiZHVlRGF0ZSI6IjIwMjUtMTItMTlUMDU6MDA6MDAuMDAwWiJ9LCJoYXNoIjoibjlFcVgyYjBNYy0xSTJlVVZZUSJ9"

response = requests.get(URL)
data = response.json()

# convert dictionaries into dataclass objects
rounds = [
    Round(
        roundId=r['roundId'],
        sessionId=r['sessionId'],
        score=r['score'],
        startTime=r['startTime'],
        endTime=r['endTime']
    ) for r in data.get('rounds', [])
]

sessions = [
    Session(
        participantId=s['participantId'],
        sessionId=s['sessionId'],
        language=s['language'],
        rounds=s['rounds'],  
        startTime=s['startTime'],
        endTime=s['endTime']
    ) for s in data.get('sessions', [])
]

participants = [
    ParticipantInfo(
        participantId=p['participantId'],
        name=p['name'],
        age=p['age'],
        sessions=p['sessions']
    ) for p in data.get('participantInfo', [])
]

# compute stats
participant_stats = [compute_participant_stats(p, sessions, rounds) for p in participants]

# sort by name
participant_stats.sort(key=lambda x: x.name)

# convert to dictionaries for posting
participant_stats_dict = [asdict(p) for p in participant_stats]

# post result
post_response = requests.post(URL, json=participant_stats_dict)
print(post_response.status_code)
print(post_response.text)
