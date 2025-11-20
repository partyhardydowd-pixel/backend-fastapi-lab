from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_commercial_flow_mutes_and_unmutes_device():
    # 1) Create device
    resp = client.post(
        "/api/v1/devices",
        json={"name": "Test TV", "type": "tv"},
    )
    assert resp.status_code == 201
    device = resp.json()
    device_id = device["id"]
    assert device["is_muted"] is False

    # 2) Create rule
    resp = client.post(
        "/api/v1/rules",
        json={
            "name": "Mute all commercials",
            "trigger": "commercial_start",
            "enabled": True,
        },
    )
    assert resp.status_code == 201

    # 3) Send commercial-start
    resp = client.post(
        "/api/v1/events/commercial-start",
        json={"device_id": device_id},
    )
    assert resp.status_code == 201

    # 4) Device should now be muted
    resp = client.get("/api/v1/devices")
    assert resp.status_code == 200
    devices = resp.json()
    current = next(d for d in devices if d["id"] == device_id)
    assert current["is_muted"] is True

    # 5) Send commercial-end
    resp = client.post(
        "/api/v1/events/commercial-end",
        json={"device_id": device_id},
    )
    assert resp.status_code == 201

    # 6) Device should now be unmuted
    resp = client.get("/api/v1/devices")
    assert resp.status_code == 200
    devices = resp.json()
    current = next(d for d in devices if d["id"] == device_id)
    assert current["is_muted"] is False
