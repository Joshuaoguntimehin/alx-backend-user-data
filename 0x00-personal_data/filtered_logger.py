#!/usr/bin/env python3
"""import statement"""
import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields=None):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields or []

    def format(self, record: logging.LogRecord) -> str:
        # Redact fields that are in the fields list
        message = super().format(record)
        for field in self.fields:
            message = message.replace(field, self.REDACTION)
        return message
