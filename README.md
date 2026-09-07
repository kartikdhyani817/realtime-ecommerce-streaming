# Real-Time E-Commerce Streaming

A real-time e-commerce data streaming and analytics platform built with **Python, Apache Kafka, and MySQL**.

The project simulates an e-commerce platform where customer order events are continuously generated, streamed through Kafka, validated and transformed, and finally stored in MySQL for analytics.

---

## 🚀 Project Overview

This project is being built step by step as a practical **Data Engineering project**.

Instead of working only with static CSV files, the pipeline handles continuously arriving e-commerce events.

Each event contains information such as:

* Order ID
* Customer ID
* Product
* Category
* Quantity
* Unit Price
* Total Amount
* City
* Event Timestamp

The data flows through Kafka before being processed and stored in a relational database.

---

## 🏗️ Architecture

```text
                    REAL-TIME E-COMMERCE PIPELINE

                    ┌─────────────────────┐
                    │   Event Generator  │
                    │      Python        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Kafka Producer    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Apache Kafka     │
                    │ ecommerce_events    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Kafka Consumer    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Event Processor   │
                    │ Validation & Clean  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       MySQL        │
                    │ realtime_ecommerce │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology      | Purpose                                         |
| --------------- | ----------------------------------------------- |
| Python          | Event generation, processing and pipeline logic |
| Apache Kafka    | Real-time event streaming                       |
| Kafka-Python    | Python integration with Kafka                   |
| MySQL           | Persistent storage                              |
| MySQL Connector | Python-MySQL connection                         |
| Pytest          | Unit testing                                    |
| Git & GitHub    | Version control                                 |

---

## 📁 Project Structure

```text
realtime ecommerce streaming/
│
├── producer/
│   ├── __init__.py
│   ├── event_generator.py
│   └── kafka_producer.py
│
├── consumer/
│   ├── __init__.py
│   └── kafka_consumer.py
│
├── processing/
│   ├── __init__.py
│   └── event_processor.py
│
├── database/
│   ├── __init__.py
│   ├── db_connection.py
│   └── event_repository.py
│
├── data/
│
├── tests/
│   ├── test_event_generator.py
│   ├── test_kafka_producer.py
│   ├── test_kafka_consumer.py
│   ├── test_event_processor.py
│   └── test_database.py
│
├── config/
│
├── README.md
├── requirements.txt
├── pytest.ini
└── .gitignore
```

---

# 📅 Development Progress

## Day 1 — Project Setup

Created the initial project structure and established the architecture for the real-time streaming pipeline.

Set up:

* Producer
* Consumer
* Processing
* Database
* Tests
* Configuration directories

---

## Day 2 — Event Generator

Created a Python event generator that produces realistic e-commerce order events.

Generated fields include:

```text
event_id
order_id
customer_id
product
category
quantity
unit_price
total_amount
city
event_time
```

Added unit tests to verify event structure and total amount calculations.

---

## Day 3 — Apache Kafka Setup

Configured Apache Kafka locally using **KRaft mode**, without requiring ZooKeeper.

Created the Kafka topic:

```text
ecommerce_events
```

Kafka is running locally on:

```text
localhost:9092
```

---

## Day 4 — Kafka Producer

Created the Kafka producer responsible for sending generated e-commerce events to Kafka.

Flow:

```text
Python Event Generator
        ↓
Kafka Producer
        ↓
ecommerce_events
```

Added tests for Kafka configuration.

---

## Day 5 — Kafka Consumer

Created a Kafka consumer that reads events from:

```text
ecommerce_events
```

The consumer deserializes the JSON messages and displays the received order information.

Flow:

```text
Kafka
  ↓
Consumer
  ↓
Received Event
```

---

## Day 6 — Event Processing

Added an event-processing layer between Kafka and MySQL.

The processor:

* Validates required fields
* Validates quantity
* Validates prices
* Normalizes product names
* Normalizes categories
* Normalizes cities
* Converts numeric values
* Validates timestamps
* Adds a processing timestamp

Flow:

```text
Kafka
  ↓
Consumer
  ↓
Validation
  ↓
Transformation
  ↓
