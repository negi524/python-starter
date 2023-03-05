main: log/ python_starter/config/credential.yml
	poetry run dev

test:
	poetry run pytest tests/

format:
	poetry run black python_starter/ tests/

type-check:
	poetry run mypy python_starter/