def num(n):
    num_str = str(n)
    if len(num_str) < 2:
        num_once = int(num_str[0])
        return num_once
    else:
        num_once = int(num_str[0])
        new_n = num_str[1:]
        return num_once + num(new_n)

print(num(12345))
