import logging

def setup_logging(log_level=logging.INFO):
    """Set up logging with a specific format and level."""
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)