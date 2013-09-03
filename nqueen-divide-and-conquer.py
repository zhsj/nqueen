queen_list = {
    0: [],          
    1: [0],
    4: [1, 3, 0, 2],
    5: [0, 2, 4, 1, 3],
    6: [1, 3, 5, 0, 2, 4],
    7: [0, 2, 4, 6, 1, 3, 5],
    8: [0, 4, 7, 5, 2, 6, 1, 3],
    9: [0, 2, 5, 7, 1, 3, 8, 6, 4],
    10: [0, 2, 5, 7, 9, 4, 8, 1, 3, 6],
    11: [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9],
    12: [0, 2, 4, 7, 9, 11, 5, 10, 1, 6, 8, 3],
    13: [0, 2, 4, 1, 8, 11, 9, 12, 3, 5, 7, 10, 6],
    14: [0, 2, 4, 6, 11, 9, 12, 3, 13, 8, 1, 5, 7, 10],
    15: [0, 2, 4, 1, 9, 11, 13, 3, 12, 8, 5, 14, 6, 10, 7],
    26: [0, 2, 4, 1, 3, 8, 10, 12, 14, 20, 22, 24, 19, 21, 23, 25, 9, 6, 15, 11, 7, 5, 17, 13, 18, 16],
    27: [0, 2, 4, 1, 3, 8, 10, 12, 14, 16, 18, 22, 24, 26, 23, 25, 5, 9, 6, 15, 7, 11, 13, 20, 17, 19, 21]
}

def divideConquer(n):
    global queen_list
    flag = 0
    if n & 1 == 0:
        n += 1
        flag = 1
        
    if n%3:
        return
    
    if n in [8,9,14,15,26,27,38,39]:
        return
    
    global queen_list
    c = 5
    while True:
        if (n-c)%4:
            c+=2
        else:
            b = (n-c)/4
            if c%3 and b%3:
                break

    
    temp = []
    if not queen_list.has_key(b):
        divideConquer(b)
    if not queen_list.has_key(c):
        divideConquer(c)
    
    for item in queen_list[5]:
        temp += [i+ b * item for i in queen_list[b]]
    
    temp = temp[b-c:]
    
    for i in range(b-c):
        try:
            temp.remove(i)
        except:
            pass
    temp = [i - b + c for i in temp]
    temp = queen_list[c] + temp
    
    if flag:
        n = n-1
        
    queen_list.update({n:temp})
    return

def main():
    global queen_list
    n = input()
    divideConquer(n)
    print queen_list[n]
    
if __name__ == "__main__":
    main()
