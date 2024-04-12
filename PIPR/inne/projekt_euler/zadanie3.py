from texts import text3


def three_big_guards(string):
    output = ''
    if string[:3].isupper():
        if string[3].islower():
            if string[4:7].isupper():
                if string[7].islower():
                    output += string[3]
    for index, _ in enumerate(string[:-8]):
        if string[index].islower():
            if string[index+1:index+4].isupper():
                if string[index+4].islower():
                    if string[index+5:index+8].isupper():
                        if string[index+8].islower():
                            output += string[index+4]
    return output


if __name__ == '__main__':
    text0 = 'ABCdaFGH'
    print(three_big_guards(text3))
