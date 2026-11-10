"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT      
Date  :01/11/2026

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
# 1. Write the functions for the "Excellent" tier.

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the formatted report."""
    print()
    print("=" * 34)
    print(f" RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f" {'Used':<10} : {value:>10.2f}")
    print(f" {'Total':<10} : {limit:>10.2f}")
    print(f" {'Free':<10} : {difference:>10.2f}")
    print(f" {'Percent':<10} : {percent:>10.2f} %")
    print(f" {'Status':<10} : {status:>10}")
    print("=" * 34)

# ==================================================================== INPUT
# 2. Work out the difference and the percentage using the check() function.

# Wrap the input/process/output steps in a loop.

over_limit_count = 0

while True:
    # 1. Ask for your three values.
    label = input("\nEnter hostname (or type 'quit' to stop): ")
    
    # Stop the loop if the user types 'quit'
    if label.lower() == 'quit':
        break
        
    value = float(input("Enter GB used: "))
    limit = float(input("Enter total GB: "))

    difference, percent = check(value, limit)

# ================================================================== PROCESS
# 3. Decide a status using the status_of() function.
status = status_of(percent)

# Keep track of OVER LIMIT records for the final summary
if status == "OVER LIMIT":
        over_limit_count += 1

# =================================================================== OUTPUT
# 4. Print the report.
print_report(label, value, limit, difference, percent, status)

# This print MUST be outside the loop (unindented) so it only runs once at the end.
print(f"\nSession complete. Total records OVER LIMIT: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [x] Run it three times with different numbers
#    [x] Run it with a total of 0 and note the error (do not fix it yet)
#    [x] Check every function does one job - if a function both calculates
#        and prints, split it
