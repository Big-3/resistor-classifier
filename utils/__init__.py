import numpy as np

def flatten_ndim(narr):
    dim = narr.shape
    x = dim[0]
    y = dim[1]

    arr = np.zeros(x*y)
    i=0
    for row in narr:
        for elem in row:
            arr[i] = elem
            i+=1

    return arr

def random_string(LIMIT=90):
    random_string=''
    for _ in range(10):
        random_integer=random.randint(65, LIMIT)
        rand_string+=(chr(random_integer))

return random_string
