# Real-Time Kafka Streaming Pipeline

## 📌 Overview
In today's digital-first era, data is the driving force behind innovation. This project showcases an **end-to-end Kafka streaming pipeline** that transforms raw API data into actionable insights in real time. The pipeline is built using **Apache Kafka, Apache Spark, Apache Cassandra, Apache Airflow, and Docker** to ensure **scalability, resilience, and real-time processing**.

## 🚀 Why Build This Pipeline?
A robust data streaming pipeline isn't just a technological achievement—it’s a **game-changer** for businesses looking to stay ahead. Here’s why real-time data streaming is essential:

✅ **Immediate Insights:** Enables quick, data-driven decision-making.
✅ **Scalability:** Manages high data volumes with ease using distributed systems.
✅ **Resilience:** Ensures fault tolerance and handles unexpected data spikes gracefully.
✅ **Innovation:** Opens doors to AI/ML integration and next-gen analytics.

---

## ⚙️ Technologies Used
- **Docker** – Containerized environment for seamless deployment
- **Apache Airflow** – Workflow automation and scheduling
- **Apache Kafka** – High-speed data streaming
- **Apache Spark** – Real-time data transformation
- **Apache Cassandra** – Scalable, fault-tolerant data storage
- **Python** – Custom API data retrieval & processing scripts

---

## 🏗️ Architecture & Workflow

### 1️⃣ **Setting Up with Docker & Apache Airflow**
- The entire environment is **containerized** using Docker.
- **Apache Airflow DAG** automates scheduled API data fetching.
- A **custom Python operator** ensures **data validation and transformation**.

### 2️⃣ **Streaming Data with Apache Kafka**
- Kafka acts as a **real-time message broker** for API data.
- Kafka setup includes **Zookeeper and a schema registry** for scalability.

### 3️⃣ **Processing Data in Real Time with Apache Spark**
- Spark reads data **directly from Kafka** and processes it on the fly.
- Structured streaming enables **efficient transformations**.

### 4️⃣ **Storing Insights in Apache Cassandra**
- Processed data is **stored in Apache Cassandra** for querying and analysis.
- Cassandra’s **distributed nature** ensures high availability.

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
 git clone https://github.com/RupinderpalSingh8/ETE-Real-time-data-streaming.git
 cd kafka-streaming-pipeline
```

### 2️⃣ **Run the Services using Docker Compose**
```bash
 docker-compose up -d
```
This starts all necessary services (**Kafka, Zookeeper, Spark, Cassandra, and Airflow**).

### 3️⃣ **Check Running Containers**
```bash
 docker ps
```

### 4️⃣ **Start the Python Scrip**
- Go to terminal
  ```bash
    python spark-stream.py
  ```

### 5️⃣ **Access Airflow UI (for DAG Scheduling)**
- Open your browser and go to: `http://localhost:8080`
- Default credentials:
  - **Username:** `airflow`
  - **Password:** `airflow`
 
### 6️⃣ **Start the Airflow DAG**
- Enable the DAG to **fetch API data** and push it to Kafka.

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit **issues**, **pull requests**, or **feature requests**.

---

---

## 📬 Contact
For questions or collaboration, reach out at: **rupinderpalsinghraze@gmail.com**
