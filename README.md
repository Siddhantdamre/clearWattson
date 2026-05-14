# clearWattson

Smart water-quality monitoring prototype combining sensor collection, cloud messaging, ML-based prediction, and alerting.

## What It Does

- Collects pH and sensor-style readings from embedded/IoT scripts.
- Sends readings through MQTT/cloud backend components.
- Runs model-based water-quality prediction logic.
- Includes SMS alert experiments for unsafe readings or threshold breaches.

## Tech

Python, Flask, MQTT, JavaScript, C/Arduino-style sensor code, ML prediction scripts.

## Repository Map

- `phsensor.c`, `phsensor.ino` - sensor-side experiments.
- `mqttdatatransmission.py`, `cloudbackend.py` - data transport/backend pieces.
- `modelprediction.py` - prediction logic.
- `smsalerts.py` - notification experiments.

## Status

Prototype and research build. The repository is useful as an IoT + ML systems sketch rather than a polished deployment.
