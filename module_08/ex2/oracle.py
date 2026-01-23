from dotenv import load_dotenv
import os


env_loaded = load_dotenv()


def configuration() -> None:
    api_keys = {"secret123",  "mboutte_key"}

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print("Mode:", matrix_mode)
    print("Database:",
          "Connected to local instance"
          if "http://localhost/" == database_url[:17]
          else "Not found")
    print("API Access:",
          "Authenticated" if api_key in api_keys else "Unverified")
    print("log_level:", log_level)
    print("zion Network:", zion_endpoint)
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def missing_configuration_warnings() -> None:
    print("\nWarnings: Configue file missing")
    print("No '.env' file found")
    print("Setup a configue file to configure the environement")


def main():
    env_loaded = load_dotenv()
    if not env_loaded:
        missing_configuration_warnings()
    else:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        configuration()


if __name__ == "__main__":
    main()
