from texts import text3

def three_big_guards(string):
    output = ''
    if string[:3].isupper() and string[3].islower() and string[4:7].isupper() and string[7].islower():
        output += string[3]
    for index, _ in enumerate(string[:-8]):
        if string[index].islower() and string[index+1:index+4].isupper() and string[index+4].islower() and string[index+5:index+8].isupper() and string[index+8].islower():
            output += string[index+4]
    return output




if __name__ == '__main__':
    text0 = 'ABCdaFGH'
    print(three_big_guards(text3))