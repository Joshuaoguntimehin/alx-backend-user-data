#!/usr/bin/env python3
"""import statement"""
import logging

PII_FIELDS = ('name', 'email', 'phone_number', 'address', 'ssn')

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class to redact PII fields in log messages """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields=None):
        """Initialize the formatter with the fields to redact"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields or []
        self.pii_fields = pii_fields

    def format(self, record: logging.LogRecord) -> str:
        """Redact sensitive information in the log message"""
        message = super().format(record)
        
        # Redact the fields in the message
        for field in self.fields:
            message = message.replace(field, self.REDACTION)

        # Redact PII_FIELDS in the message
        for pii in PII_FIELDS:
            message = message.replace(pii, '[REDACTED]')
        
        return message

def format(self, record):
        # Replace the PII fields in the log message with 'REDACTED'
        message = super().format(record)
        for field in self.pii_fields:
            message = message.replace(field, 'REDACTED')
        return message

def get_logger() -> logging.Logger:
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger