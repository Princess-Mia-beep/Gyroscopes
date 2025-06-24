# Plot function
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from data import pd_data_10g, pd_data_70g, pd_data_100g
sns.set_theme()

pd_data_10g["label"] = "10g"
pd_data_70g["label"] = "70g"
pd_data_100g["label"] = "100g"
combined_df = pd.concat([pd_data_10g, pd_data_70g, pd_data_100g])
from scipy.stats import linregress

# Group by mass label

from scipy.stats import linregress

# Group by mass label
for label, df in combined_df.groupby("label"):
    result = linregress(df["height_m"], df["t_avg_s_sqr"])
    print(f"{label}: slope = {result.slope:.4f}, intercept = {result.intercept:.4f}, R² = {result.rvalue**2:.4f}")
sns.lmplot(
    data=combined_df,
    x="height_m",
    y="t_avg_s_sqr",
    hue="label",         # separate lines by label
    markers=["o", "s", "D"],
    ci=None,             # turn off confidence interval shading (optional)
    legend_out=False,    # keep legend inside plot
    height=5,            # figure height
    aspect=1.2           # width = aspect × height
)

plt.xlabel("Height (m)")
plt.ylabel(r"$\overline{t}_f^2$ (s$^2$)")
plt.title(r"Regression of $t_f^2$ vs Height for Different Masses")
plt.tight_layout()
plt.show()
plt.show()