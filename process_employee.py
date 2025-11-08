import pandas as pd

def process_employee_data(input_path):
    # Read CSV file
    df = pd.read_csv(input_path)
    
    # Add Bonus column
    df["Bonus"] = df.apply(
        lambda row: row["Salary"] * 0.10 if row["PerformanceScore"] > 90 else row["Salary"] * 0.05,
        axis=1
    )
    
    # Filter IT employees with Bonus > 5000
    filtered_df = df[(df["Department"] == "IT") & (df["Bonus"] > 5000)]
    
    return filtered_df


if __name__ == "__main__":
    input_file = "employee_data.csv"
    output_file = "filtered_employees.csv"
    
    # Process data
    result = process_employee_data(input_file)
    
    # Save filtered data to CSV
    result.to_csv(output_file, index=False)
    
    print("Employee data processed and saved to filtered_employees.csv")
