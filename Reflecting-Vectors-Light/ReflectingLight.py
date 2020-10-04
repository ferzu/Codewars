
import random as r

def r_coordenates():
    return (r.randint(0,100), r.randint(0,100))

def size_index(max_x, max_y):
    if max_x and max_y:
        if max_x > max_y:
            return (max_x/max_y)
        else:
            return (max_y/max_x)
    else:
        return(0)

def reflections(max_x, max_y):
    s = size_index(max_x, max_y)
    k = int(s//1) # integer size_index. Sides of the rectangle => max_x, max_y. Reflection 45 from (0,0) => max_x = k*max_y + d*max_y
    d = s % 1 # decimal size_index
    if k>1 and not d:
        if not k%2:
            return False
        else:
            return True
    if k == 1 and not d: #square size area
        return True
    else: # Working out a vectorial solution for the reflections. When d!=0 the puzzel complicates, this solution is not accurate enough. 
        return False

if __name__ == '__main__':

    max_x, max_y = r_coordenates()
    print (max_x, max_y)
    ref = reflections(max_x, max_y)
    print (ref)
