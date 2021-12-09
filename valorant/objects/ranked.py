import typing as t

from .dto import DTO


class LeaderboardPlayerDTO(DTO):
    puuid: str
    gameName: str
    tagLine: str
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int


class LeaderboardDTO(DTO):
    shard: str
    actId: str
    totalPlayers: int
    players: t.Iterable[LeaderboardPlayerDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.players = [LeaderboardPlayerDTO(p) for p in obj["players"]]
