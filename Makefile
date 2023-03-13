# TODO - templatize this 

images:
	docker build -t benchapp-3.8 --build-arg VERSION=3.8 .
	docker build -t benchapp-3.9 --build-arg VERSION=3.9 .
	docker build -t benchapp-3.10 --build-arg VERSION=3.10 .
	docker build -t benchapp-3.11 --build-arg VERSION=3.11 .

web:
	cd profilersite
	python manage.py qcluster &
	python manage.py runserver
