# Retail Data Pipeline

## About This Project
The **Retail Data Pipeline** project is a Python-based solution for processing and managing retail data. This pipeline is designed to read and process a list of tables that need to be loaded into a database from a CSV file (`table_list.txt`). Key highlights of the project include:

- **Dynamic Environment Configuration**: The project allows specifying the environment (e.g., `dev`, `prod`) through command-line arguments. It dynamically retrieves database connection details for the specified environment from a configuration file.
- **File Processing**: Reads and processes the `table_list.txt` file using Python's Pandas library to identify tables marked for loading.
- **Modular Structure**: Includes separate modules for utility functions, configuration management, and main execution, ensuring maintainability and scalability.
- **Error Handling**: Incorporates argument validation and graceful error handling for missing or invalid inputs.
- **Version Control**: The project is fully version-controlled, with staged commits and clear commit messages for traceability.

## Key Files
- **`app.py`**: Main script for executing the data pipeline.
- **`util.py`**: Contains utility functions for processing files and tables.
- **`table_list.txt`**: Input file listing tables to be loaded.
- **`launch.json`**: VS Code configuration file for debugging and setting up environment variables.

## Technologies Used
- **Python**: Core programming language (Pandas for file processing).
- **VS Code**: Development environment with `launch.json` for debugging.
- **Git**: Version control for managing project changes.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/veerabhmahadik/retail_data_pipeline.git
