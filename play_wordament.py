from nltk.corpus import wordnet

matrix = []

def fillMatrix (matrix):
    for row in matrix:
        for i in range(4):
            row[i] = raw_input()

def initMatrix (matrix):
    for i in range(4):
        row = []
        for j in range(4):
            row.append(None);
        matrix.append(row)

def printMatrix (matrix):
    for i in range(4):
        for j in range(4):
            print matrix[i][j]
        print "\n"

def adjacent (x, y):
    adj = []
    for i in range (x-1,x+2):
        for j in range (y-1, y+2):
            if (i>=0 and i<4 ) and (j>=0 and j<4 ) and not(i ==x and j ==y) :
                adj.append ((i,j))
    return adj

def wordsAdjacentTo( x, y, length, matrix):
    
    words = []
    
    adj = []
    adj.append ((x,y))

    for node2 in adjacent(x, y):
       adj.append (node2)
       xx,yy = node2
       for node3 in adjacent(xx, yy):
           if node3 != (x, y) :
                word = matrix[x][y] + matrix[xx][yy] + matrix[node3[0]][node3[1]]
                if word not in words:
                    words.append (word)
    return words

'''
def wordsAdjacentTo4 (x,y,matrix):
    words = []
    adj.append ((x,y))
    for node2 in adjacent(x, y):
        adj.append (node2)
        x2,y2 = node2
        for node3 in adjacent (x2, y2):
            if node3 not in adj:
                x3, y3 = node3
                for node4 in adjacent (x3, y3):
                    if node4 not in adj:
                        word = matrix[x][y] + matrix[xx][yy] + matrix[x3][y3]; # INCOMPLETE


'''


'''
matrix = [['a','b','c','d'],\
          ['e','f','g','h'],\
          ['i','j','k','l'],\
          ['m','n','o','p']]
'''
initMatrix (matrix)
#printMatrix (matrix)
fillMatrix (matrix)
#printMatrix (matrix)

for i in range(4):
    for j in range (4):
        words = wordsAdjacentTo (i,j,3,matrix)
        for word in words:
            if  wordnet.synsets(word):
                print word
'''

while (1) :

    if not wordnet.synsets(word):
        print ("NOT FOUND")
    else:
        print ("FOUND")
'''
