# 2018-01-part A

with open('a.txt', 'r') as f:
    input = [int(_) for _ in f.read().splitlines()]

print(f'part a = {sum(input)}')

i = 0
running = 0
LEN_INPUT = len(input)
seen = set([0])
while True:
    running += input[i % LEN_INPUT]
    if running in seen:
        print(f'part b = {running}')
        break
    seen.add(running)
    i += 1
