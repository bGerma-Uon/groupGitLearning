def load_data():
    return ["record1", "record2", "record3"]

def clean_data(records):
    return [r.upper() for r in records]

# Team B to this filter function after clean_data
def filter_data(records):
    return [r for r in records if "1" in r]

# Team B to update main as shown below
def main():
    records = load_data()
    cleaned = clean_data(records)
    filtered = filter_data(cleaned)
    print("Processed records:", cleaned)
    print("Filtered:", filtered)

if __name__ == "__main__":
    main()