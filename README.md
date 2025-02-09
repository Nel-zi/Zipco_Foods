# Zipco Foods ETL and Data Analytics Pipeline

## Project Overview
Zipco Foods is a vibrant and growing fast-casual dining business specializing in pizzas and cakes. With numerous outlets across the country, the business generates a significant amount of daily sales data. However, due to inefficient data handling and fragmented data storage (spread across multiple CSV files), valuable insights remain untapped.

This project addresses these challenges by designing and implementing a robust ETL (Extract, Transform, Load) pipeline, developing a scalable and normalized database schema, and enabling real-time data analytics. The solution not only streamlines data processing but also enhances decision-making capabilities, operational efficiency, and data integrity.

## Business Problem Statement
Zipco Foods currently faces several data management issues:
- **Fragmented Data Storage:** Critical sales and inventory data is scattered across multiple CSV files.
- **Inefficient Data Access:** The lack of a unified system causes delays in data retrieval and hinders real-time insights.
- **Data Quality Challenges:** Maintaining data integrity and accuracy is difficult due to disparate data sources.

By automating the ETL process and centralizing data management, the project aims to overcome these challenges and support the company's growth and operational efficiency.

## Objectives & Benefits

### Objectives
- **Automated ETL Pipeline:** Implement a pipeline to extract, clean, transform, and load data consistently.
- **Efficient Database Design:** Create a database schema adhering to 2NF/3NF normalization standards for optimal data retrieval and scalability.
- **Real-time Analytics:** Develop tools for real-time data insights to support informed decision-making.
- **Robust Data Governance:** Ensure data integrity, version control, and compliance via efficient orchestration.

### Benefits
- **Enhanced Decision-Making:** Gain timely, accurate insights from real-time data analytics.
- **Improved Operational Efficiency:** Reduce manual processes and streamline data handling.
- **Scalability & Flexibility:** Prepare for future business growth with a scalable data management solution.
- **Reliable Data Integrity:** Maintain high-quality data for strategic planning and operations.

## Tech Stack
- **Python:** Used for scripting the ETL processes, data cleaning, transformation, and analysis with libraries such as `pandas` and `NumPy`.
- **SQL:** Employed for querying and managing the database, which is hosted on Azure.
- **Azure Blob Storage:** Serves as the centralized, scalable data repository.
- **GitHub:** Utilized for version control, ensuring collaborative development and maintenance.
- **Apache Airflow:** Orchestrates the ETL workflows, schedules jobs, and monitors data pipelines.

## Project Structure
```
zipco-foods-etl/
├── data/                  # Raw and processed data files
├── scripts/               # Python scripts for ETL tasks
│   ├── extract.py         # Data extraction logic
│   ├── transform.py       # Data transformation functions
│   ├── load.py            # Data loading procedures into Azure/SQL
│   └── utils.py           # Helper functions and utilities
├── airflow_dags/          # Apache Airflow DAG definitions
├── docs/                  # Additional documentation and reports
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and setup instructions
```

## Installation & Setup

### Prerequisites
- **Python 3.7+**
- **SQL Database on Azure**
- **Azure Blob Storage Account**
- **Apache Airflow:** Installed and configured.
- **Git:** For cloning the repository.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/zipco-foods-etl.git
   cd zipco-foods-etl
   ```

2. **Set Up the Python Environment:**
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # For Windows: venv\Scripts\activate
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure Environment Variables:**
   Create a `.env` file or set the following environment variables:
   ```
   AZURE_STORAGE_CONNECTION_STRING=your_azure_blob_storage_connection_string
   SQL_DATABASE_URL=your_azure_sql_database_connection_string
   ```

4. **Configure Apache Airflow:**
   - Place the DAG files from the `airflow_dags/` directory into your Airflow DAGs folder.
   - Start the Airflow scheduler and webserver:
     ```bash
     airflow scheduler
     airflow webserver --port 8080
     ```

## Usage

- **Running the ETL Pipeline:**
  The ETL pipeline is orchestrated via Apache Airflow. Once your Airflow environment is running, the scheduled DAG will automatically execute the extraction, transformation, and loading processes.

- **Monitoring the Workflow:**
  Access the Airflow web interface (typically at `http://localhost:8080`) to monitor job progress, review logs, and manage workflow status.

- **Querying Processed Data:**
  Use any SQL client (or Azure Data Studio) to query the processed data stored in your Azure SQL database, enabling real-time analytics and reporting.

## Contributing
Contributions are welcome! If you have suggestions or improvements:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

For significant changes, please open an issue first to discuss what you would like to change.