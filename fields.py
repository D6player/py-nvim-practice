"""
To render vector fields in blender
"""

from bpy import data as D

obj_strokes = D.objects['Stroke'].data.layers['Lines'].frames[0].strokes

def add_vector(a, b):
    assert(len(a) == len(b))
    
    return tuple( x + y  for x, y in zip(a, b) )

def draw_vector(strokes, point, vector):
    assert(len(point) == 3)
    assert(len(vector) == 3)
    
    stroke = strokes.new()
    stroke.points.add(2)
    
    stroke.points[0].co = point
    stroke.points[1].co = add_vector(point, vector)
    
    return stroke
