"""
Log Handlers

This module contains utility functions to set up logging
consistently
"""
import logging


def init_logging(app, logger_name: str):
    """Set up logging for production"""
    app.logger.propagate = False
    gunicorn_logger = logging.getLogger(logger_name)
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    # Make all log formats consistent
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s", "%Y-%m-%d %H:%M:%S %z"
    )
    for handler in app.logger.handlers:
        handler.setFormatter(formatter)
    app.logger.info("Logging handler established")


def test_method_not_allowed(self):
    """It should not allow an illegal method call"""
    resp = self.client.delete(BASE_URL)
    self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    BASE_URL = "/accounts"
