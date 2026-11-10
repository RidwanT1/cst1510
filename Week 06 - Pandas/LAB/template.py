"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT    
Date  :03/11/2026

Run it:   python template.py

"""

import pandas as pd
import matplotlib.pyplot as plt
# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). 

df = pd.read_csv("data.csv")

# ================================================================= PROCESS
# 2. Add a "percent" column:
df["percent"] = (df["used_gb"] / df["total_gb"]) * 100

# Typical and above: Add a "status" column using .apply() with a lambda.
# Rule: use & or | (not 'and'/'or') and wrap conditions in brackets.
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if (x >= 100) else ("WARNING" if (x >= 90) else "OK")
)

# ================================================================== OUTPUT
# 3. Print the DataFrame.
# Threshold: print as-is.
print("--- Full DataFrame (Threshold) ---")
print(df)
print("\n")

# Typical: filter to show only rows that are NOT "OK" using a boolean condition.
print("--- Filtered: NOT OK (Typical) ---")
not_ok_df = df[df["status"] != "OK"]
print(not_ok_df)
print("\n")

# Excellent: Group by status, print count, save to new CSV, and save a bar chart.
print("--- Group Counts (Excellent) ---")
status_counts = df.groupby("status").size()
print(status_counts)

# Save full dataframe to a new CSV
df.to_csv("results.csv", index=False)
print("\nSaved full data to results.csv")

# Produce a bar chart and save as PNG
status_counts.plot(kind="bar", title="Record Status Counts")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_chart.png")
print("Saved chart to status_chart.png")

# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case
