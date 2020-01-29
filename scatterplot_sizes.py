"""
Scatterplot with continuous hues and sizes
==========================================

_thumb: .45, .45

"""

import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

# Load the example planets dataset
#planets = sns.load_dataset("planets")
titanic = sns.load_dataset("titanic")


#cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
ax = sns.scatterplot(y="age", x="fare",
                     hue="class",
                     sizes=(10, 100),
                     data=titanic)


print(titanic)
plt.show()
