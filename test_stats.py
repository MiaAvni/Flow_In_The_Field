from stats import *
from models import Round, Session, ParticipantInfo, LanguageStats, ParticipantStats


# rounds
r0 = Round(0, 0, 7, 1650328640, 1650328740)
r1 = Round(1, 1, 2, 1650736936, 1650737636)
r2 = Round(2, 1, 12, 1650737636, 1650737936)
r3 = Round(3, 2, 6, 1650758536, 1650758596)
r4 = Round(4, 3, 9, 1650328640, 1650328840)
all_rounds = [r0, r1, r2, r3, r4]

# sessions
s0 = Session(0, 0, "French", [0], 1650328640, 1650328740)
s1 = Session(0, 1, "Japanese", [1, 2], 1650736936, 1650737936)
s2 = Session(0, 2, "French", [3], 1650758536, 1650758596)
s3 = Session(1, 3, "German", [4], 1650328640, 1650328840)

all_sessions = [s0, s1, s2, s3]

# participants
p0 = ParticipantInfo(0, "Kurapika Kurta", 17, [0, 1, 2])
p1 = ParticipantInfo(1, "Levi Ackerman", 31, [3])
p2 = ParticipantInfo(2, "Tanjiro Kamado", 15, [])


def test_round_duration():
    assert round_duration(r0) == 100


def test_session_duration():
    assert session_duration(s1) == 1000


def test_average():
    assert average([2, 4, 6]) == 4


def test_collect_sessions():
    sessions = collect_sessions(p0, all_sessions)
    assert sessions == [s0, s1, s2]


def test_collect_rounds_for_session():
    rounds = collect_rounds_for_session(s1, all_rounds)
    assert rounds == [r1, r2]


def test_collect_rounds_for_sessions():
    rounds = collect_rounds_for_sessions([s0, s2], all_rounds)
    assert rounds == [r0, r3]


def test_unique_languages():
    langs = unique_languages([s0, s1, s2])
    assert langs == ["French", "Japanese"]


def test_rounds_for_language():
    french_rounds = rounds_for_language("French", [s0, s2], all_rounds)
    assert french_rounds == [r0, r3]


def test_average_round_score():
    assert average_round_score([r0, r3]) == 6.5


def test_average_round_duration():
    assert average_round_duration([r0, r3]) == 80


def test_average_session_duration():
    assert average_session_duration([s0, s2]) == 80

def test_compute_participant_stats_p0():
    stats = compute_participant_stats(p0, all_sessions, all_rounds)

    assert stats.id == 0
    assert stats.name == "Kurapika Kurta"
    assert stats.averageRoundScore == 6.75
    assert stats.averageSessionDuration == 386.67

    # languages sorted by total score
    assert stats.languages[0].language == "Japanese"
    assert stats.languages[1].language == "French"


def test_compute_participant_stats_p1():
    stats = compute_participant_stats(p1, all_sessions, all_rounds)

    assert stats.id == 1
    assert stats.name == "Levi Ackerman"
    assert stats.averageRoundScore == 9
    assert stats.averageSessionDuration == 200
    assert stats.languages[0].language == "German"


def test_compute_participant_stats_no_sessions():
    stats = compute_participant_stats(p2, all_sessions, all_rounds)

    assert stats.languages == []
    assert stats.averageRoundScore == "N/A"
    assert stats.averageSessionDuration == "N/A"

if __name__ == "__main__":
    test_round_duration()
    test_session_duration()
    test_average()
    test_collect_sessions()
    test_collect_rounds_for_session()
    test_collect_rounds_for_sessions()
    test_unique_languages()
    test_rounds_for_language()
    test_average_round_score()
    test_average_round_duration()
    test_average_session_duration()
    test_compute_participant_stats_p0()
    test_compute_participant_stats_p1()
    test_compute_participant_stats_no_sessions()
    print("All tests passed")