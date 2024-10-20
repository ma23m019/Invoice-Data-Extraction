# data_saver.py

import pandas as pd

def save_reports(invoices_data, error_logs, output_file='invoice_data.csv', error_file='error_log.txt'):
    # Save extracted data to CSV
    df = pd.DataFrame(invoices_data)

    # Display the data that will be saved
    print("\nData to be saved to CSV:")
    print(df)

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"\nData successfully saved to {output_file}")

    # Save error logs
    with open(error_file, 'w') as f:
        for error in error_logs:
            f.write(f"{error}\n")
    print(f"\nError logs saved to {error_file}")
