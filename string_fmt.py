def print_formatted(number):
    # your code goes here
    pad_length = len(bin(number).split('b')[1])
    for num in range(1,number + 1):
        decimal = str(num).rjust(pad_length)
        octagonal = str(oct(num)).split('o')[1].rjust(pad_length)
        hexagonal = str(hex(num)).split('x')[1].rjust(pad_length).upper()
        binary = str(bin(num)).split('b')[1].rjust(pad_length)
        print(' '.join([decimal,octagonal,hexagonal,binary]))


print_formatted(17)