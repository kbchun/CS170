i = 0
j = 0
N = 50
W = 20
matrix = [[0 for x in range(N)] for x in range(N)]
import random
import re

def pretty_print(A):
    print N
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in A]))
    # print "AB"*N

for i in range(N):
    for j in range(N):
        if i == j:
            matrix[i][j] = 0
        elif matrix[j][i] == 0:
            matrix[i][j] = random.randrange(1, 30)
        else:
            matrix[i][j] = matrix[j][i]

# edges =  matrix[N-1]
# for i in range(1, N-1):
#     rand_num = random.randrange(30, 50)
#     edges[i] = rand_num
#     matrix[i][N-1] = rand_num

#local1
chosen_path_a = range(1, N+1)
random.shuffle(chosen_path_a)
count = 0
for i in range(0, N):
    if count != (N-1):
        matrix[chosen_path_a[i]-1][chosen_path_a[i+1]-1] = random.randrange(5,17)
        matrix[chosen_path_a[i+1]-1][chosen_path_a[i]-1] = matrix[chosen_path_a[i]-1][chosen_path_a[i+1]-1]
        count += 1 
#local2
chosen_path_b = range(1, N+1)
random.shuffle(chosen_path_b)
count = 0
for i in range(0, N):
    if count != (N-1):
        matrix[chosen_path_b[i]-1][chosen_path_b[i+1]-1] = random.randrange(1,20)
        matrix[chosen_path_b[i+1]-1][chosen_path_b[i]-1] = matrix[chosen_path_b[i]-1][chosen_path_b[i+1]-1]
        count += 1 
#global min
chosen_path_g = range(1, N+1)
random.shuffle(chosen_path_g)
count = 0
for i in range(0, N):
    if count != (N-1):
        # matrix[chosen_path[i]-1][chosen_path[i+1]-1] = random.randrange(4,8)
        matrix[chosen_path_g[i]-1][chosen_path_g[i+1]-1] = 5
        matrix[chosen_path_g[i+1]-1][chosen_path_g[i]-1] = matrix[chosen_path_g[i]-1][chosen_path_g[i+1]-1]
        count += 1 

current = 0
colors = ['x' for x in range(N+1)]
for i in chosen_path_g:
    if current == 0:
        colors[i] = 'R'
        current = 1
    else:
        colors[i] = 'B'
        current = 0

pretty_print(matrix)
print (''.join(colors))[1:N+1]
print re.sub('[^0-9]', ' ', str(chosen_path_g)) #output




