# Importing necessary dependencies
import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import os


# Data Extraction
def run_extraction():
    try:
        data = pd.read_csv(r'zipco_transaction.csv')
        print('Data Extracted successfully!')

    except Exception as e:
        print(f'An error occurred: {e}')



# A MORE ROBUST CODE
# import pandas as pd
# from dotenv import load_dotenv
# import os

# def run_extraction():
#     try:
#         load_dotenv()
#         data_path = os.path.join(os.getcwd(), 'zipco_transaction.csv')
#         if not os.path.exists(data_path):
#             raise FileNotFoundError(f"File not found: {data_path}")

#         data = pd.read_csv(data_path)
#         print('Data Extracted successfully!')

#     except Exception as e:
#         print(f'An error occurred during extraction: {e}')
