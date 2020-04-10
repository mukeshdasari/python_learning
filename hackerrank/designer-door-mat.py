if __name__ == '__main__':
    row, column = map(int,input().split())
    pattern1 = '-'
    pattern2 = '.|.'
    temp = [None for _ in range(row)]    
    for x in range(row):
        if x < int(row/2):
            temp[x] = (2*x)+1
            temp [row-(x+1)] = (2*x)+1
            print(((pattern1)*int((column/2)-((3*x)+1)))+((pattern2)*int(temp[x]))+((pattern1)*int((column/2)-((3*x)+1))))
        elif x == int(row/2):
            print((pattern1)*int((column/2)-3)+'WELCOME'+(pattern1)*int((column/2)-3))
        else:
            print(((pattern1)*int(((3*x)+2)-(column/2)))+((pattern2)*int(temp[x]))+((pattern1)*int(((3*x)+2)-(column/2))))
            
