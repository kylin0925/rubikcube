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

arr = []
def fill_arr(arr,n):
    arr = [ ['' for i in range(n*4)] for i in range(n*3) ]
    for i in range(n*1,n*2):
        for j in range(n):
            arr[j][i]=rubik['u'][j][i-n*1]

    face_order = 'lfrb'
    for i in range(n,n*2):
        idx = 0
        for j in range(n*4):
            if j != 0 and j % n ==0:
                idx = idx+1     

            print j,idx
            arr[i][j] = rubik[face_order[idx]][i-n][j%n]

    for i in range(n*1,n*2):
        for j in range(n*2,n*2+n):
            arr[j][i]=rubik['d'][j-n*2][i-n]


    #for i in range(n*3):
    #    print arr[i]
      
            
    return arr
arr = fill_arr(arr,2)

for i in range(len(arr)):
    tmp = ''
    for j in range(len(arr[0])):
        if arr[i][j] == '':
            tmp = tmp + black
        else:
            tmp = tmp + color_map[ arr[i][j]]
    print tmp
print '--------------------------------'
print black + black + color_map['u'] + color_map['u']
print black + black + color_map['u'] + color_map['u']

print color_map['l'] + color_map['l'] + color_map['f'] + color_map['f'] +\
    color_map['r'] + color_map['r'] + color_map['b'] + color_map['b']

print color_map['l'] + color_map['l'] + color_map['f'] + color_map['f'] +\
    color_map['r'] + color_map['r'] + color_map['b'] + color_map['b']

print black + black + color_map['d'] + color_map['d']
print black + black + color_map['d'] + color_map['d']











