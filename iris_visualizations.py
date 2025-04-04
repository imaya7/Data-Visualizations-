import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# 1. Bar Plot (Average Sepal Width and Petal Width by Species)
# calculate average widths
avg_widths = data.groupby('species')[['sepal width (cm)', 'petal width (cm)']].mean().reset_index()

plt.figure(figsize=(10, 6))
x = np.arange(len(avg_widths['species']))
width = 0.35
# bars for sepal width and petal width
plt.bar(x - width/2, avg_widths['sepal width (cm)'], width, label='Sepal Width (cm)', color='skyblue')
plt.bar(x + width/2, avg_widths['petal width (cm)'], width, label='Petal Width (cm)', color='orange')
plt.xticks(x, avg_widths['species'], fontsize=12)
#  labels for the bar plot
plt.title("Average Sepal Width and Petal Width by Species", fontsize=16)
plt.xlabel("Species", fontsize=14)
plt.ylabel("Width (cm)", fontsize=14)
#add legend and grid
plt.legend(title="Feature", fontsize=12, title_fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Histogram (Distribution of Petal Length by Species)
plt.figure(figsize=(10, 6))
colors = ['skyblue', 'orange', 'green']
species = data['species'].unique()
# loop and plot the petal length for each species
for i, sp in enumerate(species):
    subset = data[data['species'] == sp]
    plt.hist(subset['petal length (cm)'], bins=15, alpha=0.7, label=sp, color=colors[i])
#  labels for the histogram
plt.title("Petal Length by Species", fontsize=16)
plt.xlabel("Petal Length (cm)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
# add legend and grid
plt.legend(title="Species", fontsize=12, title_fontsize=14, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Scatter Plot: Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6))
colors = ['skyblue', 'orange', 'green']
markers = ['o', 's', 'D'] #marker styles for each species
# loop and plot the sepal length and width for each species
for i, sp in enumerate(species):
    subset = data[data['species'] == sp]
    plt.scatter(
        subset['sepal length (cm)'], subset['sepal width (cm)'],
        label=sp, color=colors[i], marker=markers[i], edgecolor='black', s=100, alpha=0.8
    )

# Add regression lines for each species
for i, sp in enumerate(species):
    subset = data[data['species'] == sp]
    #filter the data for each species
    m, b = np.polyfit(subset['sepal length (cm)'], subset['sepal width (cm)'], 1)
    #regression line y=mx+b
    plt.plot(subset['sepal length (cm)'], m * subset['sepal length (cm)'] + b, linestyle='--', color=colors[i])
#  labels for the scatter plot
plt.title("Sepal Length vs Sepal Width by Species", fontsize=16, fontweight='bold')
plt.xlabel("Sepal Length (cm)", fontsize=14)
plt.ylabel("Sepal Width (cm)", fontsize=14)
plt.legend(title="Species", fontsize=12, title_fontsize=14, loc='upper right')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
