# https://codingdojo.org/kata/Tennis/

import unittest
from tennis_scoring import TennisGame


class TestTennisGame(unittest.TestCase):
    def setUp(self) -> None:
        self.game = TennisGame()

    def _create_score(self, player1_score, player2_score):
        for _ in range(player1_score):
            self.game.player1_scored()
        for _ in range(player2_score):
            self.game.player2_scored()

    def test_initial_score(self):
        initial_score = self.game.score
        self.assertEqual("love all", initial_score)

    def test_score_is_15_0_when_p1_scored_once(self):
        self._create_score(1, 0)
        self.assertEqual("fifteen love", self.game.score)

    def test_score_is_0_15_when_p2_scored_once(self):
        self._create_score(0, 1)
        self.assertEqual("love fifteen", self.game.score)

    def test_score_is_15_15_when_p1_scored_once_and_p2_scored_once(self):
        self._create_score(1, 1)
        self.assertEqual("fifteen all", self.game.score)

    def test_score_is_30_0_when_p1_scored_twice(self):
        self._create_score(2, 0)
        self.assertEqual("thirty love", self.game.score)

    def test_score_is_0_30_when_p2_scored_twice(self):
        self._create_score(0, 2)
        self.assertEqual("love thirty", self.game.score)

    def test_score_is_30_15_when_p1_scored_twice_and_p2_scored_once(self):
        self._create_score(2, 1)
        self.assertEqual("thirty fifteen", self.game.score)

    def test_score_is_15_30_when_p1_scored_once_and_p2_scored_twice(self):
        self._create_score(1, 2)
        self.assertEqual("fifteen thirty", self.game.score)

    def test_score_is_30_30_when_p1_scored_twice_and_p2_scored_twice(self):
        self._create_score(2, 2)
        self.assertEqual("thirty all", self.game.score)

    def test_score_is_40_0_when_p1_scored_3times(self):
        self._create_score(3, 0)
        self.assertEqual("forty love", self.game.score)

    def test_score_is_0_40_when_p2_scored_3times(self):
        self._create_score(0, 3)
        self.assertEqual("love forty", self.game.score)

    def test_score_is_40_15_when_p1_scored_3times_and_p2_scored_once(self):
        self._create_score(3, 1)
        self.assertEqual("forty fifteen", self.game.score)

    def test_score_is_15_40_when_p1_scored_once_and_p2_scored_3times(self):
        self._create_score(1, 3)
        self.assertEqual("fifteen forty", self.game.score)

    def test_score_is_40_30_when_p1_scored_3times_and_p2_scored_twice(self):
        self._create_score(3, 2)
        self.assertEqual("forty thirty", self.game.score)

    def test_score_is_30_40_when_p1_scored_twice_and_p2_scored_3times(self):
        self._create_score(2, 3)
        self.assertEqual("thirty forty", self.game.score)

    def test_score_is_40_40_when_p1_scored_3times_and_p2_scored_3times(self):
        self._create_score(3, 3)
        self.assertEqual("forty all", self.game.score)

    def test_game_for_p1_when_scored_4times(self):
        self._create_score(4, 0)
        self.assertEqual("Game for Player1", self.game.score)

    def test_game_for_p2_when_scored_4times(self):
        self._create_score(0, 4)
        self.assertEqual("Game for Player2", self.game.score)

    def test_deuce(self):
        self._create_score(4, 4)
        self.assertEqual("deuce", self.game.score)

    def test_deuce_when_both_scored_7times(self):
        self._create_score(7, 7)
        self.assertEqual("deuce", self.game.score)

    def test_advantage_p1_when_score_5_4(self):
        self._create_score(5, 4)
        self.assertEqual("Player1 has advantage", self.game.score)

    def test_advantage_p2_when_score_4_5(self):
        self._create_score(4, 5)
        self.assertEqual("Player2 has advantage", self.game.score)

    def test_advantage_p1_when_score_12_11(self):
        self._create_score(12, 11)
        self.assertEqual("Player1 has advantage", self.game.score)

    def test_advantage_p2_when_score_11_12(self):
        self._create_score(11, 12)
        self.assertEqual("Player2 has advantage", self.game.score)

    def test_game_for_p1_after_deuce(self):
        self._create_score(6, 4)
        self.assertEqual("Game for Player1", self.game.score)

    def test_game_for_p2_after_deuce(self):
        self._create_score(4, 6)
        self.assertEqual("Game for Player2", self.game.score)

    def test_game_for_p1_when_score_is_24_22(self):
        self._create_score(24, 22)
        self.assertEqual("Game for Player1", self.game.score)

    def test_game_for_p2_when_score_is_22_24(self):
        self._create_score(22, 24)
        self.assertEqual("Game for Player2", self.game.score)
