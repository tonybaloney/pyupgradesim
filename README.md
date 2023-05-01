# pyUpgradeSim

A tool for automating load tests against a list of Python versions using locust, Docker and DjangoQ schedulers.

## Requirements

- Docker
- Python 3.8+
- The Python packages in `requirements.txt`, use `pip install -r requirements.txt` to install them

## Usage

Run `make images` to build the container images

Run `make web` to run the web application, launches on port 8000 by default
