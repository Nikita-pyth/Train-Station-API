# Train Station API

A Django-based REST API for managing train stations, journeys, orders, and users. The application is containerized using Docker for easy deployment and development.

## Project Structure

```
.
├── config/         # Django project configuration
├── journeys/       # Journeys management app
├── orders/         # Orders management app
├── stations/       # Stations management app
├── trains/         # Trains management app
├── users/          # User management app
├── tests/          # Test suite
├── Dockerfile      # Docker configuration
└── requirements.txt # Python dependencies
```

## Technologies Used

- Python 3.11
- Django 5.2.1
- Django REST Framework 3.16.0
- PostgreSQL (via psycopg2)
- Gunicorn
- Docker

## Getting Started

### Prerequisites

- Docker installed on your system
- Docker Compose (optional, for development)

### Building the Docker Image

To build the Docker image, run the following command in the project root directory:

```bash
docker build -t trainstation-api .
```

### Running the Container

To run the container after building the image:

```bash
docker run -d -p 8000:8000 --name trainstation trainstation-api
```

This command will:
- Run the container in detached mode (-d)
- Map port 8000 on your host to port 8000 in the container
- Name the container "trainstation"

### Accessing the Application

Once the container is running, you can access the API at:

```
http://localhost:8000/
```

## API Documentation

The API documentation is available at:
```
http://localhost:8000/api/docs/swagger/
``` 