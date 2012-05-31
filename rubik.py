import copy
rubik={ 'b':[['b','b'],['b','b']],
        'r':[['r','r'],['r','r']],
        'f':[['f','f'],['f','f']],
        'l':[['l','l'],['l','l']],
        'u':[['u','u'],['u','u']],
        'd':[['d','d'],['d','d']]}
rblv = 2
#clockwise
def h2v_copy(array1,hy,array2,vx):
    for y in range(rblv):
        array2[y][vx]=array1[hy][y]

def v2h_copy(array1,vx,array2,vy):
    for x in range(rblv):
        array2[vy][x]=array1[(rblv-1)-x][vx]

def v2v_copy(array1,hy,array2,vx):
    for y in range(rblv):
        array2[rblv-1-y][vx]=array1[y][vx]


#counter clockwise
def h2vcw_copy(array1,hy,array2,vx):
    for y in range(rblv):
        array2[rblv-1-y][vx]=array1[hy][y]

def v2hcw_copy(array1,vx,array2,vy):
    for x in range(rblv):
        array2[vy][rblv-1-x]=array1[x][vx]

def v2vcw_copy(array1,hy,array2,vx):
    for y in range(rblv):
        array2[rblv-1-y][vx]=array1[y][vx]


#---------------------------------------------    

def rote(face,layer,direction):
    global rubik
    tmp = None
    if layer == 0 or layer == rbl - 1 :
        tmp = copy.copy(rubik[face])
        #rote_array(tmp,direction)
    if face == 'u':
        if direction == 'right':
            tmp = copy.copy(rubik['b'][0])
            rubik['b'][0] = copy.copy(rubik['l'][0])
            rubik['l'][0] = copy.copy(rubik['f'][0])
            rubik['f'][0] = copy.copy(rubik['r'][0])
            rubik['r'][0] = copy.copy(tmp)
        elif direction == 'left':
            tmp = copy.copy(rubik['b'][0])
            rubik['b'][0] = copy.copy(rubik['r'][0])
            rubik['r'][0] = copy.copy(rubik['f'][0])
            rubik['f'][0] = copy.copy(rubik['l'][0])
            rubik['l'][0] = copy.copy(tmp)

    #elif face == 'l':
    #elif face == 'f':
#rote('u',0,'right');
#print rubik
#print "-----------------"
#rote('u',0,'left');
#
#print rubik
test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
h2v_copy(test,1,test2,0)
print test2
test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
v2h_copy(test,0,test2,1)
print test2
test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
v2v_copy(test,0,test2,0)
print test2

test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
h2vcw_copy(test,1,test2,0)
print test2
test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
v2hcw_copy(test,0,test2,1)
print test2
test=[[1,1],[2,3]]
test2=[[0,0],[0,0]]
v2vcw_copy(test,0,test2,0)
print test2

