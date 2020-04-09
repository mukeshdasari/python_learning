if __name__ == '__main__':
    s = input()
    is_alnum = is_alpha = is_digit = is_lower = is_upper = False
    
    for x in range(len(s)):
        if(s[x].isdigit()): is_digit = True
        if(s[x].isalpha()): is_alpha = True
        if(s[x].islower()) : is_lower = True
        if(s[x].isupper()) : is_upper = True
    if(is_alpha and is_digit):    if(s.isalnum() or (is_alpha and is_digit)): is_alnum = True
        is_alnum = True

    print(is_alnum)
    print(is_alpha)
    print(is_digit)
    print(is_lower)
    print(is_upper)
