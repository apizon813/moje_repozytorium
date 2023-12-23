from lotto import LottoGame

def test_init():
    game = LottoGame()
    assert game.player_numbers() == set()
    assert game.winning_numbers() == set()

def test_draw_winning_numbers(monkeypatch):
    game = LottoGame()
    def get_list(s, e):
        return [1, 2, 3, 4, 5, 6]
    monkeypatch.setattr('lotto.sample', get_list)
    game.draw_winning_numbers()
    assert game.winning_numbers() == {1, 2, 3, 4, 5, 6}

def test_set_player_numbers_none(monkeypatch):
    game = LottoGame()
    def get_list(s, e):
        return [6, 5, 4, 3, 2, 1]
    monkeypatch.setattr('lotto.sample', get_list)
    game.set_player_numbers()
    assert game.player_numbers() == {6, 5, 4, 3, 2, 1}

def test_set_player_numbers():
    game = LottoGame()
    list = [11, 12, 13, 14, 15, 16]
    game.set_player_numbers(list)
    assert game.player_numbers() == {11, 12, 13, 14, 15, 16}
