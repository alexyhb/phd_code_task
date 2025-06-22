import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Generate the original synthetic dataset
    np.random.seed(42)
    num_samples = 500
    df = pd.DataFrame(
        {
            "Category1": np.random.choice(
                ["A", "B", "C", "D", "E"],
                num_samples,
                p=[0.2, 0.4, 0.2, 0.1, 0.1]
            ),
            "Value1": np.random.normal(10, 2, num_samples),  # Continuous variable
            "Value2": np.random.normal(20, 6, num_samples),  # Continuous variable
        }
    )
    df.to_csv("./dataset.csv", sep=";")

    # Read the original dataset
    df = pd.read_csv("dataset.csv", sep=";")

    # Analyze distribution of Category1 (frequency)
    category_dist = df["Category1"].value_counts(normalize=True)
    print("Category1 distribution:\n", category_dist)

    # Compute mean and standard deviation of Value1 and Value2
    value1_mean, value1_std = df["Value1"].mean(), df["Value1"].std()
    value2_mean, value2_std = df["Value2"].mean(), df["Value2"].std()
    print(f"Value1 mean: {value1_mean:.2f}, std: {value1_std:.2f}")
    print(f"Value2 mean: {value2_mean:.2f}, std: {value2_std:.2f}")

    # Set random seed for reproducibility
    np.random.seed(2025)
    num_samples = 1000  # Generate more samples

    # Sample new data based on original distribution
    new_df = pd.DataFrame({
        "Category1": np.random.choice(
            category_dist.index,
            size=num_samples,
            p=category_dist.values
        ),
        "Value1": np.random.normal(value1_mean, value1_std, num_samples),
        "Value2": np.random.normal(value2_mean, value2_std, num_samples),
    })

    # Save the new dataset
    new_df.to_csv("new_dataset.csv", sep=";", index=False)

    # Load both datasets for comparison
    original = pd.read_csv("dataset.csv", sep=";")
    new = pd.read_csv("new_dataset.csv", sep=";")
    plt.close('all')

    # Compare categorical distribution
    print("Original Category1 distribution:")
    print(original['Category1'].value_counts(normalize=True))
    print("\nNew Category1 distribution:")
    print(new['Category1'].value_counts(normalize=True))

    # Create a figure with 2 subplots (1 row, 2 columns)
    fig, axes = plt.subplots(1, 2, figsize=(10, 8))

    # KDE plot for Value1
    sns.kdeplot(original["Value1"], label="Original Value1", ax=axes[0])
    sns.kdeplot(new["Value1"], label="Generated Value1", ax=axes[0])
    axes[0].set_title("Value1 Distribution Comparison")
    axes[0].legend()

    # KDE plot for Value2
    sns.kdeplot(original["Value2"], label="Original Value2", ax=axes[1])
    sns.kdeplot(new["Value2"], label="Generated Value2", ax=axes[1])
    axes[1].set_title("Value2 Distribution Comparison")
    axes[1].legend()

    # Adjust layout to avoid overlap
    plt.tight_layout()

    # Show plots
    plt.show()
