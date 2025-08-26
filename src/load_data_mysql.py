import pandas as pd
from sqlalchemy import create_engine

# 1. Load CSV file
csv_file = "C:/Users/adity/OneDrive/Desktop/credit_risk_analysis/data/processed/credit_risk_cleaned.csv"
df = pd.read_csv(csv_file)

# 2. Connect to MySQL (replace with your password and DB name)
engine = create_engine("mysql+pymysql://root:yourpassword@localhost/credit_risk_analysis")

# 3. Upload DataFrame to MySQL
df.to_sql("credit_risk", con=engine, if_exists="append", index=False)

print("✅ Data loaded successfully into MySQL table 'credit_risk'!")
