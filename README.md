# 🚜 AI-Assisted Yield Trend Analysis & Farm Planning System
### *Revolutionizing Precision Agriculture with Multi-Agent AI & IBM Granite*

![Status](https://img.shields.io/badge/Status-Prototype%20Complete-success)
![Tech Stack](https://img.shields.io/badge/Tech-Langflow%20%7C%20IBM%20Watsonx%20%7C%20AstraDB-blue)
![Hackathon](https://img.shields.io/badge/Hackathon-Problem%20Statement%2015-orange)

---

## 📖 Overview
The **AI-Assisted Yield Trend Analysis System** is an enterprise-grade, multi-agent AI solution designed to solve the complexity of modern farming. Unlike generic chatbots, this system uses a **Deterministic Multi-Agent Orchestrator** to route complex queries to specialized expert agents.

Powered by **IBM Granite-13b** and **Langflow**, it eliminates hallucinations by strictly grounding answers in scientific manuals (via RAG), real-time market data, and strict safety protocols.

---

## 🚧 The Challenge
Farmers today are overwhelmed by disconnected data:
* **Scientific Disconnect:** Soil health manuals are complex and inaccessible.
* **Market Volatility:** Prices fluctuate daily, making selling decisions risky.
* **Operational Uncertainty:** Weather forecasts exist, but actionable advice (e.g., "Don't spray urea today") is missing.
* **Safety Risks:** Generic AI models often recommend banned chemicals.

---

## 💡 The Solution: Multi-Agent Architecture
We moved beyond simple prompting. Our system employs a **"Supervisor-Worker" architecture** where a central Orchestrator delegates tasks to 4 distinct expert agents:

### 1. 🌱 Yield & Farm Data Analysis Agent (The Scientist)
* **Role:** Analyzes soil health, crop inputs, and yield pathology.
* **Tech:** **RAG (Retrieval Augmented Generation)** using **DataStax Astra DB**.
* **Capability:** Cross-references user queries against the *ICAR Agronomy Manual 2025* to prescribe exact fertilizer dosages (N-P-K) and diagnose diseases.
* **Safety:** Includes a **Self-Correction Loop** to auto-detect and block banned chemicals (e.g., Monocrotophos).

### 2. 💰 Trend & Correlation Detection Agent (The Economist)
* **Role:** Analyzes market volatility and profitability.
* **Tech:** **Tavily Search API** for real-time web scraping.
* **Capability:** Scrapes live APMC/Mandi prices, detects trends (Bullish/Bearish), and generates markdown tables for "Buy/Sell/Hold" recommendations.

### 3. 🌦️ Planning & Insight Assistant (The Manager)
* **Role:** Optimizes farm operations based on micro-climate data.
* **Tech:** **Logic Gates** & Weather Forecasting.
* **Capability:** Translates forecasts into logic:
    * *IF Rain > 50% → "ABORT Pesticide Spraying"* (Prevents wash-off).
    * *IF Wind > 10km/h → "STOP Irrigation"* (Prevents drift).

### 4. 🤝 Farm Advisory Agent (The Liaison)
* **Role:** Democratizes access to government schemes.
* **Capability:** Simplifies complex policies (PM-Kisan, Fasal Bima Yojana) into simple eligibility checklists and application roadmaps.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Orchestration** | **Langflow** | Visual node-based chaining & agent routing. |
| **LLM (Brain)** | **IBM Watsonx.ai** | **Granite-13b-chat-v2** for reasoning & summarization. |
| **Vector Database** | **DataStax Astra DB** | Storing embedded agricultural manuals for RAG. |
| **Search Tool** | **Tavily AI** | Real-time, noise-free search for market prices. |
| **Embedding** | **IBM Embeddings** | Converting text to vectors for the database. |

---

## ⚡ Key Features (Hackathon Highlights)
-   **🛡️ Responsible AI Guardrails:** The system actively intercepts responses. If an agent recommends a toxic chemical, the **Safety Supervisor** node rewrites the answer in real-time.
-   **🧠 Chain-of-Thought Reasoning:** Agents don't just answer; they explain *why* (e.g., "I am recommending Zinc because your soil pH is 8.5").
-   **🇮🇳 Hyper-Localized Context:** Tailored specifically for Indian agriculture (Kharif/Rabi seasons, Mandi system, Rupee currency).

---

## 🚀 How to Run
This project is built on **Langflow**. To run it locally or on the cloud:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  **Import to Langflow:**
    - Open Langflow dashboard.
    - Click **"Import"** and select the JSON file from this repo (e.g., `Farm_Agent_Flow.json`).
3.  **Add API Keys:**
    - **IBM Watsonx:** Add your API Key & Project ID in the Global Variables or node settings.
    - **Tavily:** Add your Search API Key.
4.  **Run:**
    - Click the **Lightning Bolt ⚡** icon on the Chat Output node.
    - Open the Playground to start chatting.

---

## 📸 Demo Scenarios
**Scenario 1: Scientific Diagnosis**
> **User:** "My cotton leaves are turning yellow and I have red soil."
> **Agent:** Diagnoses Zinc deficiency (Khaira disease) and prescribes Zinc Sulphate, citing the ICAR Manual.

**Scenario 2: Market Logic**
> **User:** "Should I sell my Onions today in Nashik?"
> **Agent:** Fetches live Lasalgaon rates, notices a price drop, and advises "HOLD" for 3 days.

**Scenario 3: Operational Safety**
> **User:** "Can I spray Urea? Heavy rain is forecast tomorrow."
> **Agent:** **STOP.** Rain will wash away the fertilizer. Leaching hazard detected.

---

## 🔮 Future Roadmap
-   [ ] **Voice Integration:** Allowing farmers to speak in local dialects (Hindi/Marathi/Telugu).
-   [ ] **Computer Vision:** Uploading a photo of a diseased leaf for auto-diagnosis.
-   [ ] **IoT Connection:** Directly triggering irrigation sprinklers based on the Planning Agent's decision.

---

*Built with ❤️ for the IBM Watsonx Hackathon.*
