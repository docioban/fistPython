f = open("f1.txt", "r")
txt = f.read()
f.close

f = open("f2.txt", "w")
f.write(txt)
f.close