from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tables():
    response = client.get("/tables")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_menu():
    response = client.get("/menu-items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_order():
    payload = {"table_id": 1, "items": [{"menu_item_id": 1, "quantity": 2}], "total_price": 5000}  # 50 reais em centavos
    response = client.post("/orders", json=payload)
    assert response.status_code == 200  
    data = response.json()
    assert "id" in data
    assert "total_price" in data


def test_close_table():
    response = client.put("/tables/1/close")  # Usar PUT, pois estamos alterando um dado
    assert response.status_code == 200
    assert response.json()["message"] == "Conta fechada com sucesso."

