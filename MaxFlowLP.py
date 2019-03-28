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



    f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et = vars\
        ('f_sa, f_sb, f_sc, f_ad, f_ba, f_bd, f_ce, f_dc, f_de, f_dt, f_et')


    upperBound, lowerBound = vars('upperBound, lowerBound')

    tempConstraint = 0
    constraints = []

    for i in adjacencyList:
        for j in range(len(adjacencyList[i])):
            print("iteration")
            print("i", i)
            print("j", j)

            tempConstraint = tempConstraint + adjacencyList[i][j][1]
            print("tc", tempConstraint)

        constraints.append(tempConstraint)
        tempConstraint = 0

    # lp('objective', )

    for i in constraints:
        print(constraints)

    return edgeDictionary, totalFlow

def test_MaxFlowFunction():

    adjacencyList = test_adjacencyListCreation()

    startNode = "s"
    endNode = "t"

    dictionaryEdge, totalFlow = MaxFlow(adjacencyList, startNode, endNode)



def test_adjacencyListCreation():

    adjacencyList = defaultdict(list)

    adjacencyList[0].extend([["d", 2]])
    adjacencyList[1].extend([["a", 10],["d", 1]])
    adjacencyList[2].extend([["e", 5]])
    adjacencyList[3].extend([["t", 2],["e", 1],["c", 1]])
    adjacencyList[4].extend([["t", 5]])
    adjacencyList[5].extend([["a", 3], ["b", 3], ["c", 4]])



    assert adjacencyList[0][0][0] == "d"
    assert adjacencyList[0][0][1] == 2

    assert adjacencyList[1][0][0] == "a"
    assert adjacencyList[1][0][1] == 10
    assert adjacencyList[1][1][0] == "d"
    assert adjacencyList[1][1][1] == 1

    assert adjacencyList[2][0][0] == "e"
    assert adjacencyList[2][0][1] == 5

    assert adjacencyList[3][0][0] == "t"
    assert adjacencyList[3][0][1] == 2
    assert adjacencyList[3][1][0] == "e"
    assert adjacencyList[3][1][1] == 1
    assert adjacencyList[3][2][0] == "c"
    assert adjacencyList[3][2][1] == 1

    assert adjacencyList[4][0][0] == "t"
    assert adjacencyList[4][0][1] == 5

    assert adjacencyList[5][0][0] == "a"
    assert adjacencyList[5][0][1] == 3
    assert adjacencyList[5][1][0] == "b"
    assert adjacencyList[5][1][1] == 3
    assert adjacencyList[5][2][0] == "c"
    assert adjacencyList[5][2][1] == 4

    return adjacencyList
