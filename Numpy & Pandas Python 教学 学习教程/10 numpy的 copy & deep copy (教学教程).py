import  numpy as np
a=np.arange(5);
b=a;
c=a;
f=b;
print(a)
print(b)
print(c)
print(f)

# 批量改变
b=np.copy(a)

a[1:3]=44;
print(a,b)

print(b)