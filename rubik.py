#10 01 01 -->x
#   bb 0 -->y 
#   bb 1 -->y
#ll uu rr 
#ll uu rr
#   ff
#   ff
#   dd
#   dd
import copy
rubik={ 'b':[['b','b'],['b','b']],
        'r':[['r','r'],['r','r']],
        'f':[['f','f'],['f','f']],
        'l':[['l','l'],['l','l']],
        'u':[['u','u'],['u','u']],
        'd':[['d','d'],['d','d']]}
rblv = 2
#clockwise
def raw_copy(array1,y1,x1,array2,y2,x2):
    for idx in range(rblv):
        array2[eval(y2)][eval(x2)]=array1[eval(y1)][eval(x1)]

#---------------------------------------------    

def rotate(face,layer,direction):
    global rubik
    tmp = None
    slayer = str(layer)
    if layer == 0 or layer == rblv - 1 :
        tmp = copy.copy(rubik[face])
        #rote_array(tmp,direction)
    if face == 'u':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['b'])
            raw_copy(rubik['r'],slayer,"idx",rubik['b'],slayer,"idx")
            raw_copy(rubik['f'],slayer,"rblv-1-idx",rubik['r'],slayer,"idx")
            raw_copy(rubik['l'],slayer,"idx",rubik['f'],slayer,"idx")
            raw_copy(tmp,slayer,"rblv-1-idx",rubik['l'],slayer,"idx")

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['b'])
            raw_copy(rubik['l'],slayer,"idx",rubik['b'],slayer,"idx")
            raw_copy(rubik['f'],slayer,"rblv-1-idx",rubik['l'],slayer,"idx")
            raw_copy(rubik['r'],slayer,"idx",rubik['f'],slayer,"idx")
            raw_copy(tmp,slayer,"rblv-1-idx",rubik['r'],slayer,"idx")

    elif face == 'l':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['f'],"idx",slayer,rubik['u'],"idx",slayer)
            raw_copy(rubik['d'],"rblv-1-idx",slayer,rubik['f'],"idx",slayer)
            raw_copy(rubik['b'],"idx",slayer,rubik['d'],"idx",slayer)
            raw_copy(tmp,"rblv-1-idx",slayer,rubik['b'],"idx",slayer)

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['b'],"rblv-1-idx",slayer,rubik['u'],"idx",slayer)
            raw_copy(rubik['d'],"idx",slayer,rubik['b'],"idx",slayer)
            raw_copy(rubik['f'],"rblv-1-idx",slayer,rubik['d'],"idx",slayer)
            raw_copy(tmp,"idx",slayer,rubik['f'],"idx",slayer)

    elif face == 'b':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['r'],"idx","rblv-1" + "-" + slayer,rubik['u'],slayer,"idx")
            raw_copy(rubik['d'],slayer,"rblv-1-idx",rubik['r'],"idx","rblv-1" + "-" + slayer)
            raw_copy(rubik['l'],"idx","rblv-1" + "-" + slayer,rubik['d'],slayer,"idx")
            raw_copy(tmp,slayer,"rblv-1-idx",rubik['l'],"idx","rblv-1" + "-" + slayer)

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['l'],"idx","rblv-1" + "-" + slayer,rubik['u'],slayer,"idx")
            raw_copy(rubik['d'],slayer,"idx",rubik['l'],"idx","rblv-1" + "-" + slayer)
            raw_copy(rubik['r'],"idx","rblv-1" + "-" + slayer,rubik['d'],slayer,"idx")
            raw_copy(tmp,slayer,"idx",rubik['r'],"idx","rblv-1" + "-" + slayer)
def draw_cube():
    i =0
#test
rotate('u',1,'left')
print rubik['b']
print rubik['l'],rubik['u'],rubik['r']
print rubik['f']
print rubik['d']

