import sys


def cyber_archives_tester() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    try:
        archivist_id = input("Input Stream active. Enter archivist ID: ")
        status_report = input("Input Stream active. Enter status report: ")
    except Exception as e:
        sys.stderr.write(f"Error :{e}\n")
    else:
        sys.stdout.write(
            f"\n[STANDARD] Archive status from {archivist_id}: "
            f"{status_report}\n"
        )
        sys.stderr.write(
            "[ALERT] System diagnostic: Communication channels verified\n")
        sys.stdout.write("[STANDARD] Data transmission complete\n")

        sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    cyber_archives_tester()
