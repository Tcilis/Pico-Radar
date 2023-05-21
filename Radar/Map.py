import numpy as np
import matplotlib.pyplot as plt

# Polar plot attributes and initial conditions
fig = plt.figure(facecolor='k')
ax = fig.add_subplot(111, polar=True, facecolor='#006d70')
ax.set_ylim([0.0, 100.0])  # Range of distances to show
ax.set_xlim([0.0, np.pi])  # Limited by the servo span (0-180 deg)
ax.tick_params(axis='both', colors='w')
ax.grid(color='w', alpha=0.5)  # Grid color
ax.set_rticks(np.linspace(0.0, 100.0, 5))  # Show 5 different distances
ax.set_thetagrids(np.linspace(0.0, 180.0, 10))  # Show 10 angles
angles = np.arange(0, 181, 1)  # 0 - 180 degrees
theta = angles * (np.pi / 180.0)  # To radians
dists = np.ones((len(angles),))  # Dummy distances until real data comes in
pols, = ax.plot([], linestyle='', marker='o', markerfacecolor='w',
                markeredgecolor='#EFEFEF', markeredgewidth=1.0,
                markersize=10.0, alpha=0.9)  # Dots for radar points
line1, = ax.plot([], color='w', linewidth=4.0)  # Sweeping arm plot

plt.show()
