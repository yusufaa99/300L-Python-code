def games(args1, args2):
    counter = [0,0,0]
    for team1, team2 in zip(scores1, scores2):
        if team1 > team2:
            counter[0] += 1
        elif team1 == team2:
            counter[1] += 1
        else:
            counter[2] += 1
    return(f"Team 1 win {counter[0]} games : Team 2 win {counter[2]} games and {counter[1]} Drows total of {sum(counter)} games")

scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 5, 5, 2, 3]

print(games(scores1, scores2))



# pair = list(zip(scores1, scores2))
# pair[0] = (5,3)
# print(pair)