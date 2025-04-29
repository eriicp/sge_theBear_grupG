# ERP FASTAPI Project

This project is a FastAPI application designed to manage various modules related to an ERP system. Each module handles specific functionalities, providing a structured approach to managing data and operations.

## Project Structure

```
ERP_FASTAPI
├── app
│   ├── main.py                # Entry point of the application
│   ├── modules
│   │   ├── empleats           # Module for employee management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── events             # Module for event management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── vendes             # Module for sales management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── calendari          # Module for calendar management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── compres            # Module for purchase management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── costos             # Module for cost management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── punts_de_venda     # Module for points of sale management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   │   ├── planificacio       # Module for planning management
│   │   │   ├── __init__.py
│   │   │   ├── router.py
│   │   │   └── models.py
│   └── __init__.py
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To start the FastAPI application, run:

```
uvicorn app.main:app --reload
```

You can then access the API documentation at `http://127.0.0.1:8000/docs`.

## Modules Overview

- **Empleats**: Manages employee data and operations.
- **Events**: Handles event-related functionalities.
- **Vendes**: Manages sales transactions and data.
- **Calendari**: Provides calendar functionalities.
- **Compres**: Manages purchase operations.
- **Costos**: Handles cost-related data.
- **Punts de Venda**: Manages points of sale.
- **Planificacio**: Provides planning functionalities.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.