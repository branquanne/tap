import string

n = int(input().strip())
results = []

for _ in range(n):
    temp = input().strip().lower()
    alphabet = set(string.ascii_lowercase)
    found = set(temp)
    missing = sorted(alphabet - found)
    if not missing:
        results.append("pangram")
    else:
        results.append("missing " + "".join(missing))

for result in results:
    print(result)
