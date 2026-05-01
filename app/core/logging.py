import logging
import sys
import structlog
import logging


def setup_logging():

    logging.basicConfig(level=logging.INFO)
    
    
    logger = logging.getLogger("autobackend")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s %(name)s - %(message)s"
    )

    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    logger.info("Logging system initialized")
    

    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ]
    )

    return structlog.get_logger()