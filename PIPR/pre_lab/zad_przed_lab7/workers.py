class Worker:
    '''
    atrybuty:
    imie
    nazwisko
    email
    metody:
    ustawianie
    odczyt
    '''
    def __init__(self, email, fname, lname):
        self._email = email
        self._fname = fname
        self._lname = lname

    @property
    def email(self):
        return self._email

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    def set_email(self, new_email):
        self._email = new_email

    def set_fname(self, new_fname):
        self._email = new_fname

    def set_lname(self, new_lname):
        self._email = new_lname


class Full_time_worker(Worker):
    '''
    atrybuty:
    pensja
    metody:
    ustawianie
    odczyt
    '''
    def __init__(self, email, fname, lname, salary):
        super().__init__(email, fname, lname)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary


class Technic_worker(Worker):
    '''
    atrybuty:
    stawka na godzine
    wymiar godzin
    metody:
    obliczyć miesięczną wypłatę
    '''
    def __init__(self, email, fname, lname, rph, hours):
        super().__init__(email, fname, lname)
        self._rph = rph
        self._hours = hours

    @property
    def rph(self):
        return self._rph

    def set_rph(self, new_rph):
        self._rph = new_rph

    def monthly_payment(self):
        return self.rph


class Programist:
    '''
    astrybuty:
    język
    '''
    pass


class Menager:
    '''
    atrybuty:
    podlegli pracownicy
    metody:
    dodawanie osób
    usuwanie osób

    '''
