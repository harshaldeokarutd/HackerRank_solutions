def swap_case(test):
    test1 = ""
    for i in test:
        if i.islower():
            i = i.upper()
            test1 = test1 + i
        else:
            i = i.lower()
            test1 = test1 + i
    return test1

        
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
