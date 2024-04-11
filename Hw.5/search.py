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


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    "*** YOUR CODE HERE ***"
    # queueXY: ((x,y),[path]) #
    cola = HPQ(problem, heuristica)
    
    #Did we already win?  :o
    if problem.isGoalState(problem.getStartState()):
        return []
    
    pathFromStart = []
    visited = []
    state = (problem.getStartState(),[])

    cola.push(state, heuristic)
    
    while(True):
        #Exit condition: Fail D:
        if cola.isEmpty():
            return []

        position, pathFromStart = cola.pop()

        #State already seen?
        if position in visited:
            continue

        visited.append(position)

        #Exit condition: Goal! :D
        if problem.isGoalState(position):
            return pathFromStart

        successor = problem.getSuccessors(position)
        if successor:
            for item in successor:
                if item[0] not in visited:
                    pathFromState = pathFromStart + [item[1]]
                    state = (item[0], pathFromState)
                    cola.push(state, heuristic)


from AI_HW5.util import PriorityQueue
class HPQ(PriorityQueue):
    def  __init__(self, problem, function):
        PriorityQueue.__init__(self)
        self.function = function
        self.problem = problem
    def push(self, element, heuristic):
        PriorityQueue.push(self, element, self.function(self.problem,element,heuristic))
def heuristica(problem, state, heuristic):
    return problem.getCostOfActions(state[1]) + heuristic(state[0], problem)


# Abbreviations
astar = aStarSearch
