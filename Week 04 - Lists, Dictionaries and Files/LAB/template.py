"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT     
Date  : 02/11/2026

Run it:   python template.py


"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3

def check_record(value, limit):
    """Calculate the difference, percentage, and status."""
    difference = value - limit
    percent = (value / limit) * 100
    
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
        
    return difference, percent, status

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

# ====================================================================== STORE
# 2. Get your records into a list of dicts.
# Excellent: Write a function load_records(path) that reads from a file.

def load_records(path):
    """Load records from a CSV file into a list of dictionaries."""
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                # Skip empty lines just in case
                if not line.strip():
                    continue
                    
                # Split the line by comma: label,value,limit
                parts = line.strip().split(",")
                
                # Build the dictionary and convert numbers to float
                record = {
                    "label": parts[0],
                    "value": float(parts[1]),
                    "limit": float(parts[2])
                }
                records.append(record)
    except FileNotFoundError:
        print(f"\nERROR: The file '{path}' was not found.")
        print("Starting with an empty list instead.")
        
    return records

# Call the function to load the data
records = load_records("data.txt")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
# Excellent: Also write results to a new file, and keep count of OVER LIMIT.

over_limit_count = 0

# Open a new file to write the results
with open("results.txt", "w") as out_file:
    
    for record in records:
        label = record["label"]
        value = record["value"]
        limit = record["limit"]
        
        # Run the logic
        difference, percent, status = check_record(value, limit)
        
        # Print to the screen
        print_report(label, value, limit, difference, percent, status)
        
        # Write to the results.txt file
        out_file.write(f"{label},{status}\n")
        
        # Keep track of OVER LIMIT
        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"\nProcessing complete. Total records OVER LIMIT: {over_limit_count}")
print("Results have been saved to results.txt")

# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers are correct by hand
#    [x] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [x] Check every function still does one job
