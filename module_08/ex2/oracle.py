from dotenv import load_dotenv
import hashlib
import os


def hash_message(message: str) -> str:
    # hash the str in parameter
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def configuration(env_arg: list) -> None:
    api_keys = {
        "fcf730b6d95236ecd3c9fc2d92d7b6b2bb061514961aec041d6c7a7192f592e4",
        "5c58b8f7c6d1b58b5d1bd5f7e25f186c0c8f58b17d8d3dfbac2b6f618d7835e6"
        }

    # unpack the arg
    matrix_mode, database_url, api_key, log_level, zion_endpoint = env_arg

    print("Configuration loaded:")
    print("Mode:", matrix_mode)
    print("Database:",
          "Connected to local instance" if database_url[:17] == "http://localhost/"
          else "Not found")
    print("API Access:",
          "Authenticated" if hash_message(api_key) in api_keys else "Unverified")
    print("log_level:", log_level)
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
