import csv

grid = open('input5', 'r')
reader = csv.reader(grid, delimiter=',')

cable1 = next(reader)
cable2 = next(reader)

# list of all horizontal vectors of cable1 as tuples: (y, x1, x2)
cable1_h_vectors = []

# list of all vertical vectors of cable1 as tuples: (x, y1, y2)
cable2_v_vectors = []


def vectorize(cable):
    currX = 0
    currY = 0

    h_vectors = []
    v_vectors = []
    steps=0

    for c in cable:
        if c[0] == 'U':
            nextY = currY+int(c[1:])
            v_vectors.append((currX, currY, nextY, steps))
            steps+=int(c[1:])
            currY = nextY
        elif c[0] == 'D':
            nextY = currY-int(c[1:])
            v_vectors.append((currX, currY, nextY, steps))
            steps+=int(c[1:])
            currY = nextY
        elif c[0] == 'R':
            nextX = currX+int(c[1:])
            h_vectors.append((currY, currX, nextX, steps))
            steps+=int(c[1:])
            currX = nextX
        else:
            nextX = currX-int(c[1:])
            h_vectors.append((currY, currX, nextX, steps))
            steps+=int(c[1:])
            currX = nextX

    return (h_vectors, v_vectors)

# find where the cables cross (do the cables overlay lenghtwise?)
def find_crosspoints(horizontal_vectors, vertical_vectors):
    crosspoints = []

    for hy, hx1, hx2, steps_h in horizontal_vectors:
        for vx, vy1, vy2, steps_v in vertical_vectors:

            original_hx1 = hx1
            original_hx2 = hx2
            original_vy1 = vy1
            original_vy2 = vy2

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
                    crosspoints.append(((vx, original_vy1, original_vy2, steps_v), (hy, original_hx1, original_hx2, steps_h)))

    return crosspoints


c1h_vectors, c1v_vectors = vectorize(cable1)
c2h_vectors, c2v_vectors = vectorize(cable2)

# print("hor:", c1h_vectors, "\n ver:" ,c1v_vectors, "\n\n\n")
# print("hor:", c2h_vectors, "\n ver:" ,c2v_vectors, "\n\n\n")


crosspoints = []

crosspoints += find_crosspoints(c1h_vectors, c2v_vectors)
crosspoints += find_crosspoints(c2h_vectors, c1v_vectors)


for v, h in crosspoints[1:]:
    cross_x, y_start, y_end, steps_v = v
    cross_y, x_start, x_end, steps_h = h
    steps = steps_h + steps_v
    
    # print("ver:", "cross x:", cross_x, "steps:", steps_v)
    # print("y_start:", y_start,"y_end", y_end)
    # print("")
    # print("hor:", "cross y:", cross_y, "steps:", steps_h)
    # print("x_start:", x_start,"x_end", x_end)
    # print("\n")
    # print("steps total: ", steps, "\n")

    # print("x_start - cross_x:", x_start - cross_x)
    # print("y_start - cross_y:", y_start - cross_y, "\n")

    steps += abs(x_start - cross_x)
    steps += abs(y_start - cross_y)
    if steps<48000:
        print("total total: ", steps)
    # print("\n\n\n")


    

