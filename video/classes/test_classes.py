from classes import Player, Enemy, Hydra, DragonHydra, Game
from classes import NegativeHealthError, NegativePowerError, NameError
import pytest


def test_creaate_player():
    player = Player('Jurek Ogórek')
    assert player.name() == 'Jurek Ogórek'
    assert player.power() == 5


def test_create_player_with_power():
    player = Player('Jurek Ogórek', 4)
    assert player.name() == 'Jurek Ogórek'
    assert player.power() == 4


def test_create_player_with_negative_power():
    with pytest.raises(NegativePowerError):
        Player('Jurek Ogórek', -1)


def test_introduce():
    player = Player('Jurek Ogórek', 3)
    assert player.info() == 'My name is Jurek Ogórek. I have 3 points of power'


def test_introduce_as_str():
    player = Player('Jurek Ogórek', 3)
    assert str(player) == player.info()
    player = Player('Jurek Ogórek', 1)
    assert str(player) == player.info()


def test_set_name():
    player = Player('Jurek Ogórek')
    assert player.name() == 'Jurek Ogórek'
    player.set_name('Karolina Malina')
    assert player.name() == 'Karolina Malina'


def test_set_name_empty():
    player = Player('Jurek Ogórek')
    with pytest.raises(NameError):
        player.set_name('')


def test_set_name_lowercase():
    player = Player('Jurek Ogórek')
    assert player.name() == 'Jurek Ogórek'
    player.set_name('kaROlina maLINa')
    assert player.name() == 'Karolina Malina'


def test_set_power():
    player = Player('Jurek Ogórek')
    assert player.power() == 5
    player.set_power(2)
    assert player.power() == 2


def test_set_power_zero():
    player = Player('Jurek Ogórek')
    assert player.power() == 5
    player.set_power(0)
    assert player.power() == 0


def test_set_power_negative():
    player = Player('Jurek Ogórek')
    assert player.power() == 5
    with pytest.raises(NegativePowerError):
        player.set_power(-1)


def test_attack():
    player = Player('Jurek Ogórek')
    assert player.power() == 5
    orc = Enemy('orc', 10)
    assert orc.health() == 10
    enemies = [orc]
    player.attack(enemies)
    assert player.power() == 4
    assert orc.health() < 10


def test_attack_choice():
    player = Player('Jurek Ogórek')
    orc1 = Enemy('orc1', 10)
    orc2 = Enemy('orc2', 20)
    enemies = [orc1, orc2]
    player.attack(enemies)
    assert player.power() == 4
    assert orc1.health() < 10 or orc2.health() < 20


def test_attack_choose_enemy(monkeypatch):
    player = Player('Jurek Ogórek')
    orc1 = Enemy('orc1', 10)
    orc2 = Enemy('orc2', 20)
    enemies = [orc1, orc2]

    def get_orc2(orcs):
        return orc2
    monkeypatch.setattr('classes.choice', get_orc2)

    player.attack(enemies)
    assert player.power() == 4
    assert orc1.health() < 10 or orc2.health() < 20


def test_enemy_create():
    enemy = Enemy('orc', 50)
    assert enemy.name() == 'orc'
    assert enemy.health() == 50


def test_enemy_create_negative_health():
    with pytest.raises(NegativeHealthError):
        Enemy('orc', -10)


def test_enemy_create_empty_name():
    with pytest.raises(NameError):
        Enemy('', 10)


def test_enemy_set_name():
    enemy = Enemy('orc', 50)
    assert enemy.name() == 'orc'
    enemy.set_name('dragon')
    assert enemy.name() == 'dragon'


def test_enemy_set_name_empty():
    enemy = Enemy('orc', 50)
    with pytest.raises(NameError):
        enemy.set_name('')


def test_enemy_set_health():
    enemy = Enemy('orc', 50)
    assert enemy.health() == 50
    enemy.set_health(60)
    assert enemy.health() == 60


