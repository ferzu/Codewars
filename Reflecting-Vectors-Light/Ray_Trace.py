
# Working progress code, not yet 100% functional.

import math
def get_reflected_vector(head, tail):
    h0,h1 = head
    t0, t1 = tail
    # incident vector head centered at tail (0,0)
    inc = (h0-t0, h1-t1)
    ix, iy = inc
    # normals for reflection at borders
    n = (0,0)
    if h1 == max_y: n = (0,-1)
    if h1 == 0: n = (0,1)
    if h0 == max_x: n = (-1,0)
    if h0 == 0: n = (1,0)
    nx,ny = n
    print('Incidence vector: {}'.format(inc))
    print('Normal: {}'.format(n))
    # reflected vector head at tail (0,0)
    ref  = (ix - 2*(ix*nx + iy*ny)*nx, iy - 2*(ix*nx + iy*ny)*ny)
    # normalized reflected vector at (0,0) for shortened reflections
    if abs(h0 - t0) < max_y:
        ref_u = unit_vector(ref)
        mod = math.sqrt(2)*max_y
        ref = tuple([mod * x for x in ref_u])
        r_h0, r_h1 = ref
        head = (r_h0 + h0, r_h1 + h1)
        tail = (h0, h1)
    else:
        head = ref
    print('Reflected vector: {}'.format(ref))
    # print('Reflected Head: {}'.format(head))
    # print('Reflected Tail: {}'.format(tail))
    ref = [head, tail] # reflected vector
    return ref

def unit_vector (vector):
    v = math.sqrt((vector[0]**2 + vector[1]**2))
    u = (vector[0]/v, vector[1]/v)
    return u

def border_reflection(head, tail):
    h0,h1 = head
    t0, t1 = tail
    # RIGHT BORDER
    if h0 > max_x:
        d = h0 - max_x
        h0 = max_x
        if h1 > t1: # incidence of positive slope
            h1 = h1 - d
        else: # negative slope
            h1 = h1 + d
        head = (h0, h1)
        print('Head reduction: {}'.format(head))
        print('Tail reduction: {}'.format(tail))
        ref = get_reflected_vector(head,tail)
        return ref
    # TOP BORDER
    if h1 > max_y:
        d = h1 - max_y
        h1 = max_y
        if h0 < t0: # incidence coming from the right
            h0 = h0 + d
        else:
            h0 = h0 - d
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref
    # BOTTOM BORDER
    if h1 < 0:
        d = abs(h1)
        h1 = 0
        if h0 < t0: # incidence coming from the right
            h0 = h0 + d
        else:
            h0 = h0 - d
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref
    # LEFT BORDER
    if h0 < 0:
        d = abs(h0)
        h0 = 0
        if h1 > t1:
            h1 = h1 - d
        else:
            h1 = h1 + d
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref

def propagate_vector(head, tail):
    h0,h1 = head
    ref = get_reflected_vector(head,tail)
    p_tail = head # new tail is last head
    h00, h11 = (ref[0][0], ref[0][1])
    p_head = (h0+h00, h1+h11)
    vp = [p_head, p_tail]
    # print(ref)
    # print(h00,h11)
    # print(p_head)
    # print(vp)
    return vp

def exit(head):
    if head == (0,0) or head == (max_x, max_y): return 'true'
    if head == (0,max_y) or head == (max_x,0): return 'false'
    else: return 'continue'

def ray_trace(head, tail):
    while True:
        vp = propagate_vector (head, tail)
        head, tail = vp
        h0, h1 = head
        print('Propagated vector: {}'.format(vp))
        while h0 > max_x or h1 > max_y or h1 < 0 or h0 < 0:
            vr = border_reflection(head,tail)
            head, tail = vr
            h0,h1 = head
        print('Head: {}'.format(head))
        exit1 = exit(head)
        if exit1 == 'true':
            print('True. Exit point: {}'.format(head))
            return True
            break
        if exit1 == 'false':
            print('False. Exit point: {}'.format(head))
            return False
            break
        else:
            pass

def vector_generator():
    tail = (0,0)
    head = (max_y, max_y)
    v = [head, tail]
    return v

def reflections (max_x, max_y):
    if max_x == max_y:
        return True
    if max_x > max_y: pass
    if max_x < max_y:
        swap = max_y
        max_y = max_x
        max_x = swap
    start = vector_generator()
    print('Initial vector: {}'.format(start))
    head, tail = start
    print(start)
    rt = ray_trace(head, tail)
    return rt


if __name__ == '__main__':

    global max_x, max_y
    max_x, max_y = (6,2)
    # max_x > max_y
    rf = reflections(max_x, max_y)
    print(rf)
