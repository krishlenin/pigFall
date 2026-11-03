import random

def roll():
    return random.randint(1,6)

def pigTurn(target = 20):
    turnTotal = 0
    rolledOne = False
    while turnTotal < target and not rolledONe:
        dice = roll()
        print("Roll:", dice)
        if dice == 1:
            turnTotal = 0
            rolledOne = True
        else:
            turnTotal += dice
    return turnTotal

def holdAtX(trials, target = 20):
    results = {0:0}
    for i in range(6):
        results[target + i] = 0
    for _ in range(trials):
        turnTotal = pigTurn(target)
        results[turnTotal] += 1
    print("Turn Total\t\tEstimated Prob")
    for turnTotal in results:
        print(turnTotal, results[turnTotal]/trials, sep="\t\t")
