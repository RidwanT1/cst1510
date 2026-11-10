"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT      
Date  : 31/10/2026

Run it:   python template.py

"""
# Initialize the counter for the "Excellent" tier before the loop starts
over_limit_count = 0

# ==================================================================== INPUT
# 1. Ask for your three values.
# The "Excellent" tier requires wrapping sections 1-4 in a loop.

while True:
    label = input("\nEnter hostname (or type 'quit' to stop): ")
    
    # Stop the loop if the user types 'quit'
    if label.lower() == 'quit':
        break
        
    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.      

difference = value - limit
percent = (value / limit) * 100

# 3. Decide a status and store it in a variable called status.
# Using if / elif / else for a 3-tier status as required by "Typical and above"

if percent >= 100:
    status = "OVER LIMIT"
    # Increment our counter if it's over the limit
    over_limit_count += 1
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# All numbers show 2 decimal places and are right-aligned so they line up
print(f" {'Used':<10} : {value:>10.2f}")
print(f" {'Total':<10} : {limit:>10.2f}")
print(f" {'Free':<10} : {difference:>10.2f}")
print(f" {'Percent':<10} : {percent:>10.2f} %")
print(f" {'Status':<10} : {status:>10}")

print("=" * 34)

# This prints once, after the loop ends, for the "Excellent" tier
print(f"\nSession complete. Total records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and note the error (do not fix it yet)
#    [x] Check every variable name says what it holds
