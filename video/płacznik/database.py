from model_io import read_from_file, write_to_file
class PersonPathNotFound(FileNotFoundError):
    pass

class PersonPermissionError(PermissionError):
    pass

class Database:
    def __init__(self):
        self.people = []

    def load_from_file(self, path):
        try:
            with open(path, 'r') as file_handle:
                self.people = read_from_file(file_handle)
        except FileNotFoundError as e:
            raise PersonPathNotFound('Could not open person database')
        except PermissionError as e:
            raise PersonPermissionError('You do not have permission to open database')

    def save_to_file(self, path):
        try:
            with open(path, 'w'):
                write_to_file(path, self.people)
        except: 
            raise FileNotFoundError
