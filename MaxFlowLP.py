"""

Initial Setup

"""

from collections import defaultdict
from pulp import LpProblem, LpMinimize, LpMaximize, LpVariable


def vars(s, low=None, high=None):
    """example creates three variables bounded from 0 to 10:
    a, b, c = vars('a,b,c', 0, 10)
    """
    return tuple(LpVariable(v.strip(), low, high) for v in s.split(','))



def lp(mode, objective, constraints):
    """see lp1 below for an example"""

    if mode.lower() == 'max':
        mode = LpMaximize
    elif mode.lower() == 'min':
        mode = LpMinimize
    prob = LpProblem("", mode)
    prob += objective
    for c in constraints:
        prob += c
    prob.solve()
    return prob, prob.objective.value(), dict((v.name, v.value()) for v in prob.variables())


def MaxFlow(adjacencyList, startNode, endNode):

    # x_1, x_2 = vars('x_1, x_2')
    #
    # lp('max', x_1 + 6 * x_2, [
    #     x_1 >= 0,
    #     x_2 >= 0,
    #     x_1 <= 200,
    #     x_2 <= 300,
    #     x_1 + x_2 <= 400])

    # Constrains:
    # upperbound = all the edges added together.
    # lowerbound is that they have to be greater than 0.
    # Each node can only take in so much. (Capacity)
    # Constraint of f_sc + f_dc = f_ce. The flow can't be greater going from two nodes into the
    # output of the third node.

    listOfVariablesTemp = []
    listOfVariables = {}
    constraints = []
    inWeight = defaultdict(list)
    outWeight = defaultdict(list)

    # tempInWeight = 0
    # tempOutWeight = 0

    # for i in adjacencyList:
    #     for j in range(len(adjacencyList[i])):
    #         if adjacencyList[i][j][0] == startNode:
    #             maxConstraint = maxConstraint + adjacencyList[i][j][2]

    for i in adjacencyList:
        for j in range(len(adjacencyList[i])):
            pass
            # listOfVariablesTemp.append(
            #     LpVariable(("f_" + adjacencyList[i][j][0] + adjacencyList[i][j][1]), 0, adjacencyList[i][j][2]))

    for (i, j) in adjacencyList:
        print(adjacencyList[i,j][0])
        listOfVariables[i,j] = LpVariable("f_" + i + j, 0, adjacencyList[i,j][0])

        # inWeight[j].add(i)
        # outWeight[i].add(j)

    print("inweight", inWeight)
    print("outweight", outWeight)


    # constraints.append()

    print("A list", listOfVariablesTemp)



    # temp = listOfVariablesTemp[0] + 1

    # for i in listOfVariablesTemp:
    #     listOfVariables[0].extend(vars(listOfVariablesTemp[i]))

    print("A list", listOfVariables)




    # for i in adjacencyList:
    #     for j in range(len(adjacencyList[i])):
    #         listOfVariables.append(adjacencyList[i][j][2])
    #
    # tempConstraint = 0
    #
    #
    # for i in adjacencyList:
    #     for j in range(len(adjacencyList[i])):
    #
    #         tempConstraint = tempConstraint + adjacencyList[i][j][2]
    #         # print("tc", tempConstraint)
    #
    #     constraints.append(tempConstraint)
    #     tempConstraint = 0
    #
    #
    # for i in constraints:
    #     pass # print(constraints)

    print("The result is:*****************************************")

    f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et = vars \
        ('f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et')

    print("Max Constraint is:", f_sa + f_sb + f_sc)

    returnedListOfConstraints, totalFlow, edgeDictionary = lp('max', f_sa + f_sb + f_sc,
                                                              [f_sa >= 0, f_sb >= 0, f_sc >= 0,
                                                               f_ad >= 0, f_ba >= 0, f_bd >= 0,
                                                               f_ce >= 0, f_dc >= 0, f_de >= 0,
                                                               f_dt >= 0, f_et >= 0,

                                                               f_sa <= 3, f_sb <= 3, f_sc <= 4,
                                                               f_ad <= 2, f_ba <= 10, f_bd <= 1,
                                                               f_ce <= 5, f_dc <= 1, f_de <= 1,
                                                               f_dt <= 2, f_et <= 5,

                                                               f_sa + f_ba <= f_ad,
                                                               f_sb <= f_ba + f_bd,
                                                               f_sc + f_dc <= f_ce,
                                                               f_ad + f_bd <= f_dc + f_de + f_dt,
                                                               f_de + f_ce <= f_et])

    # All the details of the variabels and the contraints.
    # print("returnedListOfConstraints", returnedListOfConstraints)

    # The max value that can be outputed.
    print("totalFlow", totalFlow)

    # Flow used for each of the tubes.
    print("edgeDictionary", edgeDictionary)


    return edgeDictionary, totalFlow

def test_MaxFlowFunction():

    adjacencyList = test_adjacencyListCreation()

    startNode = "s"
    endNode = "t"

    dictionaryEdge, totalFlow = MaxFlow(adjacencyList, startNode, endNode)



def test_adjacencyListCreation():

    adjacencyList = defaultdict(list)

    adjacencyList["a", "d"].extend([2])
    adjacencyList["b", "a"].extend([10])
    adjacencyList["b", "d"].extend([1])
    adjacencyList["c", "e"].extend([5])
    adjacencyList["d", "t"].extend([2])
    adjacencyList["d", "e"].extend([1])
    adjacencyList["d", "c"].extend([1])
    adjacencyList["e", "t"].extend([5])
    adjacencyList["s", "a"].extend([3])
    adjacencyList["s", "b"].extend([3])
    adjacencyList["s", "c"].extend([4])

    assert adjacencyList["a", "d"] == [2]
    assert adjacencyList["b", "a"] == [10]
    assert adjacencyList["b", "d"] == [1]
    assert adjacencyList["c", "e"] == [5]
    assert adjacencyList["d", "t"] == [2]
    assert adjacencyList["d", "e"] == [1]
    assert adjacencyList["d", "c"] == [1]
    assert adjacencyList["e", "t"] == [5]
    assert adjacencyList["s", "a"] == [3]
    assert adjacencyList["s", "b"] == [3]
    assert adjacencyList["s", "c"] == [4]

    return adjacencyList
