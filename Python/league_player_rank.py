# Created by Jose del Rio 2020/08/30
# Copyright 2020 Jose del Rio. All rights reserved.

# Problem statement:
# -----------------
#   Implement the player_rank function that returns the player at the given rank.
#
#   The LeagueTable class tracks the score of each player in a league.
#   After each game, the player records their score with the record_result function.
#   The player's rank in the league is calculated using the following logic:
#       1) The player with the highest score is ranked first (rank 1). The player with the lowest score is ranked last.
#       2) If 2 players are tied on score, then the player who has played the fewest games is ranked higher.
#       3) If 2 players are tied on score and number of games played, then the player who was first
#          in the list of players is ranked higher.


from collections import Counter, OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        """player_rank must return the name of the player in the rank requested"""
        # Initialize ranking
        players_ranking = {}
        i = 1
        # Fill dictionary sorted by order of player list
        for key in self.standings:
            players_ranking[i] = key
            i += 1

        for _ in self.standings:
            for j in players_ranking:
                if j < len(players_ranking):
                    if self.standings[players_ranking[j+1]]['score'] > self.standings[players_ranking[j]]['score']:
                        # Swap as per higher score
                        players_ranking[j], players_ranking[j+1] = players_ranking[j+1], players_ranking[j]

                    elif self.standings[players_ranking[j+1]]['score'] == self.standings[players_ranking[j]]['score']:
                        # Tied scores. Swap as per games played
                        if self.standings[players_ranking[j+1]]['games_played'] < \
                           self.standings[players_ranking[j]]['games_played']:
                            players_ranking[j], players_ranking[j+1] = players_ranking[j+1], players_ranking[j]

        print(f"Full ranking: {players_ranking}")
        return players_ranking[rank]


def test_player_rank():
    # Create league table
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 2)
    table.record_result('Chris', 3)
    expected_rank_1 = 'Arnold'
    expected_rank_2 = 'Mike'
    expected_rank_3 = 'Chris'

    assert table.player_rank(1) == expected_rank_1
    assert table.player_rank(2) == expected_rank_2
    assert table.player_rank(3) == expected_rank_3


if __name__ == "__main__":
    test_player_rank()
