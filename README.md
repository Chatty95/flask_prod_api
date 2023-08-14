# Flask API for Random Array Generation

This Flask API project provides an endpoint for generating random arrays of floats based on input sentences. The generated arrays are 500-dimensional and the randomness is seeded using a hash of the input sentence.

## How It Works

The project exposes a single API endpoint that accepts POST requests to `/generate_random_array`. The endpoint expects a JSON payload with a "sentence" field. The sentence is used to seed the random number generator (RNG) to ensure reproducibility while generating random arrays.

### Endpoint Details

- **Endpoint**: `/generate_random_array`
- **HTTP Method**: POST

### Input Validation

Upon receiving a POST request, the endpoint validates the input JSON data. If the "sentence" field is missing or not provided, the API returns a 400 Bad Request response with an error message indicating the missing input.

### Generating Random Arrays

If the input is valid, the endpoint uses the input sentence to generate a hash using SHA-256. This hash is then used as a seed to initialize the NumPy random number generator (`np.random.default_rng`). By using the same seed, the RNG generates consistent random numbers based on the input sentence.

A 500-dimensional array of random floats is generated using the RNG's `random` method. The resulting array is converted to a list format for JSON serialization.

### Response Format

The API responds with a JSON object containing the original input sentence and the generated random array. The response format looks like:

```json
{
  "sentence": "Input sentence here.",
  "random_array": [0.123, 0.456, "...", 0.789]
}
```

## Project Structure

The project is organized as follows:

- ├── prod_ready_api/        # Main project package
- │   ├── __init__.py
- │   ├── api/                # API package
- │   │   ├── __init__.py
- │   │   └── routes.py       # API routes
- │   ├── config.py           # Configuration settings
- │   └── gunicorn_config.py  # Gunicorn server configuration
- ├── tests/                 # Test suite
- │   ├── __init__.py
- │   ├── conftest.py        # Test configuration
- │   ├── resources/         # Test resources
- │   │   ├── __init__.py
- │   │   └── mocked_output.py # Mocked data for tests
- │   └── test_routes.py     # Test cases for routes
- ├── Makefile               # Makefile for project tasks
- ├── README.md              # Project documentation
- ├── manage.py              # Script for running the application
- ├── poetry.lock            # Dependency lock file
- └── pyproject.toml         # Project configuration for Poetry




## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python 3.9](https://www.python.org/downloads/release/python-390/) installed
- [Poetry](https://python-poetry.org/docs/#installation) installed for dependency management

Verify Python Version: Check if Python 3.9 is being used:

   ```sh
python --version
   ```
You should see the output indicating Python 3.9.x.

## Setup and Usage

1. **Clone this repository:**

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
Install Python 3.9 if not already installed:
Download it from python.org.

Install Poetry:
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

Configure Poetry: Make sure to configure Poetry to use Python 3.9 for your project:
   ```sh
poetry env use 3.9
   ``````

Start virtual environment
   ```sh
poetry shell   
   ```
   
Install project dependencies:
   ```sh
make install
   ```

Run tests:
   ```sh
make test
   ````

Run the server:
   ```sh
make run
   ```
Access the API:

Send POST requests to http://localhost:8000/generate-array with a JSON payload containing a "sentence" field.
   ```she
  curl -X POST -H "Content-Type: application/json" -d '{"sentence": "Hello World"}' http://localhost:8100/api/generate_random_array
   ```