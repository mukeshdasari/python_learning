import string


def print_rangoli(size):
    temp_len = (2*size)-1
    temp = ['' for _ in range(temp_len)]
    alpha = string.ascii_lowercase
    for x in range(0, size):
        pattern = '-'.join(alpha[x:size])
        if (size+x-1 <= temp_len):
            temp[size+x-1] = ('-'*(2*x))+pattern[::-1]+pattern[1:]+('-'*(2*x))
        temp[size-x-1] = ('-'*(2*x))+pattern[::-1]+pattern[1:]+('-'*(2*x))

    print('\n'.join(temp))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
