"""
https://leetcode.com/discuss/interview-question/808374/

Approach:
This problem requires usage of HashMaps for constant lookup times for number of things such as if there exists X same as the query city or Y same as the query city and then compute the distance. Eventually reutrn the alphabetically smallest city.

Time Complexity: O(N*KlogK)
Space Ccomplexity: O(3N)
"""
import collections
import sys

def compute_distance(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)


def get_nearest_city(num_city, cities, x_coord, y_coord, num_query, queries):
    city_list, x_list, y_list = {}, collections.defaultdict(list), collections.defaultdict(list)

    for city, x, y in zip(cities, x_coord, y_coord):
        city_list[city] = (x,y)
        x_list[x].append(city)
        y_list[y].append(city)

    res = []

    for query in queries:
        x, y = city_list[query]
        min_dist = sys.maxsize
        min_city = None

        for c in x_list[x] + y_list[y]:
            x1, y1 = city_list[c]
            if c!=query:
                dist = compute_distance(x,y, x1, y1)
                if dist < min_dist:
                    if dist == min_dist:
                        min_city = min(min_city, c)
                    else:
                        min_city = c
        if min_city:
            res.append(min_city)
        else:
            res.append(None)

    return res


assert get_nearest_city(3, ["c1","c2","c3"], [3,2,1],[3,2,3], 3, ["c1","c2","c3"]) == ["c3", None, "c1"]