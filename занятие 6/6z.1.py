#У меня 7 вариант задания
line = input()
line = line[:int((len(line) + 1) / 2)]
res = ""
for i in line:
    if i == "п":
        res += "*"
    else:
        res += i
print(res)