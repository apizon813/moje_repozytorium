from model import Person


def read_from_file(file_handle):
    # 1. open file for reading
    # 2. read data from file
    # 3. create Person instances based on the data
    # 4. store into a list and return list
    people = []
    file_handle.readline()
    for line in file_handle:
        # line = line[:-1]
        line = line.rstrip()
        tokens = line.split(',')
        id, name, sex, birth_date = tokens
        person = Person(id, name, sex, birth_date)
        people.append(person)
    return people

def  write_to_file(file_handle, people):
    file_handle.write('id,name,sex,birth_date\n')
    for person in people:
        id = person.id()
        name = person.name()
        sex = person.sex()
        birth_date = person.birth_date()
        line = f'{id},{name},{sex},{birth_date}\n'
        file_handle.write(line)