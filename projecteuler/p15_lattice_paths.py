"""

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

"""
class Node(object):
    def __init__(self, x, y, visited):
        self.x = x
        self.y = y
        self.visited = visited

gridSize = int(raw_input("How many nodes high is the grid?: "))
startNode = Node(0,0, False)
finalNode = Node(gridSize-1, gridSize-1, False)
grid = []
adjacentNodes = []
pathway = []
count = []

for x in range(0,gridSize):
    for y in range(0,gridSize):
        grid.append(Node(x,y, False))

def isInGrid(passedNode):
    for node in grid:
        if node.x == passedNode.x and node.y == passedNode.y:
            return True
    return False

def adjacentNodes(currentNode):
    returnList = []
    rightNode = Node(currentNode.x, currentNode.y + 1, False)
    downNode = Node(currentNode.x + 1, currentNode.y, False)
    if isInGrid(rightNode):
        returnList.append(rightNode)
    if isInGrid(downNode):
        returnList.append(downNode)
    return returnList

def findPath(currentNode):
    #print currentNode.x,currentNode.y
    if currentNode.x == finalNode.x and currentNode.y == finalNode.y:
#        for Node in pathway:
#            print Node.x, Node.y
        
#        print "Found a path above me!"
        count.append(pathway)
#        print len(count)
    else:
        currentNode.visited = True
        pathway.append(currentNode)
        for adjacentNode in adjacentNodes(currentNode):
            if adjacentNode.visited == False:
                findPath(adjacentNode)
                currentNode.visited = False
                if len(pathway) != 0:
                    #print "I'm popping this node: ", currentNode.x, currentNode.y
                    pathway.pop()

findPath(startNode)

print len(count)
        
"""
node targetNode
stack path
bool visited
findpath(currentNode){
    if(currentNode == targetNode)
         print all elements in path
else:
     visited[currentNode] = true
     path.push(currentNode)
 
for all 'adjacentNode' adjacent to currentNode:
    if(visited[adjacentNode] == false)
        findpath(adjacentNode)
        visited[currentNode] = false
        path.pop()
                                  
"""





"""



def getPaths(currentPoint, grid, count):
    if currentPoint.x == 20 and currentPoint.y ==20:
        return count
    if currentPoint.x == 20:
        currentPoint.y += 1
        count += 1
        return getPaths(currentPoint, grid, count)




x x x x     x x x .     x x x .     x x x .     x x . .     x x . .     x x . .     x x . .     x x . .     x x . .     x . . .     x . . .     x . . .     x . . .     x . . .  

. . . x     . . x x     . . x .     . . x .     . x x x     . x x .     . x x .     . x . .     . x . .     . x . .     x x x x     x x x .     x x x .     x x . .     x x . .

. . . x     . . . x     . . x x     . . x .     . . . x     . . x x     . . x .     . x x x     . x x .     . x . .     . . . x     . . x x     . . x .     . x x x     . x x .

. . . x     . . . x     . . . x     . . x x     . . . x     . . . x     . . x x     . . . x     . . x x     . x x x     . . . x     . . . x     . . x x     . . . x     . . x x
  
   1           2           3           4           5           6          7            8           9           10         11          12          13           14          15


x . . .     x . . .     x . . .     x . . .     x . . .

x x . .     x . . .     x . . .     x . . .     x . . .

. x . .     x x x x     x x x .     x x . .     x . . .

. x x x     . . . x     . . x x     . x x x     x x x x

  16           17          18          19          20



x | y
-----
1 | 0
2 | 2
3 | 6
4 | 20


go right all the way
go down all the way
add one




"""

