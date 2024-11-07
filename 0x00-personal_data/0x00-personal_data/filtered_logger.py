#!/usr/bin/env python3
import re
"""import statement"""
def filter_datum(fields, redaction, message, separator):
    return re.sub(rf'({"|".join(fields)})=.*?(?={separator}|\Z)', lambda x: f"{x.group(1)}={redaction}", message)