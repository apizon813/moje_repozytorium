class Testowa_klasa:
    def __init__(self, right, left, list: list=None):
        self._right = right
        self._left = left
        self._list = list

    def rev_list(self):
        list = self._list
        return list.reverse
    
    def use_lambda(self):
        return (lambda x: x * 3)(2)
    
    