import time

def fetch_data(param: str) -> str:
    print(f"starting to fetch {param}...")
    time.sleep(1)
    print(f"successfully fetched {param}...")
    return f"result of {param}"

def main():
    result1 = fetch_data("foo")
    result2 = fetch_data("bar")
    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()
    results = main()
    t2 = time.perf_counter()
    print(f"Finished in {t2-t1:.2f} seconds")