# login-app

This project is a complete end-to-end user authentication system built with FastAPI as the backend and Angular as the frontend. It implements secure login, signup, password hashing, JWT-based authentication, and protected routes. The system follows modern best practices for security, modularity, and clean architecture.

## Features

- ✨ FastAPI backend with automatic API documentation
- 🚀 RESTful API endpoints with Pydantic models
- 📝 Interactive API documentation (Swagger UI)
- 🔍 Health check endpoint for monitoring
- 🎯 Example GET/POST endpoints
- 🔧 Environment configuration support

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ShirudeAkash/login-app.git
cd login-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

## Running the Application

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The application will be available at:
- API: http://localhost:8000
- Interactive API Documentation (Swagger UI): http://localhost:8000/docs
- Alternative API Documentation (ReDoc): http://localhost:8000/redoc

## API Endpoints

### Root Endpoint
- **GET** `/` - Welcome message with API information

### Health Check
- **GET** `/health` - Check if the API is running

### Example Endpoints
- **GET** `/api/v1/hello/{name}` - Personalized greeting
- **POST** `/api/v1/items` - Create an item
- **GET** `/api/v1/search` - Search with query parameters

## Example Usage

### Get API information:
```bash
curl http://localhost:8000/
```

### Check health status:
```bash
curl http://localhost:8000/health
```

### Get a personalized greeting:
```bash
curl http://localhost:8000/api/v1/hello/Alice
```

### Create an item:
```bash
curl -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Item","description":"A test item","price":29.99,"tax":5.0}'
```

### Search with query parameters:
```bash
curl "http://localhost:8000/api/v1/search?q=example&limit=10"
```

## Development

### Running with Auto-reload
For development, use the `--reload` flag:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation
Visit http://localhost:8000/docs to see the interactive API documentation powered by Swagger UI, where you can test all endpoints directly from your browser.

## Project Structure

```
login-app/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env.example         # Example environment configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server
- **Pydantic** - Data validation using Python type annotations
- **Python-dotenv** - Environment variable management

## License

This project is open source and available under the MIT License.
