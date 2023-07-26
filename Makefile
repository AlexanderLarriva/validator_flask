start:
	poetry run flask --app validator_flask.app --debug run --port 8000

setup-key:
	export SECRET_KEY=your-secret-key