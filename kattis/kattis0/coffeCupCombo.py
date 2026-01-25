# Jonna is a university student who attends  lectures every day. Since most lectures are way too simple for an algorithmic expert such as Jonna, she can only stay awake during a lecture if she is drinking coffee. During a single lecture she needs to drink exactly one cup of coffee to stay awake.
# Some of the lecture halls have coffee machines, so Jonna can always make sure to get coffee there. Furthermore, when Jonna leaves a lecture hall, she can bring at most two coffee cups with her to the following lectures (one cup in each hand). But note that she cannot bring more than two coffee cups with her at any given time.
# Given which of Jonna’s lectures have coffee machines, compute the maximum number of lectures during which Jonna can stay awake.
# Input
# The first line contains the integers  (), the number of lectures Jonna attends.
# The second line contains a string  of length . The ’th letter is 1 if there is a coffee machine in the ’th lecture hall, and otherwise it is 0.
# Output
# Print one integer, the maximum number of lectures during which Jonna can stay awake.

n = int(input().strip())
s = input().strip()

answer = 0
cups = 0

for i in range(n):
    if s[i] == "1":
        cups = 2
        answer += 1
    if s[i] == "0" and cups > 0:
        cups -= 1
        answer += 1

    if s[i] == "0" and cups < 1:
        pass
print(answer)
