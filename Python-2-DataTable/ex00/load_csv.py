import pandas as pd


def load(path: str):
    """
    Loads a CSV file and returns its content as a DataFrame or NumPy array.

    Parameters:
    path (str): Path to the CSV file.

    Returns:
    pd.DataFrame or np.ndarray: CSV data.
                                 Returns an empty DataFrame if an error occurs.
    """
    try:
        # Load CSV with pandas (handles headers, mixed types)
        df = pd.read_csv(path)
        print(f"CSV loaded successfully: {df.shape[0]} rows x {df.shape[1]} columns")
        return df

    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty")
    except pd.errors.ParserError:
        print("Error: CSV is malformed")
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Return empty DataFrame on error
    return pd.DataFrame()
