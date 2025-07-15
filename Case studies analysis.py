import pandas as pd
from scipy.stats import ttest_rel
import seaborn as sns
import matplotlib.pyplot as plt

# Data setup: Satellite Structure and Biomimetic Spring are SLS (plastic); Hydrofoil and Aerofoil are FDM (plastic)
data = {
    'Component': ['Satellite Structure (SLS)', 'Hydrofoil Part (FDM)', 'Aerofoil Part (FDM)', 'Biomimetic Spring (SLS)'],
    'Iterations_Conventional': [7, 10, 12, 15],
    'Iterations_DfAM': [3, 3, 4, 5],
    'SurfaceRoughness_Conventional': [14.0, 30.0, 28.0, 14.0],  # SLS: 14, FDM: 30/28, SLS: 14
    'SurfaceRoughness_DfAM': [12.0, 25.0, 24.0, 12.0],         # SLS: 12, FDM: 25/24, SLS: 12
    'DimensionalError_Conventional': [0.3, 0.2, 0.2, 0.3],     # SLS: 0.3, FDM: 0.2, SLS: 0.3
    'DimensionalError_DfAM': [0.2, 0.14, 0.13, 0.2]            # SLS: 0.2, FDM: 0.14/0.13, SLS: 0.2
}
df = pd.DataFrame(data)

# Descriptive statistics
print("Descriptive Statistics for Iterations:")
print(df[['Iterations_Conventional', 'Iterations_DfAM']].describe())

print("\nDescriptive Statistics for Surface Roughness:")
print(df[['SurfaceRoughness_Conventional', 'SurfaceRoughness_DfAM']].describe())

print("\nDescriptive Statistics for Dimensional Error:")
print(df[['DimensionalError_Conventional', 'DimensionalError_DfAM']].describe())

# Paired t-tests for each metric
t_stat_iter, p_val_iter = ttest_rel(df['Iterations_Conventional'], df['Iterations_DfAM'])
t_stat_sr, p_val_sr = ttest_rel(df['SurfaceRoughness_Conventional'], df['SurfaceRoughness_DfAM'])
t_stat_de, p_val_de = ttest_rel(df['DimensionalError_Conventional'], df['DimensionalError_DfAM'])

print("\nPaired t-test for Iterations:")
print(f"t-statistic: {t_stat_iter}, p-value: {p_val_iter}")

print("\nPaired t-test for Surface Roughness:")
print(f"t-statistic: {t_stat_sr}, p-value: {p_val_sr}")

print("\nPaired t-test for Dimensional Error:")
print(f"t-statistic: {t_stat_de}, p-value: {p_val_de}")

# Data melting for visualization
iterations_df = df.melt(id_vars=['Component'], value_vars=['Iterations_Conventional', 'Iterations_DfAM'],
                        var_name='Approach', value_name='Iterations')
sr_df = df.melt(id_vars=['Component'], value_vars=['SurfaceRoughness_Conventional', 'SurfaceRoughness_DfAM'],
                var_name='Approach', value_name='Surface Roughness (Ra, µm)')
de_df = df.melt(id_vars=['Component'], value_vars=['DimensionalError_Conventional', 'DimensionalError_DfAM'],
                var_name='Approach', value_name='Dimensional Error (mm)')

# Plot 1: Design Iterations
plt.figure(figsize=(8, 5))
sns.barplot(data=iterations_df, x='Component', y='Iterations', hue='Approach')
plt.title('Design Iterations: Conventional vs. DfAM')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 2: Surface Roughness
plt.figure(figsize=(8, 5))
sns.barplot(data=sr_df, x='Component', y='Surface Roughness (Ra, µm)', hue='Approach')
plt.title('Surface Roughness: Conventional vs. DfAM')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plot 3: Dimensional Error
plt.figure(figsize=(8, 5))
sns.barplot(data=de_df, x='Component', y='Dimensional Error (mm)', hue='Approach')
plt.title('Dimensional Error: Conventional vs. DfAM')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
