import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

planets = sns.load_dataset("planets")
planets = planets.dropna()

print("\n=== FIRST 5 ROWS ===")
print(planets.head())

print("\n=== COLUMNS ===")
print(planets.columns)

print("\n=== SUMMARY STATS ===")
print(planets.describe())

print("\n=== DISCOVERY METHODS ===")
print(planets["method"].value_counts())

plt.figure(figsize=(10,5))
sns.histplot(planets["orbital_period"], bins=30)
plt.title("Distribution of Planet Orbital Periods")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
sns.histplot(planets["distance"], bins=30, kde=True)
plt.title("Planet Distance Distribution (Histogram + KDE)")
plt.xlabel("Distance (parsecs)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# KDE only
plt.figure(figsize=(10,5))
sns.kdeplot(planets["distance"], shade=True)
plt.title("KDE Curve of Planet Distances")
plt.xlabel("Distance (parsecs)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(
    data=planets,
    x="distance",
    y="orbital_period",
    hue="method",
    alpha=0.7
)
plt.title("Distance vs Orbital Period by Discovery Method")
plt.xlabel("Distance (parsecs)")
plt.ylabel("Orbital Period (days)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
corr = planets.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Planet Data")
plt.tight_layout()
plt.show()
