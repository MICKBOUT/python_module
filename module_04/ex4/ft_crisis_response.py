
def crisis_protocol(file_name: str) -> None:
    """
    Take a str 'file_name' open it read the content
    if an error occur, manage the situation
    """
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - ''{data}''")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print("RESPONSE:", e)
        print("STATUS: Crisis handled")
    else:
        print("STATUS: Normal operations resumed")


def crisis_response_tester():
    """
    test for crisis sitiation with multiple file
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_name = "lost_archive.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    crisis_protocol(file_name)

    file_name = "classified_vault.txt"
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    crisis_protocol(file_name)

    file_name = "standard_archive.txt"
    print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
    crisis_protocol(file_name)

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response_tester()
