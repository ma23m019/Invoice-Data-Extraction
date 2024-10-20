# main.py

from invoice_processor import process_invoices_batch
from data_saver import save_reports
from performance_metrics import calculate_performance_metrics

def main(invoice_files):
    extracted_data, error_logs = process_invoices_batch(invoice_files)
    save_reports(extracted_data, error_logs, output_file="invoice_data.csv", error_file="error_log.txt")
    overall_accuracy, field_accuracy = calculate_performance_metrics(extracted_data)
    
    print(f"\nOverall Accuracy: {overall_accuracy:.2f}%")
    print(f"Field Accuracy Breakdown: {field_accuracy}")


if __name__ == "__main__":
    invoice_files = ["C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv1.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv2.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv3.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv4.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv5.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv6.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv7.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv8.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv9.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv10.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv11.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv12.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv13.pdf", "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv14.pdf", 
                     "C:/Users/priya/OneDrive/Desktop/Zolvit/Data/inv15.pdf"]
    
    main(invoice_files)
