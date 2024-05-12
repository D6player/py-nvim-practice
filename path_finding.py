""" Basic pathfinding """

from collections import defaultdict
from math import inf 

def find_shortest_path(orig, dst, tiles):
    if orig == dst:
        return orig
    
    h = lambda n: distance(n, dst)
    
    queue = {orig}
    fathers = dict()

    gScore = defaultdict(lambda: inf)
    gScore[orig] = 0

    fScore = defaultdict(lambda: inf)
    fScore[orig] = h(orig)

    while queue:
        father = min(queue, key=(lambda n: fScore[n]))
        queue.remove(father)
        if father == dst:
            return first_step(fathers, dst, orig)
            
        for neighbor in get_neighbors(father, tiles):
            tentative_gScore = gScore[father] + 1
            if tentative_gScore < gScore[neighbor]:
                fathers[neighbor] = father
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                queue.add(neighbor)
                
    return orig # failure

def get_neighbors(n, tiles):
    (x, y) = n
    return filter(
        (lambda i: tiles[i[1]][i[0]].is_empty()),
        filter(
            (lambda i: i[0] in range(0, 100) and i[1] in range(0, 50)),
            [(x+1, y), (x-1, y), (x, y+1), (x, y-1)],
        ),
    )

def distance(orig, dst):
    ((x0, y0), (x1, y1)) = (orig, dst)
    return abs(x1-x0) + abs(y1-y0)

def eucli_dis(orig, dst):
    ((x0, y0), (x1, y1)) = (orig, dst)
    return (x1-x0)**2 + 4*(y1-y0)**2

def first_step(fathers, dst, orig) -> tuple:
    n = dst
    while (dst := fathers.get(dst)) != orig:
        n = dst
    
    return n

