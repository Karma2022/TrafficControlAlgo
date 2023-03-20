import json

def algorithm():
    with open('jamFactors.json', 'r') as f:
        roads = json.loads(f.read())

    # 4 Roads -> 1, 2, 3, 4
    # Set roadPenalty values initially for each Road
    roadPenalty = [1, 1, 1, 1]
    # jamFactor  value lies between [0,10]
    # jamFactor is obtained from HERE api, for now set a random value
    jamFactors = []
    for road in roads:
        jamFactors.append(roads[road])
    print(jamFactors)

    # total loss value
    lossValues = [0, 0, 0, 0]
    # calculate tot value for each lane
    for _ in range(0, 3):
        # Reward value of each road
        reward1 = roadPenalty[0]*jamFactors[0]  # 4  #8  #24
        reward2 = roadPenalty[1]*jamFactors[1]  # 3  #6  #18
        reward3 = roadPenalty[2]*jamFactors[2]  # 5  #10 #5
        reward4 = roadPenalty[3]*jamFactors[3]  # 7  #7  #14
        reward = [reward1, reward2, reward3, reward4]

        for road in range(0, 4):
            cost = reward[0]+reward[1]+reward[2]+reward[3]
            # lossValue[i] = (summation of cost of all roads excluding road i) - reward[i]
            # or
            # lossValue[i] = (summation of cost of all roads) - 2 * reward[i]
            lossValues[road] = cost - 2*reward[road]

        # lossValue[11,13,9,5]  - roadPenalty[2,2,2,1]
        # lossValue[15,19,11,17] - roadPenalty[6,6,1,2]
        # lossValue[13,25,51,33] -roadPenalty[1,42,2,6]

        # get the road with minimum loss value
        minLoss = min(lossValues)
        for y in range(len(lossValues)):
            if minLoss == lossValues[y]:
                minLossRoad = y
                break

        # change penalty value for selected road to default value 1 and rest based on the penalty formula
        for z in range(len(roadPenalty)):
            if z == minLossRoad:
                roadPenalty[z] = 1
            else:
                roadPenalty[z] = (roadPenalty[z]+1)*(roadPenalty[z])

        print(minLossRoad+1)
