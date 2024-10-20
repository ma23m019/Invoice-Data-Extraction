# error_logging.py

def log_error(error_msg, invoice_name, field=None):
    if field:
        return f"Error: {error_msg} for field '{field}' in invoice '{invoice_name}'"
    return f"Error: {error_msg} in invoice '{invoice_name}'"
