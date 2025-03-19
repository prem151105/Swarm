# AI-Agent-Swarm

## Description
This project implements a swarm of AI agents that collaborate to perform tasks. Each agent has a specialized role (e.g., Researcher, Planner, Executor, Critic, Coordinator) and communicates via a message bus. The system integrates with a large language model (LLM) for task execution and uses a shared memory pool for data exchange.

## Setup
1. Clone the repository: git clone https://github.com/yourusername/AI-Agent-Swarm.git
2. Install dependencies: 2. Install dependencies:
3. Set up your OpenAI API key in `config.yaml`:
```yaml
llm_provider:
  api_key: "your_api_key_here"
  model: "gpt-3.5-turbo"
Usage
Run the main script to start the swarm:
 python main.py
 
- **Note**: Replace `yourusername` with your actual GitHub username or adjust the repository URL as needed.
- **Purpose**: Guides users on how to set up and run the project.

---

### File: `requirements.txt`
This file lists the Python packages required for the project.

