if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    list1 = []
    # Found below result
    # lis = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]

    for num1 in range(x+1):
        for num2 in range(y+1):
            for num3 in range(z+1):
                if(num1+num2+num3 != n):
                    list1.append([num1, num2, num3])

    print(list1)
