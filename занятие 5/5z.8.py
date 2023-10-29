pred = -1
cur_rep_len = 0
max_rep_len = 0
elem = int(input())
while elem != 0:
    if pred == elem:
        cur_rep_len += 1
    else:
        pred = elem
        max_rep_len = max(max_rep_len, cur_rep_len)
        cur_rep_len = 1
    elem = int(input())
max_rep_len = max(max_rep_len, cur_rep_len)
print(max_rep_len)