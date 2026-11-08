.PHONY: install seed backend frontend clean

# Install dependencies using uv
install:
	uv sync

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
