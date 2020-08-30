
competitors = {}.fromkeys(range(1, int(input()) + 1), 0)

print (competitors)


for election in map(int, input().split()):
    try:
        competitors[election] += 1
    except KeyError:
        pass
        
win_res = max(competitors.values())
print(*filter(lambda x: competitors[x] == win_res, competitors))
