.PHONY: install seed backend frontend test lint clean

# Install all dependencies including dev tools
install:
	uv sync

# Run code linting and formatting checks with ruff
lint:
	uv run ruff check src/ tests/
	uv run ruff format --check src/ tests/

# Run unit and integration tests with pytest
test:
	uv run pytest

# Seed the SQLite database with mock data
seed:
	uv run python scripts/generate_data.py

# Run the FastAPI backend server
backend:
	uv run fastapi dev src/backend/api.py

# Run the Streamlit dashboard frontend
frontend:
	uv run streamlit run frontend/dashboard.py

# Clean up temporary files, caches, and local sqlite databases
clean:
	rm -rf .venv __pycache__ .pytest_cache src/backend/__pycache__ *.db
