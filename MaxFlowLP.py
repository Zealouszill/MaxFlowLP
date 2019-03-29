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


    # lp('objective', )

    f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et = vars \
        ('f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et')

    maxConstraint = 0

    for i in adjacencyList:
        for j in range(len(adjacencyList[i])):
            if adjacencyList[i][j][0] == startNode:
                maxConstraint = maxConstraint + adjacencyList[i][j][2]

    print("Max Constraint is:", f_sa + f_sb + f_sc)

    print("The result is:*****************************************")

    returnedListOfConstraints, totalFlow, edgeDictionary = lp('max', f_sa + f_sb + f_sc, [f_sa >= 0, f_sb >= 0, f_sc >= 0,
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
    print("returnedListOfConstraints", returnedListOfConstraints)

    # The max value that can be outputed.
    print("totalFlow", totalFlow)

    # Flow used for each of the tubes.
    print("edgeDictionary", edgeDictionary)





    listOfVariables = []

    for i in adjacencyList:
        for j in range(len(adjacencyList[i])):
            listOfVariables.append(adjacencyList[i][j][2])

    tempConstraint = 0
    constraints = []

    for i in adjacencyList:
        for j in range(len(adjacencyList[i])):

            tempConstraint = tempConstraint + adjacencyList[i][j][2]
            # print("tc", tempConstraint)

        constraints.append(tempConstraint)
        tempConstraint = 0


    for i in constraints:
        pass # print(constraints)

    return edgeDictionar, totalFlow

def test_MaxFlowFunction():

    adjacencyList = test_adjacencyListCreation()

    startNode = "s"
    endNode = "t"

    dictionaryEdge, totalFlow = MaxFlow(adjacencyList, startNode, endNode)



def test_adjacencyListCreation():

    adjacencyList = defaultdict(list)

    adjacencyList[0].extend([["a", "d", 2]])
    adjacencyList[1].extend([["b", "a", 10],["b", "d", 1]])
    adjacencyList[2].extend([["c", "e", 5]])
    adjacencyList[3].extend([["d", "t", 2],["d", "e", 1],["d", "c", 1]])
    adjacencyList[4].extend([["e", "t", 5]])
    adjacencyList[5].extend([["s", "a", 3], ["s", "b", 3], ["s", "c", 4]])


    assert adjacencyList[0][0][0] == "a"
    assert adjacencyList[0][0][1] == "d"
    assert adjacencyList[0][0][2] == 2

    assert adjacencyList[1][0][0] == "b"
    assert adjacencyList[1][0][1] == "a"
    assert adjacencyList[1][0][2] == 10
    assert adjacencyList[1][0][0] == "b"
    assert adjacencyList[1][1][1] == "d"
    assert adjacencyList[1][1][2] == 1

    assert adjacencyList[2][0][0] == "c"
    assert adjacencyList[2][0][1] == "e"
    assert adjacencyList[2][0][2] == 5

    assert adjacencyList[3][0][0] == "d"
    assert adjacencyList[3][0][1] == "t"
    assert adjacencyList[3][0][2] == 2
    assert adjacencyList[3][0][0] == "d"
    assert adjacencyList[3][1][1] == "e"
    assert adjacencyList[3][1][2] == 1
    assert adjacencyList[3][0][0] == "d"
    assert adjacencyList[3][2][1] == "c"
    assert adjacencyList[3][2][2] == 1

    assert adjacencyList[4][0][0] == "e"
    assert adjacencyList[4][0][1] == "t"
    assert adjacencyList[4][0][2] == 5

    assert adjacencyList[5][0][0] == "s"
    assert adjacencyList[5][0][1] == "a"
    assert adjacencyList[5][0][2] == 3
    assert adjacencyList[5][0][0] == "s"
    assert adjacencyList[5][1][1] == "b"
    assert adjacencyList[5][1][2] == 3
    assert adjacencyList[5][0][0] == "s"
    assert adjacencyList[5][2][1] == "c"
    assert adjacencyList[5][2][2] == 4

    return adjacencyList
