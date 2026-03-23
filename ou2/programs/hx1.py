import sys
import numpy as np
import pdb

if sys.stdin.isatty():
    with open('/Home/staff/mbe/tap/ex1.in') as f:
        inp=f.readlines()
else:
    inp=sys.stdin.readlines()

inp=[l.split() for l in inp if l[0]!='#' and ' ' in l]
inp=[(int(x),int(y)) for x,y in inp]
pts=[np.array([int(x),int(y)],dtype=np.int64) for x,y in inp]
n=len(pts)

# Compute a distance matrix
pts=np.vstack(np.array([np.array(l,dtype=np.int64) for l in inp]))
x_m,y_m=np.meshgrid(pts[:,0],pts[:,1])
dists=np.sqrt((x_m-x_m.T)**2+(y_m-y_m.T)**2)

def path_len(p):
    totl=0.0
    for i in range(len(p)):
        totl+=dists[p[i-1],p[i]]
    return totl

orig_dist=path_len(list(range(n)))
print(f'# Path length as listed in file: {orig_dist}')

# Nearest neighbor, destructive on d_dists
path=[0]
d_dists=np.array(dists)
for _ in range(n-1):
    # Asymptotically for sure slower to do it this way, but we are n^2 either
    # way, and for small instances it'll likely be faster by virtue of numpy
    # being fast.
    d_dists[path[-1],:]=2**62
    path.append(np.argmin(d_dists[:,path[-1]]))

nn_dist=path_len(path)
print(f'# Path after nearest neighbor: {nn_dist:.2f}')
print(f'# {(100*nn_dist/orig_dist):.4f}% of the original')

# To not be boring: lets try to do some local improvement hill climbing!
dist=path_len(path)
ix=list(range(n))
# Make distances into probabilities, i.e. try to swap points close to each
# other first. Rather arbitrarily scaled by the square.
probs=np.sqrt(dists+2**62*np.identity(n))
np.fill_diagonal(probs,0)
probs=probs/sum(probs)
for _ in range(5*max(n,1000)):
    pre_swap_dist=dist
    i=np.random.randint(0,n)
    j=np.random.choice(ix,p=probs[:,i])
    #j=np.random.randint(0,n)
    path[i],path[j]=path[j],path[i]
    dist=path_len(path)
    if pre_swap_dist<dist:
        # worse, undo
        path[i],path[j]=path[j],path[i]
        dist=pre_swap_dist
limp_dist=path_len(path)

print(f'# Path after local improvement: {limp_dist:.2f}')
print(f'# {(100*limp_dist/orig_dist):.4f}% of the original')

print(n)
for p in path:
    print(f"{pts[p,0]} {pts[p,1]}")
