.PHONY: run
run:
	python $(CURDIR)/src/manage.py runserver

.PHONY: prep
prep:
	python $(CURDIR)/src/manage.py makemigrations

.PHONY: mig
mig:
	python $(CURDIR)/src/manage.py migrate

.PHONY: lint
lint:
	black $(CURDIR)

.PHONY: test
test:
	pytest $(CURDIR)/tests
