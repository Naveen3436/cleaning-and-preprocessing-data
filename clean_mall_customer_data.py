import pandas as pd

# Load the raw dataset
try:
    df = pd.read_csv('Mall_Customers.csv')
    print("✅ Dataset loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'Mall_Customers.csv' not found.")
    exit()

# 1. Display and check for missing values
missing_values = df.isnull().sum()
print("\n🔍 Missing values in each column:\n", missing_values)

# 2. Drop rows with missing values (if any)
df.dropna(inplace=True)
print("✅ Dropped rows with missing values.")

# 3. Remove duplicate rows
df.drop_duplicates(inplace=True)
print("✅ Removed duplicate rows.")

# 4. Standardize text values (e.g., Gender)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.lower()
    df['Gender'] = df['Gender'].replace({'male': 'Male', 'female': 'Female'})
    print("✅ Standardized gender column.")
else:
    print("⚠️ Warning: 'Gender' column not found.")

# 5. Rename column headers to lowercase and underscore format
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print("✅ Renamed column headers.")

# 6. Fix data types (if columns exist)
expected_columns = ['age', 'annual_income_(k$)', 'spending_score_(1-100)']
for col in expected_columns:
    if col in df.columns:
        df[col] = df[col].astype(int)
        print(f"✅ Converted '{col}' to integer.")
    else:
        print(f"⚠️ Warning: Expected column '{col}' not found.")

# 7. Save the cleaned dataset
output_file = 'Mall_Customers_Cleaned.csv'
df.to_csv(output_file, index=False)
print(f"\n✅ Data cleaned successfully and saved as '{output_file}'")
