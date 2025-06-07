test:
	poetry run pytest -s -v

test-no-integration:
	poetry run pytest -s -v -m "not integration"

run:
	poetry run python -m plimp

up:
	docker compose up -d

build:
	docker compose up -d --build

down:
	docker compose down -v

