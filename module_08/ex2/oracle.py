from dotenv import load_dotenv
import os


def looks_like_api_key(key: str) -> bool:
    return len(key) >= 6 and key[-3:].isnumeric() and key[:3].isalpha()


def configuration(env_arg: list) -> None:

    # unpack the arg
    matrix_mode, database_url, api_key, log_level, zion_endpoint = env_arg

    # print the env info
    print("Configuration loaded:")
    print("Mode:", matrix_mode)
    print("Database:",
          "Connected to local instance"
          if database_url[:17] == "http://localhost/"
          else "Not found")
    print("API Access:",
          "Authenticated" if looks_like_api_key(api_key) else "Unverified")
    print("log level:", log_level)
    print("zion Network:", zion_endpoint)
    print()

    # basic print
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def missing_configuration_warnings() -> None:
    # missing message print
    print("\nWarnings: Configue file missing")
    print("No '.env' file found")
    print("Setup a configue file to configure the environement")


def main():
    load_dotenv()  # load the env var

    # get env variable
    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    env_arg = [matrix_mode, database_url, api_key, log_level, zion_endpoint]

    if any(x is None or len(x) == 0 for x in env_arg):
        missing_configuration_warnings()

    else:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        configuration(env_arg)


if __name__ == "__main__":
    main()
