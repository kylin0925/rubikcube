import copy
rubik={ 'b':[['b','b'],['b','b']],
        'r':[['r','r'],['r','r']],
        'f':[['f','f'],['f','f']],
        'l':[['l','l'],['l','l']],
        'u':[['u','u'],['u','u']],
        'd':[['d','d'],['d','d']]}
rblv = 2
print rubik['u']
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

    #elif face == 'r':
    #elif face == 'f':
rote('u',0,'right');
print rubik
print "-----------------"
rote('u',0,'left');

print rubik
