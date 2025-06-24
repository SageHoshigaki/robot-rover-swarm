---
# 🤖 robot-rover-swarm

A modular robotics platform for developing autonomous rover systems using **Python**, **Go**, and optionally **Rust**.  
This project blends real-time hardware control, computer vision, edge ML, and IoT mesh communication — with future biomedical applications.

---

## 🧠 Project Vision

The goal: to create a fully autonomous rover swarm with swarm intelligence, real-time diagnostics, and machine learning at the edge.  

Each unit will eventually integrate:
- Multi-language logic (Python for hardware/ML, Go for concurrency + networking, Rust for speed)
- Photoacoustic imaging for medical diagnostics (Bio X)
- Web-based swarm dashboards and remote control
- Edge inference + decentralized mesh communication

---

## 🧾 Current Phase: Movement Control (Phase 1)

- ✅ `robotRover.py` initialized using `RPi.GPIO`
- 🧪 Testing motor wiring to map GPIO pins to wheels
- 🛠 Next step: refactor into `movement/` with clean driving functions
- 🔁 Go microservice for stateful command relay coming soon

---

## 🧰 Tech Stack

| Layer                   | Technology                                |
|------------------------|-------------------------------------------|
| Low-Level Control       | Python (RPi.GPIO, OpenCV, TensorFlow Lite) |
| Web/Dashboard/API       | Go (Gin, Gorilla WebSockets, GORM)         |
| Sensor Sync + Messaging | Go + MQTT (Paho), WebSockets, BLE Mesh    |
| Optional Performance    | Rust (actix-web, tokio, embedded-hal)     |
| Edge ML                 | TensorFlow Lite, Edge Impulse              |
| DevOps/Infra            | Docker, GitHub Actions (planned)          |

---

### ✅ Phase 1: Basic GPIO Movement
- [x] Motor test with raw GPIO
- [ ] Refactor motor logic into `movement/drive.py`
- [ ] Add CLI and REST command relay via Go

### 🚧 Phase 2: Sensors + Vision
- [ ] Ultrasonic obstacle detection
- [ ] OpenCV camera feed + object tracking
- [ ] Image-based navigation

### 🚀 Phase 3: Edge AI + Swarm Comms
- [ ] Train TensorFlow Lite model for path planning
- [ ] Deploy on Pi with Go relay service
- [ ] Add MQTT + WebSocket mesh communication between units

### 🔬 Phase 4: Biomedical Integration (Bio X)
- [ ] Add photoacoustic sensors
- [ ] Build medical body mapping module
- [ ] Upload diagnostics via secure telemetry

---

## 🧪 Current Status

- 🟡 GPIO pin testing underway
- 🟡 One Python file committed — project structure in progress
- 🟢 Git initialized locally
- 🟣 GitHub repo not yet created (next step)

---

## 📌 Notes

- This repo is **multi-language by design**
- All core movement will be prototyped in Python, then abstracted with Go for higher-order control
- Rust may be used to optimize compute-heavy or latency-sensitive parts of the system later

---

## ✍️ Author

**Sage White**  
R&D | Embedded Systems | EMT | Biomedical Engineering  
[GitHub](https://github.com/SageHoshigaki)

---
