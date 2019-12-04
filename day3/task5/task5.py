import csv

grid = open('input5', 'r')
reader = csv.reader(grid, delimiter=',')

cable1 = reader.__next__()
cable2 = reader.__next__()

# list of all horizontal vectors of cable1 as tuples: (y, x1, x2)
cable1_h_vectors = []

# list of all vertical vectors of cable1 as tuples: (x, y1, y2)
cable2_v_vectors = []


def vectorize(cable):
    currX = 0
    currY = 0

    h_vectors = []
    v_vectors = []

    for c in cable:
        if c[0] == 'U':
            nextY = currY+int(c[1:])
            v_vectors.append((currX, currY, nextY))
            currY = nextY
        elif c[0] == 'D':
            nextY = currY-int(c[1:])
            v_vectors.append((currX, currY, nextY))
            currY = nextY
        elif c[0] == 'R':
            nextX = currX+int(c[1:])
            h_vectors.append((currY, currX, nextX))
            currX = nextX
        else:
            nextX = currX-int(c[1:])
            h_vectors.append((currY, currX, nextX))
            currX = nextX

    return (h_vectors, v_vectors)

# find where the cables cross (do the cables overlay lenghtwise?)
def find_crosspoints(horizontal_vectors, vertical_vectors):
    crosspoints = []

    for hy, hx1, hx2 in horizontal_vectors:
        for vx, vy1, vy2 in vertical_vectors:

            # make sure bigger y comes first
            if vy1 < vy2:
                vy1, vy2 = vy2, vy1 # swap

            # check if they cross on y axis
            if hy < (vy1+1) and hy > (vy2-1):

                # make sure smaller x comes first
                if hx1 > hx2:
                    hx1, hx2 = hx2, hx1 # swap

                # check if they cross on x axis
                if vx > (hx1-1) and vx < (hx2+1):
                    crosspoints.append((vx, hy))

    return crosspoints


c1h_vectors, c1v_vectors = vectorize(cable1)
c2h_vectors, c2v_vectors = vectorize(cable2)

print("hor:", c1h_vectors, "\n ver:" ,c2v_vectors, "\n\n\n")
print("hor:", c2h_vectors, "\n ver:" ,c1v_vectors, "\n\n\n")


crosspoints = []

crosspoints += find_crosspoints(c1h_vectors, c2v_vectors)
crosspoints += find_crosspoints(c2h_vectors, c1v_vectors)

print(crosspoints)

# # find crosspoint with shortest distance to origin
shortest_distance = abs(crosspoints[1][0]) + abs(crosspoints[1][1])
for x, y in crosspoints[2:]:
    if abs(x) + abs(y) < shortest_distance and x+y != 0:
        shortest_distance = abs(x) + abs(y)
        print("distance:", shortest_distance, "coords:", x, y)

print(shortest_distance)
