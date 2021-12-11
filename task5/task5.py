#ideas:
""" 
1. format the items in a way such that we have a list of lines: [[x1,y1][x2,y2]] and a list of these. we can use a range[x:y+1] (+1 so we incluse y itself) to create lists of points. then we can create a list of intersections, and figure it out from there.




"""
# Second line should intersect with third
# Open file
with open("task5/task5toyinput.txt") as file:
    taskinput = file.read().splitlines()
    taskinput = [item.split(" -> ") for item in taskinput]
    taskinput = [[[int(coords) for coords in coords.split(",")] for coords in item] for item in taskinput]

#convert a pair of coords [[x1,y1][x2,y2]] into a list of points covered
def generateLine(coords_pair):
    # For possible use on diagonal lines (I assume part 2 of the task will require us to account for this)
    # if coords_pair[0][0] != coords_pair[1][0] & coords_pair[0][1] != coords_pair[1][1]:
    #     print("hello")
    #Generates horizontal line points
    if coords_pair[0][0] != coords_pair[1][0]:
        for point in range(coords_pair[0][0], coords_pair[1][0])
