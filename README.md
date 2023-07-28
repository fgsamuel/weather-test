# Backend Test Application

## Description
It's built using Django, a high-level Python Web framework that is widely used within the company. The Django REST Framework is used to provide a REST service. Docker and Docker Compose are used to make the setup and running of the application on a local machine much easier. Additionally, a Swagger documentation is generated to facilitate the testing of the API without the need for external tools.

## Requirements
- Python 3.10.11
- Docker
- Docker Compose

## Setup & Installation
1. Clone this repository to your local machine with `git clone https://github.com/fgsamuel/weather-test.git`.
2. Navigate to the project directory with `cd weather-test`.
2. copy the file `.env.sample` to `.env` and fill in the values. `cp .env.sample .env`
3. Run `docker-compose up -d` to start the application.
4. Run `docker-compose exec app python manage.py migrate` to apply the migrations.

Now, the application should be running on http://localhost:8000. You can access the Swagger UI for the API documentation and testing at http://localhost:8000/swagger.

## Testing through Swagger
1. Navigate to http://localhost:8000/swagger.
2. Click on the `POST /temperature` endpoint.
3. Click on the `Try it out` button.
4. Fill in the required parameters.
```json
{
  "services": [
    "accuweather",
    "noaa",
    "weatherdotcom"
  ],
  "latitude": 33,
  "longitude": 44,
  "temperature_unit": "c"
}
```
5. Click on the `Execute` button.

The endpoint will get the temperature from each of the services and return the average temperature.

## Architectural Highlights
This application uses a unique design strategy to efficiently consolidate multiple external API responses and provide the user with an average result. 

At the core of this design are two major components: `ClientBase` and `ServiceBase`.

### ClientBase
`ClientBase` is an encapsulation of the `Requests` library. It provides a simple and unified way to manage outgoing API requests.

### ServiceBase
`ServiceBase` serves as a superclass to be inherited by all the services used in the application. It encapsulates common service functionalities, allowing each individual service to focus on what makes it unique.

For each external API service, a new class is derived from `ServiceBase`. This class overrides the necessary method(s) to adapt to the specific requirements of that service. This approach offers several benefits:
- **Maintainability**: The code remains clean and easy to understand. Each service is isolated, preventing changes to one from unintentionally affecting others.
- **Extensibility**: Adding new services becomes straightforward. Simply inherit from `ServiceBase` and implement the unique aspects of the new service.
- **Adaptability**: As the individual external services evolve and change over time, updating the corresponding class in our application is simple and localized.

This architectural approach provides a robust and flexible foundation for the application, ensuring it can easily adapt and grow as needed.

## Future Enhancements
While the current implementation of the application serves its purpose as a test, there are areas where it could be optimized further for a production environment. 

One of the key improvements would be in the handling of external API calls. The application currently makes these calls in sequence, which can lead to extended response times. This approach was taken due to the constraints of the test scenario.

In a production scenario, asynchronous processing would be implemented to execute these calls simultaneously. This would greatly enhance the application's performance by reducing the overall response time.

Furthermore, task queue systems such as Celery could be used to perform these tasks in the background, further improving the efficiency and user experience of the application.
