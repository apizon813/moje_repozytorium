class InvalidNameError(Exception):
    pass


class InvalidSexError(Exception):
    pass


class MalformedPersonDataError(Exception):
    pass


class Person:
    def __init__(self, id, name, sex, birth_date):
        if not name:
            raise InvalidNameError("Name cannot be empty")
        if sex not in ('Male', 'Female'):
            raise InvalidSexError('Sex has to be either Female or Male')
        self._id = id
        self._name = name
        self._birth_date = birth_date
        self._sex = sex

    def __str__(self):
        id = self.id()
        name = self.name()
        born = self.birth_date()
        return f'{id}: {name}, born on {born}'

    def id(self):
        return self._id

    def name(self):
        return self._name

    def birth_date(self):
        return self._birth_date

    def sex(self):
        return self._sex
