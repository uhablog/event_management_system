from fastapi.testclient import TestClient

from app.main import app  # FastAPIアプリケーションのインポート

client = TestClient(app)

def test_create_event():
    event_name = "Event Title4"
    query = """
    mutation {
        createEvent(
            title: Event Title4
            description: "Event Description2"
            date: "2024-07-12"
            location: "hamamatsu cho"
        ) {
            id
        }
    }
    """
    response = client.post("/graphql", json={'query': query})
    print('status code is ...',response.status_code)
    assert response.status_code == 200
    data = response.json()
    print('data is ...',data)
    # assert data['data'] is not None, "GraphQL response data is None"
    # assert 'createEvent' in data['data'], "createEvent not found in response"
    # assert data['data']['createEvent']['title'] == event_name
