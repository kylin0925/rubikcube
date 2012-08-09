red = u'\x1b[%dm\u2587\x1b[0m' % 31
green = u'\x1b[%dm\u2587\x1b[0m' % 32
yellow = u'\x1b[%dm\u2587\x1b[0m' % 33
blue = u'\x1b[%dm\u2587\x1b[0m' % 34
white = u'\x1b[%dm\u2587\x1b[0m' % 37
magenta = u'\x1b[%dm\u2587\x1b[0m' % 35

black = u'\x1b[%dm\u2587\x1b[0m' % 30


color_map= {'l':red,'f':green,'u':yellow,'d':white,'r':magenta,'b':blue}

rubik={ 'b':[['l','l'],['b','b']],
        'r':[['b','b'],['r','r']],
        'f':[['r','r'],['f','f']],
        'l':[['f','f'],['l','l']],
        'u':[['u','u'],['u','u']],
        'd':[['d','d'],['d','d']]}

#
# print black_str(n),color_blk(u,n)
# print color_blk(l,n),color_blk(f,n),color_blk(r,n), color_blk(b,n)
# print black_str(n),color_blk(b,n),color_blk(d,n)
#
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
n = 2
for i in range(2):
    print black_str(n)+color_blk('u',i,n)

for i in range(2):
    print color_blk('l',i,n)+color_blk('f',i,n)+color_blk('r',i,n)+ color_blk('b',i,n)

for i in range(2):
    print black_str(n)+color_blk('d',0,n)



