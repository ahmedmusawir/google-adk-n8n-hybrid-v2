# ADK Hybrid Multi-Agent Bundle

This repository contains a multi-agent bundle developed with Google's Agent Development Kit (ADK). The system is designed as a scalable backend service deployed on **Google Cloud Run**, providing a suite of specialized AI agents for various tasks.

---

## 🏛️ System Architecture

The project follows a modern, multi-service architecture. A central **ADK Wrapper** acts as a simplified gateway, routing requests from various frontends to the core **ADK Agent Bundle** service. This design separates concerns and allows for independent scaling and development.

---

## 🤖 Agents Included (All Agents using Vertex Gemini 2.5 Flash)

### Because, all other models w/ OpenRouter simply sux!

This bundle features five specialized agents, each powered by Google's Vertex AI and configured for a specific purpose:

- **`jarvis_agent`**: A general-purpose assistant with Google Search capabilities.
- **`calc_agent`**: A tool-using agent for performing mathematical calculations.
- **`ghl_mcp_agent`**: A CRM agent ("Rico") with live access to GoHighLevel data.
- **`greeting_agent`**: A conversational agent for handling initial interactions.
- **`product_agent`**: A specialist agent with knowledge fetched from Google Cloud Storage.

---

## 📚 Documentation

For detailed information on the project's architecture, deployment process, and API usage, please refer to the documents in the `/docs` directory.

- **[📄 Project Overview](./docs/overview.md)**: Learn about the project's purpose and the capabilities of each agent.
- **[🚀 Deployment Guide](./docs/deployment.md)**: A complete, step-by-step guide to deploying the ADK Agent Bundle to Google Cloud Run.
- **[🔌 API Information](./docs/api-info.md)**: Instructions on how to interact with the deployed system via the ADK Wrapper.

---

## ✨ Key Technologies

- **Backend Framework:** Google Agent Development Kit (ADK)
- **Cloud Platform:** Google Cloud Run, Google Secret Manager, Google Cloud Storage
- **AI Models:** Google Vertex AI (Gemini)
- **Database:** Supabase (Postgres) for session history
- **Gateway/Wrapper:** FastAPI
- **Containerization:** Docker
