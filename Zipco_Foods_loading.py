# Importing necessary dependencies
import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import os

# Data Loading
def run_loading():
    # Loading the dataset
    data = pd.read_csv(r'cleaned_zipco_foods_data.csv')
    product = pd.read_csv(r'product.csv')
    staff = pd.read_csv(r'staff.csv')
    customer = pd.read_csv(r'customer.csv')
    transaction = pd.read_csv(r'transaction.csv')


    # Data Loading
    # Loading the environment variables from .env files
    load_dotenv()

    connect_str = os.getenv('AZURE_CONNECT_STR')
    container_name = os.getenv('CONTAINER_NAME')

    # Create a BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    # Load data to Azure Blob Storage
    files = [
        (data, 'cleandataset/cleaned_zipco_foods_data.csv'),
        (product, 'cleandataset/product.csv'),
        (customer, 'cleandataset/customer.csv'),
        (staff, 'cleandataset/staff.csv'),
        (transaction, 'cleandataset/transaction.csv')
    ]

    for file, blob_name in files:
        blob_client = container_client.get_blob_client(blob_name)
        output = file.to_csv(index=False)
        blob_client.upload_blob(output, overwrite=True)
        print(f'{blob_name} loaded into Azure Blob Storage')







# A MORE ROBUST CODE
# import pandas as pd
# from dotenv import load_dotenv
# from azure.storage.blob import BlobServiceClient
# import os

# def run_loading():
#     try:
#         load_dotenv()
#         connect_str = os.getenv('AZURE_CONNECT_STR')
#         container_name = os.getenv('CONTAINER_NAME')

#         if not connect_str or not container_name:
#             raise ValueError("Azure Storage connection details missing!")

#         # Ensure all required files exist
#         files_to_check = ['cleaned_zipco_foods_data.csv', 'product.csv', 'staff.csv', 'customer.csv', 'transaction.csv']
#         for file in files_to_check:
#             file_path = os.path.join('Clean_dataset', file)
#             if not os.path.exists(file_path):
#                 raise FileNotFoundError(f"Error: {file_path} not found!")

#         blob_service_client = BlobServiceClient.from_connection_string(connect_str)
#         container_client = blob_service_client.get_container_client(container_name)

#         # Upload files
#         files = [
#             ('cleaned_zipco_foods_data.csv', 'cleandataset/cleaned_zipco_foods_data.csv'),
#             ('product.csv', 'cleandataset/product.csv'),
#             ('customer.csv', 'cleandataset/customer.csv'),
#             ('staff.csv', 'cleandataset/staff.csv'),
#             ('transaction.csv', 'cleandataset/transaction.csv')
#         ]

#         for file_name, blob_name in files:
#             file_path = os.path.join('Clean_dataset', file_name)
#             with open(file_path, "rb") as data:
#                 blob_client = container_client.get_blob_client(blob_name)
#                 blob_client.upload_blob(data, overwrite=True)
#                 print(f'{blob_name} loaded into Azure Blob Storage')

#     except Exception as e:
#         print(f'Error during data loading: {e}')
