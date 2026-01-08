def vault_security_tester() -> None:
    """
    exemple of how with statment work in action
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", 'r') as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            print(file.read())
    except Exception as e:
        print("Error:", e)

    print("\nSECURE PRESERVATION:")
    try:
        with open("security_protocols.txt", 'w') as file:
            print("[CLASSIFIED] New security protocols archived")
            file.write("[CLASSIFIED] New security protocols archived")
    except Exception as e:
        print("Error:", e)

    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security_tester()
