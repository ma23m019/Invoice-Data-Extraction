# performance_metrics.py

def calculate_performance_metrics(extracted_data):
    total_confidence_scores = {
        "Invoice Number": 0,
        "Invoice Date": 0,
        "Due Date": 0,
        "Customer Name": 0,
        "Total Amount": 0,
        "Taxable Amount": 0,
    }
    total_count = len(extracted_data)

    for invoice in extracted_data:
        for field in total_confidence_scores.keys():
            if "Confidence Scores" in invoice and field in invoice["Confidence Scores"]:
                total_confidence_scores[field] += invoice["Confidence Scores"][field]

    # Calculate average confidence scores
    field_accuracy = {field: total_confidence_scores[field] / total_count if total_count > 0 else 0 for field in total_confidence_scores}
    overall_accuracy = sum(field_accuracy.values()) / len(field_accuracy) if field_accuracy else 0

    return overall_accuracy, field_accuracy
