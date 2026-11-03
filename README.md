
# CyberMirror
### An AI-Powered Digital Twin for Vehicle Cybersecurity

## Project Overview

CyberMirror is an AI-powered vehicle cybersecurity digital twin designed to simulate vehicle network environments, detect abnormal CAN bus traffic, identify potential cyberattacks, and assess security risks.

The system uses machine learning, network monitoring tools, and a graph database to support vehicle cybersecurity analysis.

## System Architecture

Attack Simulation
↓
Network Traffic
↓
Zeek + Suricata
↓
Log Collection
↓
Feature Extraction
↓
ML / Threat Detection
↓
Neo4j Knowledge Graph
↓
Risk Analysis
↓
FastAPI Backend
↓
React Frontend
↓
Security Dashboard

## Technologies Used

### Backend
- Python
- FastAPI
- PostgreSQL
- Neo4j AuraDB

### Frontend
- React
- JavaScript
- Vite
- CSS

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Isolation Forest

### Network Security
- Zeek
- Suricata
- CAN Bus Traffic Analysis

## Implemented Features

- FastAPI backend setup
- PostgreSQL database integration
- Security alerts API (create and retrieve alerts)
- React frontend integration with the alerts API
- CAN traffic preprocessing pipeline
- Feature extraction and scaling
- Isolation Forest anomaly detection
- ML model training and inference
- Neo4j AuraDB connection
- ECU uniqueness constraint
- ECU and Threat node creation
- AFFECTS relationship between Threat and ECU
- Threat retrieval using ECU ID

## Neo4j Graph Structure

The graph database represents relationships between vehicle ECUs and cybersecurity threats.

Example:

Threat: CAN_MESSAGE_SPOOFING

ECU: ECU_01

Relationship: AFFECTS

## Project Structure

```text
CyberMirror/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── utils/
│   └── main.py
│
├── frontend/
│   └── src/
│
├── ml/
│   ├── datasets/
│   ├── evaluation/
│   ├── models/
│   ├── preprocessing/
│   └── README.md
│
└── README.md
```

## Project Status

The project is under development.

Completed:
- Backend and PostgreSQL setup
- Frontend and backend API integration
- Initial ML preprocessing and anomaly detection
- ML inference pipeline
- Neo4j graph database integration

Remaining:
- Risk analysis integration
- Complete ML and backend integration
- Frontend functionality
- End-to-end testing
- Public deployment
- Vehicle attack simulation integration

## Team Members

- Daniya Tazeen
- Aiman
- Ruthvika
