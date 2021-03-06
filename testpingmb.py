
from pingmb import pingmb
import sys
import matplotlib.pyplot as plt

_,MB_Begin,MB_End,MB_Step,IP_SRC=[1]+[int(x) for x in sys.argv[1:-1]]+[sys.argv[3]]


x=[1]
r=[pingmb(IP_SRC,1)]
for i in range(MB_Begin,MB_End,MB_Step):
    r.append(pingmb(IP_SRC,i))
    x.append(i)
    print(f"{i} MBs => {r[-1]:.02f} s")

fig = plt.figure()    
plt.plot(x,r)
fig.suptitle("tamano vs tiempo")
plt.xlabel("Tamano")
plt.ylabel("Tiempo")
plt.savefig("plot.png")
