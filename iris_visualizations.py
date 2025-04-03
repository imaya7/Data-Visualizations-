import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Set a consistent style for all plots
sns.set_theme(style="whitegrid")

# 1. Bar Plot (Average Sepal Width and Petal Width by Species)
avg_widths = data.groupby('species')[['sepal width (cm)', 'petal width (cm)']].mean().reset_index()
avg_widths_melted = avg_widths.melt(id_vars='species', var_name='Feature', value_name='Width (cm)')
plt.figure(figsize=(10, 6))  # call once
try:
    sns.barplot(data=avg_widths_melted, x='species', y='Width (cm)', hue='Feature', palette='husl')
    plt.title("Average Sepal Width and Petal Width by Species", fontsize=16)
    plt.xlabel("Species", fontsize=14)
    plt.ylabel("Width (cm)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Feature", fontsize=12, title_fontsize=14)
    plt.show()
except Exception as e:
    print(f"Error while creating the bar plot: {e}")

# 2. Histogram (Distribution of Petal Length by Species)
plt.figure(figsize=(10, 6))  # call once
try:
    sns.histplot(
        data=data,
        x='petal length (cm)',
        hue='species',
        kde=True,
        palette='husl',
        bins=15,
        alpha=0.7
    )
    plt.title(" Petal Length by Species", fontsize=16)
    plt.xlabel("Petal Length (cm)", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)

    # Add a legend to the histogram
    plt.legend(
        title="Species",
        fontsize=12,
        title_fontsize=14,
        loc='upper right',
        labels=[
            "Setosa",
            "Versicolor",
            "Virginica"
        ]
    )
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
except Exception as e:
    print(f"Error while creating the histogram: {e}")

# 3. Scatter Plot: Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6))  # call once
try:
    sns.scatterplot(
        data=data,
        x='sepal length (cm)',
        y='sepal width (cm)',
        hue='species',
        style='species',
        palette='husl',
        s=100,  #  markers size 
        edgecolor='black',  # Add marker border
        alpha=0.8  # Transparency 
    )

    # Add regression lines for each species
    for species in data['species'].unique():
        subset = data[data['species'] == species]
        sns.regplot(
            data=subset,
            x='sepal length (cm)',
            y='sepal width (cm)',
            scatter=False,
            color=sns.color_palette('husl', n_colors=3)[list(data['species'].unique()).index(species)],
            line_kws={'linestyle': '--', 'linewidth': 1.5}
        )

    # Customize the plot
    plt.title("Sepal Length vs Sepal Width by Species", fontsize=16, fontweight='bold')
    plt.xlabel("Sepal Length (cm)", fontsize=14)
    plt.ylabel("Sepal Width (cm)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Species", fontsize=12, title_fontsize=14, loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error while creating the scatter plot: {e}")