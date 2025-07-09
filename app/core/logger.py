import logging
from logging.config import dictConfig

def setup_logger():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] [%(levelname)s] %(name)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console"],
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",
            },
            "uvicorn.error": {
                "level": "INFO",
            },
            "uvicorn.access": {
                "level": "WARNING",
            },
        },
    })

    return logging.getLogger("app")
