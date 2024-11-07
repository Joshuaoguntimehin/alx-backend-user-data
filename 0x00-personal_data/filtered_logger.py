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
    def format(self, record: logging.LogRecord) -> str:
        # Custom formatting logic
        log_message = super().format(record)  # Use the default format first
        
        # Add custom information (e.g., include a custom log prefix or timestamp)
        custom_message = f"CustomPrefix: {log_message}"

        return custom_message

