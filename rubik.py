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
#draw black
red = u'\x1b[%dm\u2587\x1b[0m' % 31
green = u'\x1b[%dm\u2587\x1b[0m' % 32
yellow = u'\x1b[%dm\u2587\x1b[0m' % 33
blue = u'\x1b[%dm\u2587\x1b[0m' % 34
white = u'\x1b[%dm\u2587\x1b[0m' % 37
magenta = u'\x1b[%dm\u2587\x1b[0m' % 35
black = u'\x1b[%dm\u2587\x1b[0m' % 30
color_map= {'l':red,'f':green,'u':yellow,'d':white,'r':magenta,'b':blue}

def black_str(n):
    return "".join([black for i in range(n)])

def color_blk(face,lv,n):
    tmp = ""
    if face !='l':
        for i in range(n):
            tmp = tmp + color_map[rubik[face][lv][i]]
    else:
        for i in range(n-1,-1,-1):
            tmp = tmp + color_map[rubik[face][lv][i]]
    return tmp

def draw_cube(rblv):
    n = rblv
    for i in range(2):
        print black_str(n)+color_blk('u',i,n)

    for i in range(2):
        print color_blk('l',i,n)+color_blk('f',i,n)+color_blk('r',i,n)+ color_blk('b',i,n)

    for i in range(2):
        print black_str(n)+color_blk('d',0,n)

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
            raw_copy(rubik['r'],slayer,"idx",rubik['b'],slayer,"rblv-1-idx")
            raw_copy(rubik['f'],slayer,"idx",rubik['r'],slayer,"idx")
            raw_copy(rubik['l'],slayer,"idx",rubik['f'],slayer,"rblv-1-idx")
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
#test
rotate('u',0,'left')
rotate('u',1,'left')
print rubik['b']
print rubik['l'],rubik['u'],rubik['r']
print rubik['f']
print rubik['d']
draw_cube(rblv)
