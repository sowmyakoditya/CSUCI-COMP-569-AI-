# Team members Yashwanth Sai Tirukkovalluru, Sandipta Khare, Sowmya Kodityala 
l =[1,2,5,2]
# verified test_cases [1,2,5,-2], [0,2,5,0], [-1,-2,-5,-2]

def max_player(l, score):
    if len(l) == 0:
        return score 
    lft = min_player(l[1:], score + l[0])
    rt = min_player(l[:-1], score + l[-1])
    print(l, 'left', lft)
    print(l, 'right', rt)
    return max(lft, rt)

def min_player(l, score):
    if len(l) == 0:
        return score 
    lft = max_player(l[1:], score - l[0])
    rt = max_player(l[:-1], score - l[-1])
    print(l, 'left', lft)
    print(l, 'right', rt)
    return max(lft, rt)

def minmax_(lst):
    return max_player(lst, 0) > 0
print(minmax_(l))
