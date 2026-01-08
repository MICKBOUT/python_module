def cyber_archives_tester() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    text = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Mboutte"""

    try:
        file = open(file_name, "w")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        file.write(text)
        print(text)
        file.close()
    except Exception as e:
        print("Error :", e)
    else:
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    cyber_archives_tester()