def test_enemy_set_health_negative():
    enemy = Enemy('orc', 50)
    assert enemy.health() == 50
    enemy.set_health(-10)
    assert enemy.health() == 0


def test_enemy_description():
    enemy = Enemy('orc', 50)
    assert str(enemy) == 'This is orc. It has 50 health points left.'


def test_enemy_take_damage():
    enemy = Enemy('orc', 40)
    assert enemy.health() == 40
    enemy.take_damage(10)
    assert enemy.health() == 30


def test_enemy_take_damage_invalid():
    enemy = Enemy('orc', 40)
    with pytest.raises(ValueError):
        enemy.take_damage(-10)
    with pytest.raises(ValueError):
        enemy.take_damage(0)


def test_enemy_take_damage_drops_below_zero():
    enemy = Enemy('orc', 10)
    assert enemy.health() == 10
    enemy.take_damage(30)
    assert enemy.health() == 0


def test_enemy_is_alive_true():
    enemy = Enemy('orc', 10)
    assert enemy.health() == 10
    assert enemy.is_alive()


def test_enemy_is_alive_false():
    enemy = Enemy('orc', 0)
    assert enemy.health() == 0
    assert not enemy.is_alive()


def test_hydra_create():
    hydra = Hydra('Hydra', health=20, heads=3)
    assert hydra.name() == 'Hydra'
    assert hydra.health() == 20
    assert hydra.heads() == 3


def test_hydra_create_default_heads():
    hydra = Hydra('Hydra', health=20)
    assert hydra.name() == 'Hydra'
    assert hydra.health() == 20
    assert hydra.heads() == 1


def test_hydra_describtion():
    hydra = Hydra('two-headed-hydra', 30, 2)
    assert str(hydra) == 'This is two-headed-hydra.'\
        ' It has 30 health points left. It has 2 heads.'


def test_hydra_regenerate():
    hydra = Hydra('two-headed-hydra', 30, 2)
    hydra.take_damage(10)
    hydra.regenerate(5)
    assert hydra.health() == 25


def test_hydra_regenerate_max_health():
    hydra = Hydra('two-headed-hydra', 30, 2)
    hydra.take_damage(10)
    hydra.regenerate(15)
    assert hydra.health() == 30


def test_hydra_base_health():
    hydra = Hydra('two-headed-hydra', 30, 2)
    assert hydra.base_health() == 30


def test_hydra_set_health_above_base():
    hydra = Hydra('two-headed-hydra', 30, 2)
    assert hydra.base_health() == 30
    hydra.set_health(50)
    assert hydra.health() == 50
    assert hydra.base_health() == 30


def test_hydra_regenerate_health_above_base():
    hydra = Hydra('two-headed hydra', 30, 2)
    assert hydra.base_health() == 30
    hydra.set_health(50)
    hydra.take_damage(10)  # health = 40, base = 30
    hydra.regenerate(5)
    assert hydra.health() == 40


def test_dragonhydra_take_damage_hit(monkeypatch):
    def returnOne(f, t):
        return 1
    monkeypatch.setattr('classes.randint', returnOne)
    enemy = DragonHydra('dragon', 40, 3)
    assert enemy.health() == 40
    enemy.take_damage(10)
    assert enemy.health() == 30


def test_dragonhydra_take_damage_miss(monkeypatch):
    def returnZero(f, t):
        return 0
    monkeypatch.setattr('classes.randint', returnZero)
    enemy = DragonHydra('dragon', 40, 3)
    assert enemy.health() == 40
    enemy.take_damage(10)
    assert enemy.health() == 40


def test_game_create():
    player = Player('Jurek ogórek')
    enemies = [
        Hydra('hydra', 10),
        Enemy('orc', 20)
    ]
    game = Game(player, enemies)
    assert game.player == player
    assert game.enemies == enemies


def test_game_create_defult_enemies():
    player = Player('Jórek Ogórek')

    game = Game(player)
    assert game.player == player
    assert game.enemies == []
