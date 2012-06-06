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
    if layer == 0 or layer == rblv - 1 :
        tmp = copy.copy(rubik[face])
        #rote_array(tmp,direction)
    if face == 'u':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['b'])
            raw_copy(rubik['r'],"0","idx",rubik['b'],"0","idx")
            raw_copy(rubik['f'],"0","rblv-1-idx",rubik['r'],"0","idx")
            raw_copy(rubik['l'],"0","idx",rubik['f'],"0","idx")
            raw_copy(tmp,"0","rblv-1-idx",rubik['l'],"0","idx")

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['b'])
            raw_copy(rubik['l'],"0","idx",rubik['b'],"0","idx")
            raw_copy(rubik['f'],"0","rblv-1-idx",rubik['l'],"0","idx")
            raw_copy(rubik['r'],"0","idx",rubik['f'],"0","idx")
            raw_copy(tmp,"0","rblv-1-idx",rubik['r'],"0","idx")

    elif face == 'l':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['f'],"idx","0",rubik['u'],"idx","0")
            raw_copy(rubik['d'],"rblv-1-idx","0",rubik['f'],"idx","0")
            raw_copy(rubik['b'],"idx","0",rubik['d'],"idx","0")
            raw_copy(tmp,"rblv-1-idx","0",rubik['b'],"idx","0")

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['b'],"rblv-1-idx","0",rubik['u'],"idx","0")
            raw_copy(rubik['d'],"idx","0",rubik['b'],"idx","0")
            raw_copy(rubik['f'],"rblv-1-idx","0",rubik['d'],"idx","0")
            raw_copy(tmp,"idx","0",rubik['f'],"idx","0")

            print rubik['f']
    elif face == 'b':
        if direction == 'right':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['r'],"idx","1",rubik['u'],"0","idx")
            raw_copy(rubik['d'],"0","rblv-1-idx",rubik['r'],"idx","1")
            raw_copy(rubik['l'],"idx","1",rubik['d'],"0","idx")
            raw_copy(tmp,"0","rblv-1-idx",rubik['l'],"idx","1")

        elif direction == 'left':
            tmp = copy.deepcopy(rubik['u'])
            raw_copy(rubik['l'],"idx","1",rubik['u'],"0","idx")
            raw_copy(rubik['d'],"0","idx",rubik['l'],"idx","1")
            raw_copy(rubik['r'],"idx","1",rubik['d'],"0","idx")
            raw_copy(tmp,"0","idx",rubik['r'],"idx","1")

#test
rotate('b',0,'right')
print rubik['b']
print rubik['l'],rubik['u'],rubik['r']
print rubik['f']
print rubik['d']

