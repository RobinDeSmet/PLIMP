test:
	poetry run pytest -s -v

test-no-integration:
	poetry run pytest -s -v -m "not integration"

test-data:
	poetry run python scripts/generate_test_data.py

test-assistant:
	poetry run python plimp/assistant/gemini.py

run:
	poetry run python -m plimp

up:
	docker compose up -d

build:
	docker compose up -d --build

down:
	docker compose down -v

backend:
	poetry run uvicorn plimp.api.src.main:app --reload