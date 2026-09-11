# Real-Time E-Commerce Streaming Pipeline 🚀
n
A real-time data engineering project that simulates an e-commerce platform where customer order events are generated, streamed through Apache Kafka, processed using Python, and stored in MySQL for further analytics.

This project demonstrates a complete **end-to-end streaming data pipeline** similar to real-world data engineering systems.

---

# 📌 Project Overview

Traditional data pipelines work with batch data collected over time. Modern applications require systems that can process data continuously as it arrives.

This project builds a real-time streaming architecture where:

* E-commerce orders are generated as events
* Events are sent to Apache Kafka
* Kafka Consumer receives incoming events
* Events are validated and transformed
* Clean data is stored in MySQL
* The system handles duplicate events safely

---

# 🏗️ System Architecture

```
                 Real-Time E-Commerce Pipeline


        Event Generator (Python)
                  |
                  ↓
        Kafka Producer
                  |
                  ↓
          Apache Kafka
        ecommerce_events
                  |
                  ↓
        Kafka Consumer
                  |
                  ↓
       Event Processor
   Validation + Transformation
                  |
                  ↓
              MySQL
       realtime_ecommerce DB
```

---

# 🛠️ Tech Stack

| Technology      | Usage                              |
| --------------- | ---------------------------------- |
| Python          | Event generation, processing logic |
| Apache Kafka    | Real-time event streaming          |
| Kafka-Python    | Kafka integration                  |
| MySQL           | Data storage                       |
| MySQL Connector | Database connection                |
| Pytest          | Automated testing                  |
| Git/GitHub      | Version control                    |

---

# 📂 Project Structure

```
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
├── tests/
│   ├── test_event_generator.py
│   ├── test_kafka_producer.py
│   ├── test_kafka_consumer.py
│   ├── test_event_processor.py
│   └── test_database.py
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

# 📅 Development Progress

## ✅ Day 1 — Project Setup

Created the initial project structure.

Added:

* Producer module
* Consumer module
* Processing module
* Database module
* Testing framework

---

# ✅ Day 2 — Event Generator

Created a Python-based e-commerce event generator.

Generated event fields:

```
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

Added validation tests for generated events.

---

# ✅ Day 3 — Kafka Setup

Configured Apache Kafka locally using **KRaft mode**.

Created Kafka topic:

```
ecommerce_events
```

Kafka broker running on:

```
localhost:9092
```

---

# ✅ Day 4 — Kafka Producer

Built Kafka Producer to send generated events into Kafka.

Flow:

```
Python Event
      |
      ↓
Kafka Producer
      |
      ↓
Kafka Topic
```

---

# ✅ Day 5 — Kafka Consumer

Created Kafka Consumer to read events from Kafka.

Consumer features:

* Reads JSON messages
* Deserializes Kafka messages
* Displays incoming orders

Flow:

```
Kafka
  |
  ↓
Consumer
  |
  ↓
Order Event
```

---

# ✅ Day 6 — Event Processing Layer

Added a processing layer between Kafka and Database.

Features:

* Required field validation
* Quantity validation
* Price validation
* Text normalization
* Data type conversion
* Timestamp validation
* Processing timestamp creation

Flow:

```
Raw Kafka Event

      ↓

Validation

      ↓

Transformation

      ↓

Processed Event
```

---

# ✅ Day 7 — MySQL Integration

Connected processed events with MySQL.

Created database:

```
realtime_ecommerce
```

Created table:

```
ecommerce_events
```

Stored fields:

```
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

---

# ✅ Day 8 — Database Reliability Improvements

Improved database performance and reliability.

Added:

## Database Indexing

Indexes created on:

```
order_id
customer_id
event_time
product
category
city
```

This improves query performance.

---

## Duplicate Event Handling

Kafka may deliver the same event more than once.

Implemented duplicate protection using unique:

```
event_id
```

Example:

```
Database | Duplicate event ignored
```

The pipeline continues running without failure.

---

# 🧪 Testing

Testing is done using Pytest.

Run tests:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD="1"
python -m pytest -v
```

Test coverage includes:

* Event generation
* Kafka configuration
* Consumer configuration
* Event validation
* Event transformation
* Database configuration
* Error handling

---

# ▶️ Running the Project

## 1. Start Kafka

```
cd C:\kafka

.\bin\windows\kafka-server-start.bat .\config\server.properties
```

---

## 2. Start Kafka Consumer

```
python -m consumer.kafka_consumer
```

---

## 3. Start Kafka Producer

```
python -m producer.kafka_producer
```

---

## 4. Check MySQL Data

```sql
USE realtime_ecommerce;

SELECT *
FROM ecommerce_events;
```

---

# 🔄 Current Data Flow

```
Generate Event

      ↓

Kafka Producer

      ↓

Apache Kafka

      ↓

Kafka Consumer

      ↓

Validation

      ↓

Transformation

      ↓

Duplicate Check

      ↓

MySQL Storage
```

---

# 🚧 Future Improvements

Planned upgrades:

* Real-time analytics dashboard
* Revenue analytics
* Product performance analysis
* Customer behaviour analysis
* Kafka retry mechanism
* Error queues
* Logging system
* Docker deployment
* Cloud deployment
* Data visualization dashboard
* Monitoring system

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Real-time streaming architecture
* Apache Kafka
* Event-driven systems
* Data validation
* Data transformation
* Database design
* MySQL optimization
* Duplicate handling
* Automated testing
* Python project structure
* Git workflow

---

# 📌 Current Status

```
Completed: Day 8

Pipeline Status:

Python
  ↓
Kafka Producer
  ↓
Apache Kafka
  ↓
Kafka Consumer
  ↓
Event Processor
  ↓
MySQL Database
```

The foundation of the real-time e-commerce streaming platform is complete.

Next phase: building analytics and reporting capabilities on top of streaming data.
