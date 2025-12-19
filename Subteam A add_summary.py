# Team A to add driectly after clean_data
def summarise_data(records):
    return {
        "count": len(records),
        "sample": records[:2]
    }
# Team A to update main as shown below
def main():
    records = load_data()
    cleaned = clean_data(records)
    summary = summarise_data(cleaned)
    print("Processed records:", cleaned)
    print("Summary:", summary)
