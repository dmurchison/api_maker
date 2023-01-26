
start:
	docker-compose up -d

start_build:
	docker-compose up ---build -d

stop:
	docker-compose down

unit_tests:
	docker-compose exec -T app-test pytest tests


