# test_cicd_01

A CI/CD test project utilizing Databricks Asset Bundle. This project provides structure and utilities for efficiently managing and deploying Python modules and notebooks in Databricks environments.

> 📖 **한국어 문서**: [README-KR.md](./README-KR.md)

## Project Structure

```
test_cicd_01/
├── src/                          # Source code
│   ├── test_cicd_01/            # Main package
│   │   ├── main.py              # Spark-based main application
│   │   └── __init__.py          # Package initialization (v0.0.1)
│   ├── module/                  # Common modules
│   │   ├── path_manager.py      # Path management utility
│   │   └── util.py              # Basic utility functions
│   ├── foo/                     # Example module
│   │   └── bar.py               # Resource file reading example
│   ├── main.ipynb               # Main notebook (module usage examples)
│   └── set_notebook_paths.ipynb # Notebook path configuration utility
├── resources/                   # Resource files
│   ├── test_cicd_01.job.yml    # Databricks Job definition
│   └── foo/bar.yml             # Example configuration file
├── tests/                       # Test code
│   ├── foo/test_read_resource.py
│   └── module/test_path_manager.py
├── config/                      # Configuration files directory
├── databricks.yml              # Databricks Bundle configuration
└── setup.py                    # Python package setup
```

## Key Features

### 1. Path Management System (PathResolver)
- Path management class implemented with **Singleton pattern**
- Provides absolute paths to various directories within Bundle in Databricks environment
- Supported paths: `resources`, `config`, `tests`

```python
from module.path_manager import PathResolver

paths = PathResolver()
print(paths.resources)  # Resources directory path
print(paths.config)     # Configuration directory path
print(paths.tests)      # Tests directory path
```

### 2. Notebook Path Configuration
- `set_notebook_paths.ipynb`: Automatically configures sys.path for importing Python modules in Databricks notebooks
- Dynamic path configuration based on Bundle name

### 3. Resource File Management
- YAML configuration file reading example
- Safe file access through path manager

```python
from foo.bar import parse_bar
content = parse_bar()  # Read resources/foo/bar.yml file
```

## Getting Started

### 1. Environment Setup

Install Databricks CLI:
```bash
pip install databricks-cli
```

Authenticate to Databricks workspace:
```bash
databricks configure
```

### 2. Development Environment Deployment

Deploy to development environment:
```bash
databricks bundle deploy --target dev
```

Deploy to production environment:
```bash
databricks bundle deploy --target prod
```

### 3. Job Execution

Run deployed Job:
```bash
databricks bundle run
```

### 4. Local Development

Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

Run tests:
```bash
pytest
```

## Testing

The project includes the following tests:

- **Path Manager Tests**: Verify proper operation of PathResolver class
- **Resource File Reading Tests**: Validate YAML file reading functionality

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/module/test_path_manager.py
pytest tests/foo/test_read_resource.py
```

## Development Tools

- **Databricks Connect**: Connect to Databricks cluster from local IDE
- **Visual Studio Code Extension**: Databricks development environment integration
- **pytest**: Unit testing framework

## CI/CD Configuration

This project uses Databricks Asset Bundle to configure CI/CD pipeline:

- **Git Integration**: Source management based on GitHub repository
- **Automated Deployment**: Development/production environment separation through Bundle
- **Job Scheduling**: Automated workflow execution support

For more details, refer to the [Databricks Asset Bundles documentation](https://docs.databricks.com/dev-tools/bundles/index.html).
