import pandas as pd
import pandas.testing as pdt
from process_employee import process_employee_data

def test_process_employee_data(tmp_path):
    # Create a temporary input CSV
    data = {
        "EmployeeID": [1, 2, 3],
        "Name": ["Alice", "Bob", "Charlie"],
        "Department": ["IT", "IT", "Sales"],
        "Salary": [60000, 80000, 50000],
        "JoiningDate": ["2020-01-01", "2019-03-05", "2021-06-10"],
        "PerformanceScore": [95, 85, 92],
    }
    df = pd.DataFrame(data)
    input_csv = tmp_path / "test_employee_data.csv"
    df.to_csv(input_csv, index=False)

    # Run the function
    result = process_employee_data(input_csv)

    # Expected output: only Alice (IT, Bonus > 5000)
    expected = pd.DataFrame({
        "EmployeeID": [1],
        "Name": ["Alice"],
        "Department": ["IT"],
        "Salary": [60000],
        "JoiningDate": ["2020-01-01"],
        "PerformanceScore": [95],
        "Bonus": [60000 * 0.10],
    })

    # Compare DataFrames
    pdt.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
    print("✅ test_process_employee_data passed!")


if __name__ == "__main__":
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmpdir:
        test_process_employee_data(tmp_path=pd.Path(tmpdir))
