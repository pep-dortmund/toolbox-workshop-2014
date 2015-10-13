import matplotlib as mpl
mpl.rcdefaults()


import matplotlib.pyplot as plt
import numpy as np








x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)
plt.figure(figsize=(4.76, 2.94))
plt.plot(x, y)
plt.xlabel(r'$\alpha / \Omega$')
plt.tight_layout(pad=0)
plt.savefig('build/figures/mattex2.pdf',
            bbox_inches='tight', pad_inches=0)
