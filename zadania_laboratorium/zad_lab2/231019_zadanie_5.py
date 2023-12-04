def binary_length(int_number):
    bin_number = format(int_number, 'b')
    bin_length = len(bin_number)
    return bin_length

number = int(input("Choose you number: "))

print(binary_length(number))
