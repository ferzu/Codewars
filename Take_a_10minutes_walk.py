import random
import itertools
directions = ['n','s','e','w']
opposites = {
    'n': 's',
    'e': 'w'
}

def opposite_dir(dire1, dire2):
    for dr, op_dir in opposites.items():
        if dire1 == dr and dire2 == op_dir:
            return True
        if dire1 == op_dir and dire2 == dr:
            return True
    return False

def opposite_route(dir):
    if dir == 'n':
        return 's'
    if dir == 's':
        return 'n'
    if dir == 'e':
        return 'w'
    if dir == 'w':
        return 'e'
    else: return False

def generate_walk():
    walk_route = []
    distance = 0
    while distance < 10:
        walk_route.append(random.choice(directions))
        distance +=1
    return walk_route

def generate_good_walk():
    walk_route = []
    distance = 0
    while distance < 5:
        walk_route.append(random.choice(directions))
        distance +=1
    distance = 0
    route_back = walk_route
    while distance < 5:
        walk_route.append(opposite_route(route_back[distance]))
        distance +=1
    return (walk_route)

def is_valid_walk(walk):
    e1 = 0
    w1 = 0
    n1 = 0
    s1 = 0
    if len(walk) != 10:
        return False
    for wk in walk:
        if wk == 'e': e1 +=1
        if wk == 'w': w1 +=1
        if wk == 'n': n1 +=1
        if wk == 's': s1 +=1
    if e1 == w1 and n1 == s1:
        return True
    else:
        return False


def main ():
    # random generated walk
    walk = generate_walk()
    print('\n\n-> Back on time: {}'.format(is_valid_walk(walk)))
    print('{} - Randomzed walk'.format(walk))


    # random generated walk that goes back to start (2nd half of the array is the opposite directions than the 1rst, in order )
    good_walk = generate_good_walk()
    print('\n-> Back on time: {}'.format(is_valid_walk(good_walk)))
    print('{} - Good walk'.format(good_walk))


    # random generated walk shuffled (an improved experience would be an array avoiding two opposite directions following each other in the array)
    user_walk = good_walk
    random.shuffle(user_walk)
    print('\n-> Proposed route: {}\n\n'.format(user_walk))

if __name__ == '__main__':
    main()
