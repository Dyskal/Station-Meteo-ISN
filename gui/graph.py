import matplotlib.pyplot as plt
import numpy as np

plt.style.use('bmh')
fig = plt.figure(figsize=(16, 9))
ax = plt.axes()
plt.title("Humidité (dernières 24h)", color="white", size="30")

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))

plt.grid(color='white')
ax.tick_params(colors='white')
for tick in ax.get_xticklabels():
    tick.set_color('white')
for tick in ax.get_yticklabels():
    tick.set_color('white')


plt.savefig('static/images/graph_daily.png', transparent=True, bbox_inches='tight')
print("graph created !")
