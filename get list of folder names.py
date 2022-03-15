from glob import glob
folders = glob('Datasets/Train/*')
l=[]
for row in folders:
    x=row.split("\\")
    l.append(x[1])
print(l[0],l[1],l[2])