from random import randint, choice


class NegativePowerError(Exception):
    def __init__(self, lives):
        super().__init__('Life Count cannot be negative.')
        self.lives = lives


class NameError(Exception):
    pass


class NegativeHealthError(Exception):
    def __init__(self, health):
        super().__init__('Health cannot be negative')
        self.health = health


class InvalidHeadCountError(Exception):
    def __init__(self, count):
        super().__init__('Needs to have at least one head.')
        self.head_count == count


class Player:
    '''
    Class Player. Contains attributes:
    :param name: player's name
    :type name: str

    :param power: player's lives, defaults to 5
    :type lives: int
    '''
    def __init__(self, name, power=5):
        self._name = name
        power = int(power)
        if power < 0:
            raise NegativePowerError(power)
        self._power = power

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            raise NameError('Name cannot be empty.')
        self._name = str(new_name).title()

    def power(self):
        return self._power

    def set_power(self, new_power):
        if new_power < 0:
            raise NegativePowerError(new_power)
        self._power = new_power

    def attack(self, enemies):
        if self.power() == 0 or not enemies:
            return
        # choose enemy from enemies
        enemy = choice(enemies)
        # calculate damage
        damage = randint(1, self.power())
        enemy.take_damage(damage)
        # apply damage
        self._power -= 1

    def info(self):
        '''
        Returns basic describtion of the player.
        '''
        return f'My name is {self._name}. I have {self._power} points of power'

    def __str__(self):
        return self.info()


class Enemy():
    def __init__(self, name, health):
        '''
        Creates instance of Enemy.

        Raises NameError if name is empty od health is negative.
        '''
        if not name:
            raise NameError('Name cannot be empty.')
        health = int(health)
        if health < 0:
            raise NegativeHealthError('Health cannot be negative.')
        self._name = name
        self._health = health

    def name(self):
        '''
        Returns name of the enemy.
        '''
        return self._name

    def set_name(self, new_name):
        '''
        Sets name of enemy to new_name
        '''
        if not new_name:
            raise NameError('Name cannot be empty.')
        self._name = new_name

    def health(self):
        '''
        Returns health of enemy
        '''
        return self._health

    def set_health(self, new_health):
        '''
        Sets health of enemy to new_health
        '''
        self._health = max(0, new_health)

    def __str__(self):
        name = self._name
        health = self._health
        return f'This is {name}. It has {health} health points left.'

    def take_damage(self, damage):
        '''
        Reduces health of enemy by damage.
        '''
        damage = int(damage)
        if damage <= 0:
            raise ValueError('Damage has to be positive')
        self._health -= min(damage, self._health)

    def is_alive(self):
        '''
        Returns True if health greater than 0.
        '''
        return self._health > 0


class Hydra(Enemy):
    def __init__(self, name, health, heads=1):
        super().__init__(name, health)
        if heads < 1:
            raise InvalidHeadCountError(heads)
        self._heads = heads
        self._base_health = health

    def heads(self):
        return self._heads

    def base_health(self):
        return self._base_health

    def regenerate(self, heal):
        if heal < 0:
            raise ValueError('Heal has to be positive')

        if self.health() >= self.base_health():
            return
        self._health += min(heal, self._base_health - self._health)

    def __str__(self):
        base = super().__str__()
        heads = self._heads
        return f'{base} It has {heads} heads.'


class DragonHydra(Hydra):
    def take_damage(self, damage):
        if randint(0, 1):
            super().take_damage(damage)


class Game:
    def __init__(self, player, enemies=None):
        self.player = player
        self.enemies = enemies if enemies else []
        self._result = None
