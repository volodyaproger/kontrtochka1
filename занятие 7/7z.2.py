spisok = list(map(int, input().split()))
max_index, min_index = spisok.index(max(spisok)), spisok.index(min(spisok))
spisok[max_index], spisok[min_index] = spisok[min_index], spisok[max_index]
print(spisok)