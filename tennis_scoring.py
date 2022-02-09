class TennisGame:
    def __init__(self):
        self._p1_score = 0
        self._p2_score = 0

    @property  # trochę jak getter > pole widoczne, ale chronione przed zapisem
    def score(self):
        return self._calculate_score()

    def player1_scored(self):
        self._p1_score += 1

    def player2_scored(self):
        self._p2_score += 1

    def _calculate_score(self):
        if self._is_game_won():
            return f"Game for {self._player_with_higher_score()}"
        if self._is_deuce():
            return "deuce"
        if self._is_advantage():
            return f"{self._player_with_higher_score()} has advantage"
        if self._p1_score == self._p2_score:
            return f"{self._translate_score(self._p1_score)} all"
        return f"{self._translate_score(self._p1_score)} " \
               f"{self._translate_score(self._p2_score)}"

    def _is_deuce(self):
        return 4 <= self._p1_score == self._p2_score >= 4

    def _is_advantage(self):
        return self._p1_score >= 4 and self._p2_score >= 4 and \
               abs(self._p1_score - self._p2_score) == 1

    def _is_game_won(self):
        return (self._p1_score >= 4 or self._p2_score >= 4) and \
               abs(self._p1_score - self._p2_score) >= 2

    def _player_with_higher_score(self):
        if self._p1_score > self._p2_score:
            return "Player1"
        elif self._p2_score > self._p1_score:
            return "Player2"

    @staticmethod
    def _translate_score(player_score):
        if player_score == 0:
            return "love"
        elif player_score == 1:
            return "fifteen"
        elif player_score == 2:
            return "thirty"
        elif player_score == 3:
            return "forty"
