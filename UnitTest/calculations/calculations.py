import statistics

def calculate_statistics(data):
    """
    Calculates mean, median, and standard deviation of numerical data.

    Args:
        data (list): List of numerical data.

    Returns:
        dict: A dictionary containing mean, median, and standard deviation.
    """
    if not data:
        raise ValueError("Input list is empty")

    mean = sum(data) / len(data)
    median = statistics.median(data)
    std_dev = statistics.stdev(data)

    return {"mean": mean, "median": median, "std_dev": std_dev}
