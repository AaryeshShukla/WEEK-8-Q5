import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for customer engagement
np.random.seed(42)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [f"{h}:00" for h in range(8, 20)]  # 8 AM to 7 PM

# Random engagement values (0-100)
data = np.random.randint(0, 100, size=(len(hours), len(days)))
df = pd.DataFrame(data, index=hours, columns=days)

# Plot heatmap
plt.figure(figsize=(8, 8))  # 512x512 pixels with dpi=64
sns.heatmap(df, annot=True, fmt="d", cmap="YlGnBu", cbar=True, linewidths=0.5)

plt.title("Customer Engagement Heatmap", fontsize=18)
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Hour of Day", fontsize=14)

# Save figure
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
