from dataclasses import dataclass
from typing import List

@dataclass
class Round: 
    roundId: int
    sessionId: int
    score: int
    startTime: int
    endTime: int


@dataclass
class Session: 
    participantId: int
    sessionId: int
    language: str
    rounds: List[int]
    startTime: int
    endTime: int


@dataclass
class ParticipantInfo: 
    participantId: int
    name: str
    age: int
    sessions: List[int]

@dataclass
class LanguageStats:
    language: str
    averageScore: float
    averageRoundDuration: float
    maxScore: float

@dataclass
class ParticipantStats:
    id: int
    name: str
    languages: List[LanguageStats]
    averageRoundScore: float
    averageSessionDuration: float

