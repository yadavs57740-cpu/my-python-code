#slicing for 1d
import numpy as np
arr=np.arange(11)
print(arr)
up_arr=arr[:3]
print(up_arr)

#slicing for 2d
import numpy as np
arr=np.arange(16).reshape(8,2)
print(arr)
up_arr=arr[:,-1]
print(up_arr)
