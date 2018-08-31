x=32
string="00000000000000000000000000000000"
string2=[]
string3=[]
for i in range(len(string)):
    string2.append(string[i])
for j in range(x):
    string2[j]="1"
int1 = ''.join(string2[0:8])
int2 = ''.join(string2[8:16])
int3 = ''.join(string2[16:24])
int4 = ''.join(string2[24:32])
b1 = str(int(int1,2))
b2 = str(int(int2,2))
b3 = str(int(int3,2))
b4 = str(int(int4,2))
for i in (b1,b2,b3,b4):
    string3.append(i)
sub='.'.join(string3)
print(sub)
