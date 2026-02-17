import os

LOG_TYPES = ["INFO", "WARNING", "ERROR"]


def analyze_log(filepath):
    counts = {key: 0 for key in LOG_TYPES}
    unknown = 0
    total = 0

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            total += 1

            matched = False
            for key in LOG_TYPES:
                if line.upper().startswith(key):
                    counts[key] += 1
                    matched = True
                    break

            if not matched:
                unknown += 1

    return counts, unknown, total


def main():
    path = input("Enter log file path: ").strip()

    if not os.path.exists(path):
        print("File not found.")
        return

    try:
        counts, unknown, total = analyze_log(path)
    except Exception as e:
        print("Could not read file:", e)
        return

    print("\n--- Log Summary ---")
    print("Total lines:", total)

    for key in LOG_TYPES:
        print(f"{key}: {counts[key]}")

    print("Unknown:", unknown)


if __name__ == "__main__":
    main()
