
# Working progress, not yet tested.

def get_reflected_vector(head, tail):
    h0,h1 = head
    t0, t1 = tail
    inc = (h0-t0, h1-t1)
    ix, iy = inc
    n = (0,0)
    if h1 == max_y: n = (0,-1)
    if h1 == 0: n = (0,1)
    if h0 == max_x: n = (-1,0)
    if h0 == 0: n = (1,0)
    nx,ny = n
    ref  = (ix - 2*(ix*nx + iy*ny)*nx, iy - 2*(ix*nx + iy*ny)*ny)
    if abs(h0 - t0) < max_y:
        ref_u = unit_vector(ref)
        ref = tuple([max_y * x for x in ref_u])
    return ref

def unit_vector (vector):
    v = (vector[0]**2 + vector[1]**2)**0.5
    u = (vector[0]/v, vector[1]/v)
    return u

def border_reflection(head, tail):
    h0,h1 = head
    t0, t1 = tail
    # reflection right border
    if h0 > max_x:
        d = h0 - max_x
        h0 = h0 - d
        h1 = h1 - d
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref
    # reflection top border
    if h1 > max_y:
        d = h0 - max_y
        h0 = h0 - d
        h1 = h1 - d
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref
    # reflection bottom border
    if h1 < 0:
        h0 = t1
        h1 = 0
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref
    # reflection left border
    if h0 < 0:
        d = 0 - max_y
        h0 = 0
        h1 = t0
        head = (h0, h1)
        ref = get_reflected_vector(head,tail)
        return ref

def propagate_vector(head, tail):
    h0,h1 = head
    ref = get_reflected_vector(head,tail)
    p_tail = head
    p_head = (h0+ref[0], h1+ref[1])
    vp = [p_head, p_tail]
    return vp

def vector_generator():
    tail = (0,0)
    head = (max_y, max_y)
    v = [head, tail]
    return v

def exit(head):
    if head == (0,0) or head == (max_x, max_y): return True
    return False

def ray_trace(head, tail):
    h0,h1 = head
    while True:
        head,tail = propagate_vector(head, tail)
        h0,h1 = head
        if h0 > max_x or h1 > max_y or h1 < 0 or h0 < 0:
            head, tail = border_reflection(head,tail)
            h0,h1 = head
        if exit (head):
            return True
            break


if __name__ == '__main__':

    global max_x, max_y
    max_x, max_y = (3,2)

    start = vector_generator()
    if ray_trace(start[0], start[1]):
        print(True)



    # print(get_reflected_vector((2,2), (0,0)))
    # print(propagate_vector((2,2), (0,0)))
