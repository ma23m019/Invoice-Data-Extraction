# invoice_processor.py

import pdfplumber
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from confidence_assessment import confidence_score
from error_logging import log_error

def process_invoice(file_path):
    invoice_name = file_path.split('/')[-1]  # Extract file name for logging
    try:
        with pdfplumber.open(file_path) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()
    except Exception as e:
        return None, log_error(f"Failed to read file: {str(e)}", invoice_name)

    try:
        # Define regex patterns
        invoice_number_pattern = r"Invoice #: (INV-\d+)"
        invoice_date_pattern = r"Invoice Date: (\d{2} \w+ \d{4})"
        due_date_pattern = r"Due Date: (\d{2} \w+ \d{4})"
        customer_name_pattern = r"Customer Details:\s*([A-Za-z\s]+)"
        ph_num_pattern = r"Ph: (\d+)"
        total_amount_pattern = r"Total ₹([\d,.]+)"
        taxable_amount_pattern = r"Taxable Amount ₹([\d,.]+)"

        
        # Extract data with fallback to "N/A"        
        invoice_number = re.search(invoice_number_pattern, text).group(1) if re.search(invoice_number_pattern, text) else "N/A"
        invoice_date = re.search(invoice_date_pattern, text).group(1) if re.search(invoice_date_pattern, text) else "N/A"
        due_date = re.search(due_date_pattern, text).group(1) if re.search(due_date_pattern, text) else "N/A"
        customer_name = re.search(customer_name_pattern, text).group(1) if re.search(customer_name_pattern, text) else "N/A"
        ph_num = re.search(ph_num_pattern, text).group(1) if re.search(ph_num_pattern, text) else "N/A"
        total_amount = re.search(total_amount_pattern, text).group(1) if re.search(total_amount_pattern, text) else "N/A"
        taxable_amount = re.search(taxable_amount_pattern, text).group(1) if re.search(taxable_amount_pattern, text) else "N/A"

        # Calculate confidence scores
        confidence_scores = {
            "Invoice Number": confidence_score(invoice_number, "Invoice Number"),
            "Invoice Date": confidence_score(invoice_date, "Invoice Date"),
            "Due Date": confidence_score(due_date, "Due Date"),
            "Customer Name": confidence_score(customer_name, "Customer Name"),
            "Phone Number": confidence_score(ph_num, "Phone Number"),
            "Total Amount": confidence_score(total_amount, "Total Amount"),
            "Taxable Amount": confidence_score(taxable_amount, "Taxable Amount"),
        }

        # Return extracted data
        return {
            "Invoice Number": invoice_number,
            "Invoice Date": invoice_date,
            "Due Date": due_date,
            "Customer Name": customer_name,
            "Phone Number": ph_num,
            "Total Amount": total_amount,
            "Taxable Amount": taxable_amount,
            "Confidence Scores": confidence_scores
        }, None

    except Exception as e:
        return None, log_error(f"Extraction failed: {str(e)}", invoice_name)


def process_invoices_batch(file_paths):
    extracted_data = []
    error_logs = []

    with ThreadPoolExecutor(max_workers=4) as executor:  # Adjust max_workers for performance
        futures = {executor.submit(process_invoice, file): file for file in file_paths}
        for future in as_completed(futures):
            result, error = future.result()
            if result:
                extracted_data.append(result)
            if error:
                error_logs.append(error)

    return extracted_data, error_logs
