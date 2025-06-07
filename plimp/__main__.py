import logging

from plimp.utils.functions import configure_logging
from dotenv import load_dotenv

# configure logging
configure_logging()
logger = logging.getLogger(__name__)

load_dotenv()
# Define global variables here that map to the env vars
# Example:
# EXAMPLE_ENV_VAR = os.getenv("EXAMPLE_ENV_VAR", "")


def main():
    logger.info("Running plimp...")

    # Do stuff

    logger.info("plimp executed successfully.")


if __name__ == "__main__":
    main()
