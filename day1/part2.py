f = open("input.txt")
txt = [i.strip() for i in f.readlines()]

s = 0

for parth in txt:
    i = parth.replace('two', 't2').replace('one', 'o1').replace('eight', 'e8').replace('four', 'f4').replace('seven', 's7').replace('three', 't3').replace('five', 'f5').replace('nine', 'n9').replace('six', 's6')
    for j in i:
        if j.isdigit():
            b = int(j)*10
            break
    i = parth.replace('nine', '9e').replace('eight', '8t').replace('one', '1e').replace('four', '4r').replace('seven', '7n').replace('two', '2o').replace('three', '3e').replace('five', '5e').replace('six', '6x')
    for j in i:
        if j.isdigit():
            d = j
    s += b+int(d)
    print(b+int(d))

print(s)
