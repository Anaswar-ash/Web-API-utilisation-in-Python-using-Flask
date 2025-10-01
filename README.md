
# Python CSV Data Cleaner API

A simple web API built with Flask to clean and analyze CSV data.

## Features

-   Removes duplicate rows.
-   Corrects specified columns to a numeric type.
-   Fills missing values in numerical columns with the column's mean.
-   Provides a data summary of the cleaned data.

## Project Structure

```
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── sample_data.csv
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── data_cleaner.py
│   ├── main.py
├── tests
│   └── test_data_cleaner.py
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Web-API-utilisation-in-Python-using-Flask
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**
    -   Copy the `.env.example` file to `.env`:
        ```bash
        cp .env.example .env
        ```
    -   Update the `.env` file with your secret key.

5.  **Run the application:**
    ```bash
    python src/main.py
    ```

## Running the Tests

To run the tests, use `pytest`:

```bash
pytest
```

## API Endpoints

### `/upload`

-   **Method:** `POST`
-   **Content-Type:** `multipart/form-data`
-   **Form Data:**
    -   `file`: The CSV file to be processed.
    -   `column_to_correct` (optional): The name of the column to convert to a numeric type.

-   **Example using `curl`:**
    ```bash
    curl -X POST -F "file=@/path/to/your/sample_data.csv" -F "column_to_correct=Salary" http://127.0.0.1:5000/upload
    ```

### Example of a Successful JSON Response

```json
{
  "cleaned_data_head": [
    {
      "Name": "Alice",
      "Age": 28.0,
      "Salary": 60000.0,
      "Department": "HR"
    },
    {
      "Name": "Bob",
      "Age": 34.0,
      "Salary": 71400.0,
      "Department": "Engineering"
    },
    {
      "Name": "Charlie",
      "Age": 42.0,
      "Salary": 85000.0,
      "Department": "Engineering"
    },
    {
      "Name": "Diana",
      "Age": 30.0,
      "Salary": 62000.0,
      "Department": "Marketing"
    },
    {
      "Name": "Eve",
      "Age": 33.5,
      "Salary": 75000.0,
      "Department": null
    }
  ],
  "data_summary": {
    "Age": {
      "count": 6.0,
      "mean": 33.5,
      "std": 5.54075806363402,
      "min": 28.0,
      "25%": 29.5,
      "50%": 32.0,
      "75%": 36.5,
      "max": 42.0
    },
    "Salary": {
      "count": 5.0,
      "mean": 71400.0,
      "std": 10430.72384889523,
      "min": 60000.0,
      "25%": 62000.0,
      "50%": 75000.0,
      "75%": 85000.0,
      "max": 85000.0
    }
  },
  "message": "File processed successfully",
  "original_missing_values": {
    "Name": 0,
    "Age": 2,
    "Salary": 2,
    "Department": 1
  }
}
```
