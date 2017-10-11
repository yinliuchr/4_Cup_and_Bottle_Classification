import pickle

a = open('valid_forstu.pickle','rd')
b = pickle.load(a)

imgCount = len(b[0])
chaCount = len(b[0][0])
print imgCount, chaCount

g = open('g.txt','w')
for i in range(0, imgCount):
    s = b[1][i]
    s = '%d'%s 
    for j in range(0, chaCount):
        tt = j + 1
        hh = b[0][i][j]
        s = s + ' ' + '%d'%tt + ':' + '%f'%hh
    s = s + '\n'
    g.writelines(s)

