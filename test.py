from rubik import *
test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"0","idx",test2,"idx","1")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"idx","1",test2,"0","idx")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"0","idx",test2,"idx","1")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"idx","1",test2,"0","idx")
print test2
#left face test
test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"idx","0",test2,"idx","0")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"rblv-1-idx","0",test2,"idx","0")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"idx","0",test2,"idx","0")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"rblv-1-idx","0",test2,"idx","0")
print test2
#upper face test
test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"0","rblv-1-idx",test2,"0","idx")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"0","idx",test2,"0","idx")
print test2

test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,"0","rblv-1-idx",test2,"0","idx")
print test2
lv = 0
test=[[5,6],[2,3]]
test2=[[0,0],[0,0]]
raw_copy(test,str(lv),"idx",test2,str(lv),"idx")
print test2

