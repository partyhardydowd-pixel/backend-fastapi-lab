📺 AdMute Hub

Event-Driven Commercial Muting Backend — FastAPI + Pydantic + pytest

AdMute Hub is a clean, lightweight backend service that automatically mutes and unmutes a TV or media device based on incoming events such as commercial_start and commercial_end.

It’s a fully working, event-driven rules engine built with:

FastAPI (async web framework)

Pydantic (data models & validation)

pytest (automated test suite)

Simple in-memory services (device registry, rule engine, events log)

This project was built fully by hand — no scaffolding, no shortcuts — to demonstrate real backend engineering ability and production-grade structure.

🚀 Features
✔ Device Registry

Add TVs, receivers, or any device that can be muted/unmuted.

✔ Rules Engine

Create rules like:

"Mute all commercials"
trigger = "commercial_start"
enabled = true


When a matching event arrives, the engine applies the rule.

✔ Commercial Detection Events

Two core endpoints:

POST /events/commercial-start

POST /events/commercial-end

Each triggers automatic mute/unmute behavior.

✔ Full API + Auto Docs

Swagger UI available at:

http://127.0.0.1:8010/docs

✔ Fully Tested

One end-to-end test proves the entire commercial muting workflow:

Create device

Create rule

Trigger commercial_start → device mutes

Trigger commercial_end → device unmutes

📁 Project Structure
backend-fastapi-lab/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── users.py
│   │       ├── devices.py
│   │       ├── rules.py
│   │       └── events.py
│   │
│   ├── schemas/
│   │       device.py
│   │       rule.py
│   │       event.py
│   │       user.py
│   │
│   ├── services/
│   │       device_service.py
│   │       rule_service.py
│   │       event_service.py
│   │
│   └── main.py
│
├── tests/
│   └── test_admute_flow.py
│
├── .gitignore
└── README.md

🧩 API Overview
Health Check

GET /health

Devices
POST /api/v1/devices
GET /api/v1/devices
POST /api/v1/devices/{id}/mute
POST /api/v1/devices/{id}/unmute

Rules
POST /api/v1/rules
GET /api/v1/rules

Events
POST /api/v1/events/commercial-start
POST /api/v1/events/commercial-end

🧪 Running the Tests

Inside the venv:

pytest


Example output:

1 passed in 0.46s

▶ Running the Server
Set-Location 'D:\Embraced\backend-fastapi-lab'
& .\.venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --host 127.0.0.1 --port 8010 --reload


Open Swagger:

http://127.0.0.1:8010/docs

🎯 Why This Exists

People hate commercials.
And you know what? It’s fun to build things that make life better — even in small ways.

This backend forms the foundation of a potential cross-platform app:

Smart TV agent

Chromecast / FireStick integration

Simple commercial detector

Speaker/receiver mute control

…and it doubles as a strong backend engineering portfolio piece, showing:

Clean service layout

Real event-driven logic

FastAPI architecture

Pydantic model design

Automated test coverage

📌 Next Up (Roadmap)

Add persistent storage (SQLite → PostgreSQL)

Add user authentication (JWT or API keys)

Add real TV/receiver integrations (CEC / LAN control)

Add an ML-based commercial detector module

Deploy a cloud version (AWS API Gateway + Lambda or ECS)

Web UI dashboard

🧑‍💻 Author

Michael (“partyhardydowd-pixel”)
Backend Engineer · FastAPI · Python · AWS · Systems & Automation
Building the Embraced OS ecosystem & practical AI tools.
