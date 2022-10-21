
import numpy as np
x1 = np.random.randint(1,20,15)
print(x1)

x2=np.reshape(x1,(3,5))
print(x2)
print(x2.shape)

max_element=np.amax(x2,axis=1)
max_element=max_element[:,None]
x3=np.where(x2==max_element,0,x2)
print(x3)

