from model_io import read_from_file, MalformedPersonDataError
from io import StringIO
import pytest


def test_read_from_file():
    data = 'id,name,sex,birth_date\nid1,name1,Female,1/1/2000\n'
    file_handle = StringIO(data)
    people = read_from_file(file_handle)
    assert len(people) == 1
    assert people[0].id() == 'id1'


# def test_read_missing_column_in_row():
#     data = 'id,name,sex,birth_date\nid1,name1Female,1/1/2000\n'
#     file_handle = StringIO(data)
#     with pytest.raises(MalformedPersonDataError):
#         read_from_file(file_handle)


# def test_read_from_file():
#     read_from_file('people.txt')

# def test_read_from_file_not_exist():
#     read_from_file('nonexist')

# def test_read_from_file_directory():
#     read_from_file('/')

# def test_read_and_write():
#     with open('people.txt', 'r') as people_txt:
#         people = read_from_file(people_txt)
#     with open('people_saved.txt', 'w') as people_saved:
#         write_to_file(people_saved, people)
