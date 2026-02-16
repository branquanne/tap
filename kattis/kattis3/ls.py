in_string = input().strip()
n = int(input().strip())

parts = in_string.split("*")
start = not in_string.startswith("*")
end = not in_string.endswith("*")
for _ in range(n):
    curr_file = input().strip()
    i = 0
    ok = True

    for j, part in enumerate(parts):
        if part:
            k = curr_file.find(part, i)
            if k < 0 or (j == 0 and start and k != 0):
                ok = False
                break
            i = k + len(part)

    if ok and (not end or curr_file.endswith(parts[-1])):
        print(curr_file)