Processed Event
```

---

## Day 7 — MySQL Integration

Added the MySQL database layer.

Created:

```text
realtime_ecommerce
```

Database table:

```text
ecommerce_events
```

Processed Kafka events can now be stored permanently in MySQL.

Flow:

```text
Kafka
  ↓
Consumer
  ↓
Event Processor
  ↓
MySQL
```

---

## Day 8 — Database Reliability & Indexing

Improved the database layer to make it more reliable and closer to a production-style pipeline.

Added indexes for commonly queried fields:

```text
order_id
customer_id
event_time
product
category
city
```

Also added **duplicate-event handling** using the unique `event_id`.

If Kafka delivers the same event more than once, the pipeline safely ignores the duplicate instead of crashing.

Example:

```text
Database | Duplicate event ignored: event-123
```

Improved MySQL connection error handling and added database configuration tests.

---

# 🧪 Testing

The project uses **Pytest** for unit testing.

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD="1"
python -m pytest -v
```

The environment variable prevents unrelated globally installed pytest plugins from interfering with the project's tests.

Tests currently cover:

* Event generation
* Event calculations
* Kafka configuration
* Kafka consumer configuration
* Event validation
* Event transformation
* Data type conversion
* Processing timestamps
* Invalid events
* Database configuration

---

# ▶️ Running the Project

The project currently runs locally using three terminals.

### Terminal 1 — Start Kafka

```powershell
cd C:\kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

### Terminal 2 — Start Consumer

```powershell
cd "C:\Users\HP\Desktop\realtime ecommerce streaming"
python -m consumer.kafka_consumer
```

### Terminal 3 — Start Producer

```powershell
cd "C:\Users\HP\Desktop\realtime ecommerce streaming"
python -m producer.kafka_producer
```

Events generated by the producer are streamed through Kafka, processed by the consumer, and stored in MySQL.

---

# 🗄️ Database

Database:

```text
realtime_ecommerce
```

Main table:

```text
ecommerce_events
```

The table stores:

```text
event_id
order_id
customer_id
product
category
quantity
unit_price
total_amount
city
event_time
processed_at
created_at
```

The `event_id` column is unique to prevent duplicate events from being inserted.

---

# 🔄 Current Data Flow

```text
Generate Event
      ↓
Serialize as JSON
      ↓
Kafka Producer
      ↓
Apache Kafka
      ↓
Kafka Consumer
      ↓
Validate Event
      ↓
Transform Event
      ↓
Check Duplicate
      ↓
Store in MySQL
```

---

# 📌 Roadmap

The project will continue to evolve into a more complete real-time data engineering platform.

Planned improvements include:

* [ ] Real-time analytics
* [ ] Aggregated sales metrics
* [ ] Product and category analysis
* [ ] Customer-level analytics
* [ ] Kafka consumer improvements
* [ ] Better logging
* [ ] Error handling and retry mechanisms
* [ ] Monitoring
* [ ] Data quality checks
* [ ] Docker containerization
* [ ] Analytics dashboard
* [ ] Production-style project documentation

---

# 💡 What This Project Demonstrates

This project focuses on practical Data Engineering concepts rather than just building a dashboard.

It demonstrates experience with:

* Real-time data ingestion
* Event-driven architecture
* Apache Kafka
* Kafka producers and consumers
* Data validation
* Data transformation
* Relational databases
* MySQL integration
* Database indexing
* Duplicate-event handling
* Error handling
* Automated testing
* Git and GitHub
* Modular Python project structure

---

# 👨‍💻 Project Status

**Current progress: Day 8**

The core streaming pipeline is now working:

```text
Python
  ↓
Kafka Producer
  ↓
Apache Kafka
  ↓
Kafka Consumer
  ↓
Event Processing
  ↓
MySQL
```

The next stage is to build the **analytics layer** on top of the stored streaming data.

---

## ⭐ Future Goal

The final goal is to turn this into a small but realistic **real-time e-commerce data platform** that demonstrates the complete journey of data:

```text
Generate
   ↓
Stream
   ↓
Consume
   ↓
Validate
   ↓
Transform
   ↓
Store
   ↓
Analyze
   ↓
Visualize
```

This project is designed to showcase practical Data Engineering skills through a complete end-to-end pipeline.
