
import numpy as np
import matplotlib.pyplot as plt

# create a fig of size 8 x 6 inches, 80 dots per inch
plt.figure(figsize=(8, 6), dpi=80)

# create a new subplot from a grid of 1 x 1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# plot cosine with blue continous line of width 1 pixel
plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# plot sine with gree continous line of width 1 pixel
plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# set the X limits
plt.xlim(-4.0, 4.0)

# set x ticks
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))

plt.ylim(-1.0, 1.0)

plt.yticks(np.linspace(-1, 1, 5, endpoint=True))



plt.show()