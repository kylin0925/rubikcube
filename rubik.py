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
            a = 1
        elif direction == 'left':
            a = 1
    #elif face == 'l':
    elif face == 'b':
        if direction == 'right':
            t = 1
        elif direction == 'left':
            print 'face b left'
            tmp = copy.copy(rubik['u'])
            raw_copy(rubik['l'],"idx","1",rubik['u'],"0","idx")
            raw_copy(rubik['d'],"0","idx",rubik['l'],"idx","1")
            raw_copy(rubik['r'],"idx","1",rubik['d'],"0","idx")
            raw_copy(tmp,"0","idx",rubik['r'],"idx","1")

            #raw_copy(face['r'],"idx","1",face['d'],"0","idx")
            #raw_copy(face['d'],"0","idx",face['l'],"idx","1")
            #raw_copy(face['l'],"idx","1",face['u'],"0","idx")

#rote('u',0,'right');
#print rubik
#print "-----------------"
#rote('u',0,'left');
#
#print rubik
#back face test
rotate('b',0,'left')
print rubik['b']
print rubik['l'],rubik['u'],rubik['r']
print rubik['f']
print rubik['d']

