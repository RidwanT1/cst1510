"""
RECORD CHECK  -  my version
===========================

Name  : Ridwan Tarafder 
Lane  : IT      
Date  : 03/11/2026

Run it:   python template.py

"""

# ====================================================================== CLASS
# 1. Define a class called Record.
# Excellent: add over_limit_count as a class-level running total.

class Record:
    """Represents a single record check."""
    
    # Class-level variable to track OVER LIMIT records across all instances
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize the record with label, value, and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage."""
        percent = (self.value / self.limit) * 100
        
        if percent >= 100:
            # Increment the class-level counter when a record is over the limit
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"

# ==================================================================== RECORDS
# 2. Create your records.
# Excellent: write load_records(path) that reads lines and returns a list of Record objects.

def load_records(path):
    """Load records from a CSV file into a list of Record objects."""
    records = []
    try:
        with open(path, "r") as f:
            for line in f:
                if not line.strip():
                    continue
                
                # Split line: label,value,limit
                parts = line.strip().split(",")
                
                # Create a Record object and add it to the list
                record = Record(parts[0], float(parts[1]), float(parts[2]))
                records.append(record)
    except FileNotFoundError:
        print(f"\nERROR: The file '{path}' was not found.")
        
    return records

# Call the function to load the records from your data file
records = load_records("data.txt")

# ==================================================================== OUTPUT
# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # Calculate extra stats for the report
    difference = record.value - record.limit
    percent = (record.value / record.limit) * 100
    
    # Call status() ONCE, store it in a variable, and use that variable
    current_status = record.status()
    
    print(f" {'Used':<10} : {record.value:>10.2f}")
    print(f" {'Total':<10} : {record.limit:>10.2f}")
    print(f" {'Free':<10} : {difference:>10.2f}")
    print(f" {'Percent':<10} : {percent:>10.2f} %")
    print(f" {'Status':<10} : {current_status:>10}")
    
    print("=" * 34)

# Print the final count after the loop ends
print(f"\nSession complete. Total records OVER LIMIT: {Record.over_limit_count}")

# ==========================================================================
# 4. Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#    [x] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [x] Check every method and __init__ has a one-line docstring
