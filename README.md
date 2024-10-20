# Invoice Data Extraction System

This project provides a system for extracting relevant information from invoice PDFs. It supports various types of PDFs (text-based, scanned, or mixed) and allows for processing both local files and invoices accessible via URLs without downloading them.

## Installation

1. Clone the repository:

2. Install dependencies:

## Usage

1. Update the `invoice_sources` list in `main.py` with your invoice file paths.
2. Run the application:

## Modules

- `invoice_processor.py`: Handles the extraction of data from invoices.
- `confidence_assessment.py`: Contains logic for assessing confidence scores.
- `error_logging.py`: Logs errors encountered during processing.
- `data_saver.py`: Saves extracted data to CSV files.
- `performance_metrics.py`: Calculates performance metrics for extracted data.

## License

This project is licensed under the MIT License.
