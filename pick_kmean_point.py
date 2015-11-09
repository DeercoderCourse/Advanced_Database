#!/usr/bin/env python
import math

# given the first point, find the other one furthest from it
point1 = (3, 4)
points = [(2,2), (5,2), (9,3), (12,3), (11,4),\
        (12,6), (10,5), (4,8), (6,8), (4,10), (7, 10)]

# given two points, find the remaining one furthest from them
point_set = [(3,4), (12,6)]
other_points = [(2,2), (5,2), (9,3), (12,3),\
        (11,4), (7,10), (10,5), (4,8), (6,8), (4,10)]

def find_most_distant(point, points):
    max_distance = 0
    marker = ()
    for p in points:
        # here we just use dst's square to represent
        distance = math.sqrt(math.pow(p[0]-point[0], 2) \
                + math.pow(p[1]-point[1], 2))
        if distance > max_distance:
            max_distance = distance
            marker = p
    print marker

def find_last_point(points, other_points):
    max_distance = 0
    marker = ()
    # for limited time, I don't use loop for points
    for p in other_points:
        dst1 = math.sqrt(math.pow(p[0]-points[0][0], 2) \
                + math.pow(p[1]-points[0][1], 2))
        dst2 = math.sqrt(math.pow(p[0]-points[1][0], 2) \
                + math.pow(p[1]-points[1][1], 2))
        distance = min(dst1, dst2)
        if distance > max_distance:
            max_distance = distance
            marker = p
    print marker

find_most_distant(point1, points)
find_last_point(point_set, other_points)
