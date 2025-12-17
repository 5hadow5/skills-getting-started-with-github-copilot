from fastapi.testclient import TestClient
from app import app, activities

client = TestClient(app)

def test_unregister_participant():
    # ensure participant exists
    act = "Chess Club"
    email = "daniel@mergington.edu"
    assert email in activities[act]["participants"]

    # call delete endpoint
    r = client.delete(f"/activities/{act}/participants", params={"email": email})
    assert r.status_code == 200
    assert email not in activities[act]["participants"]
    assert "Unregistered" in r.json()["message"]

    # try deleting again -> 404
    r2 = client.delete(f"/activities/{act}/participants", params={"email": email})
    assert r2.status_code == 404

if __name__ == "__main__":
    test_unregister_participant()
    print("OK")
