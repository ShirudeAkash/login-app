"""
Basic FastAPI Application
A simple FastAPI application with basic endpoints.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

# Create FastAPI application instance
app = FastAPI(
    title="Login App API",
    description="A basic FastAPI application for user authentication",
    version="1.0.0"
)


# Pydantic models for request/response
class HealthResponse(BaseModel):
    status: str
    message: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class MessageResponse(BaseModel):
    message: str
    data: Dict[str, Any] | None = None


# Root endpoint
@app.get("/", response_model=MessageResponse)
async def root():
    """Root endpoint returning a welcome message."""
    return {
        "message": "Welcome to Login App API",
        "data": {
            "version": "1.0.0",
            "status": "running"
        }
    }


# Health check endpoint
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint to verify the API is running."""
    return {
        "status": "healthy",
        "message": "API is running successfully"
    }


# Example GET endpoint
@app.get("/api/v1/hello/{name}", response_model=MessageResponse)
async def hello(name: str):
    """
    Example GET endpoint that greets a user by name.
    
    Args:
        name: The name to greet
    
    Returns:
        A greeting message
    """
    return {
        "message": f"Hello, {name}!",
        "data": {"name": name}
    }


# Example POST endpoint
@app.post("/api/v1/items", response_model=Item)
async def create_item(item: Item):
    """
    Example POST endpoint that creates an item.
    
    Args:
        item: Item data to create
    
    Returns:
        The created item data
    """
    return item


# Example GET endpoint with query parameters
@app.get("/api/v1/search", response_model=MessageResponse)
async def search(q: str = "", limit: int = 10):
    """
    Example GET endpoint with query parameters.
    
    Args:
        q: Search query string
        limit: Maximum number of results to return
    
    Returns:
        Search results
    """
    return {
        "message": "Search completed",
        "data": {
            "query": q,
            "limit": limit,
            "results": []
        }
    }
