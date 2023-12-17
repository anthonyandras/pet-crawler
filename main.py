import logging
import sys


def _init_logger():
    """
    Setup logging strategy for the crawler. Since logging is global, this
    should only be required once if the logging namespace does not change
    """
    logger = logging.getLogger("pet.crawler")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(module) s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def main():
    _init_logger()
    _logger = logging.getLogger("pet.crawler")
    _logger.info("test message")


if __name__ == "__main__":
    main()
