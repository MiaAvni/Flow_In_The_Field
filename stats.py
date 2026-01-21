from typing import List
from models import Round, Session, ParticipantInfo, LanguageStats, ParticipantStats


def round_duration(r: Round) -> int:
    """Returns the duration of a round in seconds."""
    return r.endTime - r.startTime


def session_duration(s: Session) -> int:
    """Returns the duration of a session in seconds."""
    return s.endTime - s.startTime


def average(nums: List[int]) -> float:
    """Returns the average of a list of integers."""
    total = 0
    for n in nums:
        total += n
    return total / len(nums)



def collect_sessions(
    participant: ParticipantInfo,
    all_sessions: List[Session]
) -> List[Session]:
    """Collects all sessions for a participant from the list of all sessions."""

    result = []

    for s in all_sessions:
        if s.sessionId in participant.sessions:
            result.append(s)

    return result


def collect_rounds_for_session(
    session: Session,
    all_rounds: List[Round]
) -> List[Round]:
    """Collects all rounds for a session from the list of all rounds."""

    result = []

    for r in all_rounds:
        if r.roundId in session.rounds:
            result.append(r)

    return result


def collect_rounds_for_sessions(
    sessions: List[Session],
    all_rounds: List[Round]
) -> List[Round]:
    """Collects all rounds for a list of sessions from the list of all rounds."""

    result = []

    for s in sessions:
        session_rounds = collect_rounds_for_session(s, all_rounds)
        for r in session_rounds:
            result.append(r)

    return result


def unique_languages(sessions: List[Session]) -> List[str]:
    """Returns a list of unique languages used in the sessions."""
    languages = []

    for s in sessions:
        if s.language not in languages:
            languages.append(s.language)

    return languages


def rounds_for_language(
    language: str,
    sessions: List[Session],
    all_rounds: List[Round]
) -> List[Round]:
    """Returns all rounds for a given language in a list of sessions."""

    result = []

    for s in sessions:
        if s.language == language:
            session_rounds = collect_rounds_for_session(s, all_rounds)
            for r in session_rounds:
                result.append(r)

    return result


def max_score_per_language(rounds: List[Round]) -> int:

    max = 0

    for r in rounds:
        if r.score > max:
            max == r.score
    
    return max



def average_round_score(rounds: List[Round]) -> float:
    """Returns the average score of all rounds."""
    scores = []

    for r in rounds:
        scores.append(r.score)

    return average(scores)


def average_round_duration(rounds: List[Round]) -> float:
    """Returns the average duration of all rounds in seconds."""
    durations = []

    for r in rounds:
        durations.append(round_duration(r))

    return average(durations)


def average_session_duration(sessions: List[Session]) -> float:
    """Returns the average duration of all sessions in seconds."""
    durations = []

    for s in sessions:
        durations.append(session_duration(s))

    return average(durations)


def compute_participant_stats(
    participant: ParticipantInfo,
    all_sessions: List[Session],
    all_rounds: List[Round]
) -> ParticipantStats:
    """Computes and returns the statistics for a participant."""

    sessions = collect_sessions(participant, all_sessions)

    if len(sessions) == 0:
        return ParticipantStats(
            id=participant.participantId,
            name=participant.name,
            languages=[],
            averageRoundScore="N/A",
            averageSessionDuration="N/A"
        )

    all_rounds_for_participant = collect_rounds_for_sessions(sessions, all_rounds)
    languages = unique_languages(sessions)

    language_stats = []

    for lang in languages:
        lang_rounds = rounds_for_language(lang, sessions, all_rounds)

        language_stats.append(
            LanguageStats(
                language=lang,
                averageScore=round(average_round_score(lang_rounds), 2),
                averageRoundDuration=round(average_round_duration(lang_rounds), 2)
                maxScore=round(max_score_per_language(lang_rounds),2)
            )
        )

    # sort languages by total score descending
    language_stats.sort(
        key=lambda ls: sum(
            r.score for r in rounds_for_language(ls.language, sessions, all_rounds)
        ),
        reverse=True
    )

    return ParticipantStats(
        id=participant.participantId,
        name=participant.name,
        languages=language_stats,
        averageRoundScore=round(average_round_score(all_rounds_for_participant), 2),
        averageSessionDuration=round(average_session_duration(sessions), 2)
    )
