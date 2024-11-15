# Ultimate Data Pre-Processing Tool: Data Cleaning Master

**Data Cleaning Master** is a Python-based application engineered to simplify and accelerate dataset cleaning. By efficiently tackling duplicates and missing values, it delivers a polished dataset ready for analysis in just moments. Designed with user-friendliness in mind, this tool is optimized for performance, rigorously tested, and capable of handling extensive datasets with ease.

## Why Choose Data Cleaning Master?
This application is a robust solution for cleaning datasets with thousands of rows. It ensures error-free execution while:
- Preserving a backup of duplicate entries for future reference.
- Replacing missing numeric values with column averages.
- Removing rows containing missing non-numeric data.
These features make it an invaluable resource for data analysts and scientists during pre-processing.

---

## Core Objectives
The primary goals of this project include:
- Seamless dataset loading in multiple formats (CSV and Excel).
- Automated detection and backup of duplicate entries.
- Intelligent handling of missing values:
  - Replacing missing numeric data with column means.
  - Dropping rows with non-numeric missing values.
- Exporting both cleaned datasets and backup files of duplicates for review.

---

## Requirements
To use Data Cleaning Master, ensure the following dependencies are installed:
- **Python 3.x**
- **Pandas**
- **Numpy**
- **Openpyxl**
- **Xlrd**
- **OS library**
- **Jupyter Notebook** (optional, for testing)

---

## Step-by-Step Workflow
### 1. Input Verification
- Users provide the dataset path and file name.
- The application validates the path and file type (CSV or Excel).

### 2. Duplicate Handling
- Identifies and saves duplicates in a separate file `{dataset_name}_duplicates.csv`.
- Removes duplicates from the main dataset.

### 3. Resolving Missing Values
- Numeric columns: Fills missing values with column averages.
- Non-numeric columns: Drops rows containing missing entries.

### 4. Exporting Cleaned Data
- Saves the cleaned dataset as `{dataset_name}_Clean_data.csv`.
- Confirms the successful cleaning process.

### 5. Testing and Optimization
- Extensively tested on datasets exceeding 10,000 rows, delivering consistent results within seconds.
- Performance validated through Jupyter Notebook for smooth integration with data science workflows.

---

## Key Features
- **Lightning-Fast Processing**: Handles large datasets swiftly and efficiently.
- **Duplicate Backup**: Retains all duplicates for audit trails.
- **Smart Missing Value Handling**: Automates numeric imputation and removes problematic non-numeric rows.
- **User-Centric Design**: Provides clear instructions and updates at every stage.
- **Multi-Format Support**: Compatible with both CSV and Excel formats.

---

## How to Use
1. Run the program in a Python environment:
   ```bash
   python data_Cleaner.py
   ```
2. Enter the dataset path and file name when prompted.
3. The tool cleans the dataset and exports the results.

---

## Example Execution
```plaintext
Welcome to Data Cleaning Master!
Please enter dataset path: /usr/Desktop/amazon.csv
Please enter dataset name: amazon_sales_data
```
**Output:**
- Duplicate records saved as: `amazon_sales_data_duplicates.csv`
- Cleaned data saved as: `amazon_sales_data_Clean_data.csv`

---

## Final Notes
Data Cleaning Master streamlines data preparation, offering accuracy, speed, and convenience. It’s the perfect companion for anyone looking to elevate their data analysis workflows with clean, reliable datasets.
