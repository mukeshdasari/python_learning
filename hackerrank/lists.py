if __name__ == '__main__':
    N = int(input())
    M = N
    lst = list()
    command = list()
    while(N!=0):
        command.append(raw_input())
        N = N-1

    while(M != 0):
        step = input()
        num = step.split(' ')
        if 'insert' in step:
            lst.insert(int(num[1]), int(num[2]))
        elif 'print' in step:
            print(lst)
        elif 'remove' in step:  
            lst.remove(int(num[1]))
        elif 'append' in step:
            lst.append(int(num[1]))
        elif 'sort' in step:
            lst.sort()
        elif 'pop' in step:
            lst.pop()
        elif 'reverse' in step:
            lst.reverse()
        M =  M-1
        