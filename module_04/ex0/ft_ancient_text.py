def cyber_archives_tester() -> None:
    """
    A simple test that open a basic file and print its content
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file_name = "ancient_fragment.txt"
    print(f"\nAccessing Storage Vault: {file_name}")
    try:
        file = open(file_name, 'r')
        print("Connection established...")
        content = file.read()
        file.close()
    except Exception as e:
        print("Error :", e)
    else:
        print("\nRECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    cyber_archives_tester()
