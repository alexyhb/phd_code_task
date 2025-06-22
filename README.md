## Synthetic Dataset Generator & Distribution Verifier

This project demonstrates how to:

- Analyze a real dataset’s statistical properties.
- Generate a synthetic dataset that follows the same distributions.
- Compare and visualize the statistical similarity between the original and synthetic data.

## Files

`main.py`: Main Python script that performs dataset generation and analysis.

## How to Run

```bash
pip install numpy pandas scipy matplotlib seaborn
python main.py
```

Note: Re-Running the script will generate and overwrite `dataset.csv` and `new_dataset.csv` in the working directory.

## Problem Solving Strategy

### Objective

To simulate data augmentation using statistical cloning. The goal is to replicate the distribution of an original dataset into a new one, preserving categorical proportions and continuous variable distributions.

### Step-by-Step Breakdown

1. **Generate Original Data**
   - `Category1` is a categorical variable with a custom distribution:
     A: 20%, B: 40%, C: 20%, D: 10%, E: 10%.
   - `Value1` and `Value2` are continuous variables drawn from normal distributions:
     - `Value1 ~ N(10, 2)`
     - `Value2 ~ N(20, 6)`
   - Saved to `dataset.csv`.
2. **Analyze Distributions**
   - Compute category frequencies.
   - Compute mean and standard deviation for `Value1` and `Value2`.
3. **Generate New Dataset**
   - Sample `Category1` using the same frequency distribution.
   - Sample `Value1` and `Value2` using the same Gaussian parameters.
   - Output to `new_dataset.csv`.
4. **Compare Distributions**
   - Print category distributions for both datasets.
   - Plot KDE (Kernel Density Estimation) for `Value1` and `Value2` using `seaborn`.
   - Visually verify that the synthetic dataset closely mirrors the original one.
