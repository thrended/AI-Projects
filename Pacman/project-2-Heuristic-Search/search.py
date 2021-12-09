# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Every path in a set of actions: next node, direction, and cost.

    Variable path is used to maintain visited vertices, and is a list to
    ensure no errors like "TypeError: unhashable type: 'list'"

    problem.getStartState() is set of coordinates on the x and y axis.
    problem.isGoalState(problem.getStartState()) is a boolean to check if
    the current state is the goal.
    problem.getSuccessors(problem.getStartState()) is a set of next node,
    direction, and cost.

    Implementation returns a list of actions that reaches the goal.
    """
    stack_util = util.Stack()
    path = []
    stack_util.push((problem.getStartState(), [], 1))

    while stack_util:
        next_node, direction, cost = stack_util.pop()    # unpacks problem.getStartState() to next_node

        if next_node in path:
            continue

        path.append(next_node)

        if problem.isGoalState(next_node):
            return direction

        for state, action, cost in problem.getSuccessors(next_node):
            stack_util.push((state, direction+[action], cost))
    return path


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.

    Similar to the above implementation of DFS but a queue is used instead
    of a stack.
    """
    queue_util = util.Queue()
    path = []
    queue_util.push((problem.getStartState(), [], 1))

    while not queue_util.isEmpty():
        next_node, direction, cost = queue_util.pop()

        if next_node in path:
            continue

        path.append(next_node)

        if problem.isGoalState(next_node):
            return direction

        for state, action, cost in problem.getSuccessors(next_node):
            queue_util.push((state, direction+[action], cost))
    return path


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.

    Similar to the above implementation of BFS but a priority queue is used
    instead of a queue.
    """
    priority_queue_util = util.PriorityQueue()
    path = []
    priority_queue_util.push((problem.getStartState(), [], 1), 0)

    while priority_queue_util:
        next_node, direction, cost = priority_queue_util.pop()

        if next_node in path:
            continue

        path.append(next_node)

        if problem.isGoalState(next_node):
            return direction

        for state, action, cost in problem.getSuccessors(next_node):
            priority_queue_util.push((state, direction+[action], cost), \
            problem.getCostOfActions(direction+[action]))
    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    priority_queue_util = util.PriorityQueue()
    path = []
    priority_queue_util.push((problem.getStartState(), [], 1), 0)

    while priority_queue_util:
        next_node, direction, cost = priority_queue_util.pop()

        if next_node in path:
            continue

        path.append(next_node)

        if problem.isGoalState(next_node):
            return direction

        for state, action, cost in problem.getSuccessors(next_node):
            priority_queue_util.push((state, direction+[action], cost), \
            problem.getCostOfActions(direction+[action]) + heuristic(state, problem))
    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
