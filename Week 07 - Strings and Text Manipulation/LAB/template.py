"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT      
Date  :

Run it:   python template.py

"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) and status_of(...)
def parse_line(raw_line):
    """Clean and parse one raw, messy line into a dict."""
    # Strip whitespace and lowercase the whole line
    clean_line = raw_line.strip().lower()
    
    # Split into 3 parts by comma
    parts = clean_line.split(",")
    
    # Extract values, strip spaces around them, and split by '=' to get the number
    label = parts[0].strip()
    value = float(parts[1].split("=")[1].strip())
    limit = float(parts[2].split("=")[1].strip())
    
    # Return the clean dictionary
    return {"label": label, "value": value, "limit": limit}

def status_of(value, limit):
    """Return the status based on the percentage."""
    percent = (value / limit) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

# ====================================================================== INPUT
# 2. Your raw, messy records.
# Excellent: save these lines to a file and load them with open() / a for loop.
# (I'm putting them directly in a list here so we don't get file errors)

raw_records = [
    " Srv-01 , used=87 , total=100 ",
    "srv-02,used=150,total=100",
    "SRV-03, used=45 , total=100",
    "srv-04,used=95,total=100",
    " Srv-05 , used=110 , total=110 ",
    "srv-06,used=abc,total=100"
]

# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.


print("--- Parsed Records ---")
total_records = 0
flagged_count = 0

for raw_record in raw_records:
    try:
        # Parse the line
        clean_dict = parse_line(raw_record)
        
        # Get the status
        status = status_of(clean_dict["value"], clean_dict["limit"])
        
        # Print the results
        print(f"{clean_dict} -> Status: {status}")
        
        total_records += 1
        if status == "OVER LIMIT":
            flagged_count += 1
            
    except ValueError:
        print(f"ERROR: Could not convert numbers in line: '{raw_record.strip()}'")

print("\n--- Summary ---")
print(f"Total valid records processed: {total_records}")
print(f"Total records flagged (OVER LIMIT): {flagged_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records
#    [x] Run it with a value that will not convert to a number - write the
#        error down
#    [x] Check every function does one job, with a docstring
