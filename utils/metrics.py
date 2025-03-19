def calculate_accuracy(true_labels, predicted_labels):
    """Calculate the accuracy of predictions."""
    correct = sum(t == p for t, p in zip(true_labels, predicted_labels))
    total = len(true_labels)
    return correct / total if total > 0 else 0