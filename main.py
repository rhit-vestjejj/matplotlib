import matplotlib.pyplot as plt

import numpy as np
import pandas as pandas

x_1 = np.linspace(0, 5, 10)
y_1 = x_1**2
# plt.plot(x_1, y_1)
plt.xlabel('Days')
plt.ylabel('Days Squared')
plt.title('Days Squared Chart')

plt.subplot(1, 2, 1)
plt.plot(x_1, y_1, 'r')


plt.subplot(1, 2, 2)
plt.plot(x_1, y_1, 'b')

fig_1 = plt.figure(figsize=(5, 4), dpi=100)
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
axes_1.set_xlabel('Days')
axes_1.set_ylabel('Days Squared')
axes_1.set_title('Days Squared Chart')
axes_1.plot(x_1, y_1, label = 'x/x^2')
axes_1.plot(y_1, x_1, label = 'x/x^2')
axes_1.legend(loc = 0)

plt.show()