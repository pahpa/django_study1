LOGFORMATDATE = "%d/%m/%Y %H:%M:%S"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] (%(name)s) %(module)s::%(funcName)s %(lineno)-4d %(levelname)-8s %(message)s",
            "datefmt": LOGFORMATDATE,
        },
        "simple": {
            "format": "[%(asctime)s] (%(name)s) %(levelname)s %(message)s",
            "datefmt": LOGFORMATDATE,
        },
        "colored": {
            "()": "djangocolors_formatter.DjangoColorsFormatter",
            "format": "[%(asctime)s] (%(name)s) %(module)s::%(funcName)s %(lineno)-4d %(levelname)-8s %(message)s",
            "datefmt": LOGFORMATDATE,
        },
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "debug": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "consoleverbose": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "consolecolore": {
            "class": "logging.StreamHandler",
            "formatter": "colored",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["consolecolore"],
            "propagate": True,
            "level": "INFO",
        },
        "wikiapi": {
            "handlers": ["consolecolore"],
            "propagate": False,
            "level": "DEBUG",
        },
    },
}
