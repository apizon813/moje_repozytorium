def read_from_file(path):
    # 1. open file for reading
    # 2. read data from file
    # 3. create Person instances based on the data
    # 4. store into a list and return list
    with open(path, 'r') as file_handle:
        file_handle.readline()
        for line in file_handle:
            line = line[:-1]
            pass

def  write_to_file(path, people):
    pass