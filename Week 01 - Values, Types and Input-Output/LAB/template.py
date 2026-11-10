"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT      
Date  : 30/10/2026

Run it:   python template.py

"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.

label = input("Enter hostname: ")
first = float(input("Enter GB used: "))
second = float(input("Enter total GB: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       

difference = first - second
percent = (first / second) * 100

# Excellent requirement: One extra calculated line genuinely useful for the lane.
# Why: Knowing the exact amount of free space (GB remaining) is critical for IT 
# capacity planning to prevent servers from crashing when they hit 100%.
free_space = second - first

# =================================================================== OUTPUT
# 3. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# Threshold: print the three values you were given
print(f" Used       : {first:>10.2f}")

# Typical: add difference and percent, right-aligned, 2 decimal places
print(f" Total      : {second:>10.2f}")
print(f" Free       : {free_space:>10.2f}")
print(f" Percent    : {percent:>10.2f} %")

# Excellent: difference always shows its sign (using +10.2f), plus the extra line
print(f" Difference : {difference:>+10.2f}")

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and write the error in your journal
#    [x] Check every variable name says what it holds
#    [x] Show it to the person next to you
