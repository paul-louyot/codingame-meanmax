import sys
import math

class Unit:
    def __init__(self, unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2):
        self.x=x
        self.y=y
        self.unit_id=unit_id
        self.unit_type=unit_type
        self.vx = vx
        self.vy = vy


def dist(u,v):
    """u and v are from the Unit class"""
    return math.sqrt((u.y-v.y)**2 + (u.x-v.x)**2)

def findClosestWreck(dictWreck,aUnit): #returns a wreck (actually Unit) object
    """dictWreck is a dictionnary with all the current Wrecks.
    Returns the current Wreck Unit which is the closest to the r Unit"""
    wreckList = [dictWreck[w] for w in dictWreck]
    distList = [dist(dictWreck[w],aUnit) for w in dictWreck]
    closestWreck = wreckList[distList.index(min(distList))]
    return closestWreck

def findClosestTanker(dictTanker, aUnit):
    """dictWreck is a dictionnary with all the current Tankers.
    Returns the current Tanker Unit which is the closest to the r Unit"""
    tankerList = [dictTanker[w] for w in dictTanker]
    distList = [dist(dictTanker[w], aUnit) for w in dictTanker]
    closestTanker = tankerList[distList.index(min(distList))]
    return closestTanker

def findUnitsInRadius(unitsList, aUnit, radius):
    return [u for u in unitsList if dist(u, aUnit) <= radius]

def higherTargetValue(target1, target2):
    if target1.unit_type == 0 and target2.unit_type == 0:
        return (target2,target1)[target1.ownerScore >= target2.ownerScore]
    elif target1.unit_type == 0:
        return target1
    elif target2.unit_type == 0:
        return target2
    elif target1.unit_type == 2 and target2.unit_type == 2:
        return (target2,target1)[target1.ownerScore >= target2.ownerScore]
    elif target1.unit_type == 2:
        return target1
    elif target2.unit_type == 2:
        return target2
    else:
        return target1

def playReaper(dictWreck, myReaper, myDestroyer):
    """fonction définissant le comportement du Reaper"""
    if len(dictWreck) == 0:
        X = myDestroyer.x
        Y = myDestroyer.y
        throttle = 150
        print(str(X) + " " + str(Y) + " " +str(throttle))
    else:
        closestWreck = findClosestWreck(dictWreck, myDestroyer)
        X = closestWreck.x
        Y = closestWreck.y
        d=dist(closestWreck, myReaper)
        if d>300:
            throttle=300
        else:
            throttle=int(d)
        printOutput(str(X),str(Y),str(throttle))

def playDestroyer(myDestroyer, listOpponents, my_rage):
    opponentsInRadius = findUnitsInRadius(listOpponents, myDestroyer, 1900)
    print('opp close to destroyer :',len(opponentsInRadius), file = sys.stderr)
    if my_rage >= 60 and len(opponentsInRadius) > 0:
        deltaT = 1
        bestTarget = listOpponents[0]
        for o in listOpponents:
            bestTarget = higherTargetValue(bestTarget,o)
        [targetX, targetY] = [bestTarget.x + deltaT*bestTarget.vx, bestTarget.y + deltaT*bestTarget.vy]
        printOutput('SKILL', str(targetX), str(targetY))
    else:
        if len(dictTanker) == 0:
            print("WAIT")
        else:
            X = findClosestTanker(dictTanker,myDestroyer).x
            Y = findClosestTanker(dictTanker,myDestroyer).y
            printOutput(str(X), str(Y), str(300))

def playDoof(myDoof):
    if myDoof.vx == 0 and myDoof.vy == 0:
        X = 0
        Y = 2999
    else:
        deltaT = 10
        X = myDoof.x + deltaT*myDoof.vx
        Y = myDoof.y + deltaT*myDoof.vy
    printOutput(str(X), str(Y), str(300))


def formatOutput(str1, str2, str3):
    return(str1+" "+str2+" "+str3)

def printOutput(str1,str2,str3):
    print(str1+" "+str2+" "+str3)

def printWait():
    print("WAIT")
    print("WAIT")
    print("WAIT")

# game loop

while True:

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    #print(unit_count,file=sys.stderr)
    scoreList = [my_score, enemy_score_1, enemy_score_2]
    dict = {}
    dictWreck = {}
    dictTanker = {}

    for i in range(unit_count):
        unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2 = input().split()
        unit_id = int(unit_id)
        unit_type = int(unit_type)
        player = int(player)
        mass = float(mass)
        radius = int(radius)
        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        extra = int(extra)
        extra_2 = int(extra_2)
        dict[unit_id] = Unit(unit_id, unit_type, player, mass, radius, x, y, vx, vy, extra, extra_2)
        if (player in [0,1,2]):
            dict[unit_id].ownerScore = scoreList[player]
        else:
            dict[unit_id].ownerScore = -42

        # Wreck Dict
        if(unit_type == 4):
            dictWreck.update({unit_id:dict[unit_id]})

        # Tanker Dict
        if(unit_type == 3):
            dictTanker.update({unit_id:dict[unit_id]})

        # parse Units
        if (player == 0):
            if unit_type == 0:
                myReaper = dict[unit_id]
            if unit_type == 1:
                myDestroyer = dict[unit_id]
            if unit_type == 2:
                myDoof = dict[unit_id]

        if player == 1:
            if unit_type == 0:
                Reaper1 = dict[unit_id]
            if unit_type == 1:
                Destroyer1 = dict[unit_id]
            if unit_type == 2:
                Doof1 = dict[unit_id]

        if player == 2:
            if unit_type == 0:
                Reaper2 = dict[unit_id]
            if unit_type == 1:
                Destroyer2 = dict[unit_id]
            if unit_type == 2:
                Doof2 = dict[unit_id]

		# fin du for sur les Units

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # where are targets
    print("Reaper 1 :", Reaper1.x, Reaper1.y, file = sys.stderr)
    print("Reaper 2 :", Reaper2.x, Reaper2.y, file = sys.stderr)

    listOpponents = [Reaper1, Reaper2, Destroyer1, Destroyer2]

    playReaper(dictWreck, myReaper, myDestroyer)

    playDestroyer(myDestroyer, listOpponents, my_rage)

    playDoof(myDoof)
