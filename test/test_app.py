# test_app.py
import pytest
from httpx import AsyncClient
from main import app  # FastAPIアプリケーションのインポート

@pytest.mark.asyncio
async def test_create_event():
    async with AsyncClient(app=app, base_url="http://localhost:8000") as ac:
        query = """
        mutation {
            createEvent(
                title: "Test Event"
                description: "Test Description"
                date: "2024-12-12"
                location: "Test Location"
            ) {
                id
                title
            }
        }
        """
        response = await ac.post("/graphql", json={'query': query})
        assert response.status_code == 200
        data = response.json()
        assert data['data']['createEvent']['title'] == "Test Event"
