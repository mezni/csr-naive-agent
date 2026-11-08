csr-naive-agentcsr-naive-agent is a modular, container-ready Customer Service Representative (CSR) billing and support service built with FastAPI, SQLite, SQLAlchemy, and an interactive Streamlit dashboard. Designed as a foundational component for enterprise telecom BSS/OSS portfolios, it provides robust REST endpoints for account and product management, paired with mock data generators and clean architectural separation.📂 Project ArchitecturePlaintextcsr-naive-agent/
├── .env.example                 # Environment variable templates
├── .gitignore                   # Excludes caches, virtual environments, and SQLite DBs
├── Dockerfile                   # Container build configuration
├── Makefile                     # Shortcut automation for setup, run, and seeding
├── pyproject.toml               # Project metadata and dependencies (managed by uv)
├── README.md                    # Project documentation
├── frontend/
│   └── dashboard.py             # Streamlit operator control panel & frontend UI
├── scripts/
│   └── generate_data.py         # Mock data generator for database seeding
├── src/
│   └── backend/
│       ├── __init__.py
│       ├── api.py               # FastAPI application entrypoint & REST routing
│       ├── database.py          # SQLite engine and session configuration
│       ├── models.py            # SQLAlchemy ORM models
│       └── schemas.py           # Pydantic data validation and serialization models
└── tests/
    ├── __init__.py
    ├── conftest.py              # Pytest configuration and fixtures
    └── test_api.py              # Integration tests for FastAPI endpoints
⚙️ Prerequisites & InstallationThis project utilizes uv for lightning-fast virtual environment and dependency management.Clone and enter the repository:Bashcd csr-naive-agent
Install dependencies:Bashmake install
(Or manually via uv sync)🚀 Quick Start & UsageYou can manage the entire application lifecycle using the provided Makefile commands:Seed the Database:
Populate your SQLite database with mock catalog items:Bashmake seed
Start the FastAPI Backend:
Launch the API development server (available at [http://127.0.0.1:8000](http://127.0.0.1:8000)):Bashmake backend
(Interactive Swagger docs can be accessed at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs))Start the Streamlit Dashboard:
In a separate terminal window, launch the interactive operator interface (available at http://localhost:8501):Bashmake frontend
🛠️ Makefile CommandsCommandDescriptionmake installSyncs and installs project dependencies using uv.make seedRuns the mock data generator script to populate SQLite.make backendStarts the FastAPI server in development mode.make frontendLaunches the Streamlit dashboard interface.make cleanRemoves local build artifacts, caches, virtual environments, and SQLite databases.
