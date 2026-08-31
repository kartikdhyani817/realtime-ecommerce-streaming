# Real-Time E-Commerce Streaming & Analytics Platform
r
A real-time data engineering project designed to simulate how e-commerce events can be generated, streamed, processed, stored, and eventually analysed.

The project focuses on building a practical streaming pipeline using Python, Apache Kafka, and MySQL.

## Architecture

```text
E-Commerce Events
       ↓
Python Event Producer
       ↓
Apache Kafka
       ↓
Kafka Consumer
       ↓
Data Processing
       ↓
MySQL
       ↓
Analytics & Dashboard
```

## Project Goals

The main goal is to build a complete real-time data pipeline from event generation to analytics.

The project will gradually introduce:

* Real-time event generation
* Apache Kafka streaming
* Kafka producers and consumers
* Data validation
* Data transformation
* MySQL storage
* Docker
* Automated testing
* Logging and monitoring
* Analytics and dashboards

## Tech Stack

* Python
* Apache Kafka
* MySQL
* Pandas
* SQL
* Docker
* Pytest
* Git & GitHub

## Project Structure

```text
realtime-ecommerce-streaming/
│
├── producer/
├── consumer/
├── processing/
├── database/
├── data/
├── tests/
├── config/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Development Plan

| Day    | Focus                             | Status |
| ------ | --------------------------------- | ------ |
| Day 1  | Project setup & architecture      | ✅      |
| Day 2  | E-commerce event generator        | ⏳      |
| Day 3  | Kafka setup                       | ⏳      |
| Day 4  | Kafka producer                    | ⏳      |
| Day 5  | Kafka consumer                    | ⏳      |
| Day 6  | Event validation                  | ⏳      |
| Day 7  | Data processing                   | ⏳      |
| Day 8  | MySQL integration                 | ⏳      |
| Day 9  | Real-time database pipeline       | ⏳      |
| Day 10 | Dockerization                     | ⏳      |
| Day 11 | Testing & monitoring              | ⏳      |
| Day 12 | Analytics dashboard               | ⏳      |
| Day 13 | Final integration & documentation | ⏳      |

## Current Progress

**Day 1 — Project setup completed ✅**

The basic project structure, technology stack, and development roadmap have been created.

The next step is to build the Python-based e-commerce event generator.
