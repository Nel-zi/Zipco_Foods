# Importing necessary dependencies
import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import os



# Data Extraction
def run_transformation():
    data = pd.read_csv(r'zipco_transaction.csv')

    # Data cleaning and transformation
    # remove duplicates, i.e remove rows that are completely duplicate
    data.drop_duplicates(inplace=True)


    # Handle missing values numeric columns...
    # ...we do this by filling missing numeric values with the mean or median
    numeric_columns = data.select_dtypes(include= ['float64', 'int64']).columns
    for col in numeric_columns:
        data.fillna({col : data[col].mean()}, inplace=True)


    #Handle missing values of string/object columns...
    # ...we do this by filling missing string/object values with 'unknown'
    string_columns = data.select_dtypes(include = ['object']).columns
    for col in string_columns:
        data.fillna({col : 'Unknown'}, inplace=True)

    # Converting Date to a DateTime data type
    data['Date'] = pd.to_datetime(data['Date'])

    # Create the product table
    product = data[['ProductName']].drop_duplicates().reset_index(drop=True)
    product.index.name = 'ProductID'
    product = product.reset_index()

    # Create the customers Table
    customer = data[['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber',
                    'CustomerEmail']].drop_duplicates().reset_index(drop=True)
    customer.index.name = 'CustomerID'
    customer = customer.reset_index()

    # Staff Table
    staff = data[['Staff_Name', 'Staff_Email']].drop_duplicates().reset_index(drop=True)
    staff.index.name = 'StaffID'
    staff = staff.reset_index()

    # Transaction table
    transaction = data.merge(product, on=['ProductName'], how='left')\
                    .merge(customer, on=['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber', 'CustomerEmail'], how='left')\
                    .merge(staff, on=['Staff_Name', 'Staff_Email'], how='left')

    transaction.index.name = 'TransactionID'
    transaction = transaction.reset_index()\
                            [['Date', 'TransactionID', 'ProductID', 'CustomerID', 'StaffID', 'Quantity', 'UnitPrice', 'StoreLocation',
                                'PaymentType', 'PromotionApplied', 'Weather', 'Temperature', 'StaffPerformanceRating', 'CustomerFeedback',
                                'DeliveryTime_min', 'OrderType', 'DayOfWeek', 'TotalSales']]

    # Save data as csv files
    data.to_csv('Clean_dataset\cleaned_zipco_foods_data.csv', index=False)
    product.to_csv('Clean_dataset\product.csv', index=False)
    customer.to_csv('Clean_dataset\customer.csv', index=False)
    staff.to_csv('Clean_dataset\staff.csv', index=False)
    transaction.to_csv('Clean_dataset/transaction.csv', index=False)

    print('Data Cleaning and Transformation completed successfully')




# A MORE ROBUST CODE
# import pandas as pd
# import os

# def run_transformation():
#     try:
#         data_path = os.path.join(os.getcwd(), 'zipco_transaction.csv')
#         if not os.path.exists(data_path):
#             raise FileNotFoundError(f"File not found: {data_path}")

#         data = pd.read_csv(data_path)

#         # Data cleaning
#         data.drop_duplicates(inplace=True)

#         numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
#         for col in numeric_columns:
#             if data[col].isnull().any():
#                 data[col].fillna(data[col].mean(), inplace=True)

#         string_columns = data.select_dtypes(include=['object']).columns
#         for col in string_columns:
#             data.fillna({col: 'Unknown'}, inplace=True)

#         data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

#         # Creating output folder
#         output_dir = 'Clean_dataset'
#         os.makedirs(output_dir, exist_ok=True)

#         # Creating tables
#         product = data[['ProductName']].drop_duplicates().reset_index(drop=True)
#         product.index.name = 'ProductID'
#         product = product.reset_index()

#         customer = data[['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber', 'CustomerEmail']].drop_duplicates().reset_index(drop=True)
#         customer.index.name = 'CustomerID'
#         customer = customer.reset_index()

#         staff = data[['Staff_Name', 'Staff_Email']].drop_duplicates().reset_index(drop=True)
#         staff.index.name = 'StaffID'
#         staff = staff.reset_index()

#         transaction = data.merge(product, on=['ProductName'], how='left')\
#                           .merge(customer, on=['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber', 'CustomerEmail'], how='left')\
#                           .merge(staff, on=['Staff_Name', 'Staff_Email'], how='left')

#         transaction.index.name = 'TransactionID'
#         transaction = transaction.reset_index()

#         # Saving transformed data
#         product.to_csv(os.path.join(output_dir, 'product.csv'), index=False)
#         customer.to_csv(os.path.join(output_dir, 'customer.csv'), index=False)
#         staff.to_csv(os.path.join(output_dir, 'staff.csv'), index=False)
#         transaction.to_csv(os.path.join(output_dir, 'transaction.csv'), index=False)

#         print('Data Cleaning and Transformation completed successfully')

#     except Exception as e:
#         print(f'Error during transformation: {e}')
