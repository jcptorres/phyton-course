from io import open as op
lorem = op('lorem.txt','w')
lTxt = ''
lorem.write(lTxt)
lorem.close()

loremod = op('lorem.txt','r')
lorem = loremod.read()
