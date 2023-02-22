import cythonfn
import sys
import matplotlib.pyplot as plt



max_size = 50000 
times = [0 for i in range(4)]
bw = [0 for i in range(max_size)]

for i in range(max_size):
    times = cythonfn.benchmark_numpy(i)
    data_size = 10*sys.getsizeof(i)*i
    bw[i] = data_size*1e-9/(times[0]+times[1]+times[2]+times[3])
    

plt.plot(range(max_size), bw)
plt.xlabel('Array elements')
plt.ylabel('Bandwidth [GB/s]')