# LangChain AI Agent – Databricks Apps Deployment

A simple AI agent built using **Python, LangChain, OpenAI and Streamlit**, developed locally in VS Code, version-controlled using GitHub, and deployed as a Databricks App.

This project demonstrates how to build an AI agent locally and deploy it to Databricks Apps using a GitHub repository.

## 1. Project Overview

The objective of this project was to understand the end-to-end development and deployment lifecycle of a LangChain-based AI agent.

The application provides a conversational interface where users can interact with an AI agent. The agent uses an OpenAI model and can invoke custom tools to perform tasks.

### Key Features

- Built an AI agent using LangChain.
- Integrated OpenAI GPT-4o-mini using `ChatOpenAI`.
- Implemented a custom multiplication tool using LangChain's `@tool` decorator.
- Used LangChain's `create_agent` API for agent orchestration.
- Developed a chatbot interface using Streamlit.
- Tested the application locally using VS Code.
- Pushed source code to GitHub.
- Deployed the application using Databricks Apps.
- Configured OpenAI API credentials securely using Databricks Secrets.

## 2. Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.12 |
| Agent framework | LangChain |
| Agent creation | `create_agent` |
| LLM | OpenAI GPT-4o-mini |
| LLM integration | `langchain-openai` |
| UI framework | Streamlit |
| IDE | VS Code |
| Version control | Git |
| Source repository | GitHub |
| Deployment platform | Databricks Apps |
| Secret management | Databricks Secrets |

## 3. Architecture

```text
                 DEVELOPMENT
                      |
                      v
                VS Code (Local)
                      |
              Python + LangChain
                      |
                Streamlit UI
                      |
                      v
                  GitHub
               (Source Code)
                      |
                      v
              Databricks Apps
                      |
                Streamlit Runtime
                      |
                      v
                LangChain Agent
                      |
                      v
                 OpenAI API
                 GPT-4o-mini
                      |
                      v
                Agent Response
```

**Deployment workflow:**

1. Develop the application locally in VS Code.
2. Test the application using Streamlit.
3. Push the source code to GitHub.
4. Connect the GitHub repository to Databricks Apps.
5. Configure the required application resources.
6. Deploy the application.
7. Access the deployed application through its Databricks Apps URL.

## 4. Project Structure

```text
langchain-databricks-agent/
│
├── agent.py
│   └── LangChain agent implementation
│
├── app.py
│   └── Streamlit chatbot interface
│
├── requirements.txt
│   └── Python dependencies
│
├── app.yaml
│   └── Databricks Apps configuration
│
├── .env
│   └── Local OpenAI API credentials (not committed)
│
├── .gitignore
│   └── Excludes secrets and virtual environments
│
└── README.md
    └── Project documentation
```

## 5. Agent Implementation

The agent was implemented using LangChain's `create_agent` API.

### Custom Tool

A simple multiplication tool was created to demonstrate tool calling.

```python
from langchain.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b
```

### LLM Configuration

The OpenAI model was integrated using `ChatOpenAI`.

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

### Agent Creation

```python
from langchain.agents import create_agent

agent = create_agent(
    model=llm,
    tools=[multiply],
    system_prompt="You are a helpful AI assistant. Use tools when appropriate."
)
```

The agent can decide when to invoke the multiplication tool based on the user's query.

## 6. Streamlit Application

Streamlit was used to create a simple conversational interface.

The application supports:

- User input through a chat interface.
- Displaying user messages.
- Displaying AI-generated responses.
- Maintaining conversation history using Streamlit session state.

The application was tested locally using:

```bash
python -m streamlit run app.py
```

Local application URL:

```text
http://localhost:8501
```

## 7. Local Development Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

### Step 2: Create a virtual environment

```bash
python -m venv agent_dbc
```

Activate the environment on Windows:

```powershell
.\agent_dbc\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure OpenAI API credentials

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Never commit this file to GitHub.

### Step 5: Run the application

```bash
python -m streamlit run app.py
```

## 8. Databricks Apps Deployment

The application was deployed to Databricks Apps using the GitHub repository as its source.

### Step 1: Create a GitHub repository

Created a GitHub repository to maintain the application source code and version history.

### Step 2: Push local code to GitHub

```bash
git init

git add .

git commit -m "Initial LangChain agent application"

git branch -M main

git remote add origin YOUR_GITHUB_REPOSITORY_URL

git push -u origin main
```

### Step 3: Create a Databricks App

In the Databricks workspace:

1. Navigate to Databricks Apps.
2. Select Create a custom app.
3. Provide the application name.
4. Configure the GitHub repository as the source.
5. Select the `main` branch.
6. Create the application.

### Step 4: Configure app.yaml

Databricks Apps uses `app.yaml` to determine how to launch the application.

```yaml
command:
  - streamlit
  - run
  - app.py
  - --server.port
  - "8000"
  - --server.address
  - "0.0.0.0"

env:
  - name: OPENAI_API_KEY
    valueFrom: openai-api-key
```

### Step 5: Configure secrets

The OpenAI API key was stored in Databricks Secrets instead of being committed to GitHub.

A secret scope was created:

```bash
databricks secrets create-scope openai-agent
```

The API key was stored using:

```bash
databricks secrets put-secret openai-agent OPENAI_API_KEY
```

The secret was then added as a resource to the Databricks App.

| Configuration | Value |
|---|---|
| Secret scope | `openai-agent` |
| Secret key | `OPENAI_API_KEY` |
| Permission | Can read |
| App resource key | `openai-api-key` |

The app resource exposed the secret as the `OPENAI_API_KEY` environment variable.

### Step 6: Deploy the application

After configuring the GitHub source and secret resource:

1. Updated `app.yaml`.
2. Committed and pushed the changes to GitHub.
3. Selected the latest source revision in Databricks Apps.
4. Triggered deployment.
5. Verified the deployed application using its Databricks Apps URL.

## 9. Challenges Faced and Learnings

This project helped me understand several practical aspects of AI application development and deployment.

### 1. Python Virtual Environment Management

Initially, VS Code was using the Anaconda Python interpreter instead of the project's virtual environment.

**Learning:** Always verify the Python interpreter and install dependencies in the correct virtual environment.

Useful commands:

```bash
python -c "import sys; print(sys.executable)"

python -m pip install package_name
```

### 2. LangChain Package Compatibility

Encountered import errors related to `create_agent` and the Databricks LangChain integration.

**Learning:**

- LangChain 1.x provides the `create_agent` API.
- The Databricks integration package uses the `databricks_langchain` import namespace.
- The OpenAI integration uses `langchain_openai`.

### 3. Running Streamlit in the Correct Environment

Initially, Streamlit was launched using the wrong Python installation.

**Learning:** Prefer module-based execution:

```bash
python -m streamlit run app.py
```

This ensures Streamlit runs using the currently selected Python interpreter.

### 4. Databricks Authentication

The Databricks Python SDK initially failed because local Databricks credentials were not configured.

**Learning:** Databricks CLI OAuth authentication can be used to authenticate local development tools and interact with workspace resources.

```bash
databricks auth login --host YOUR_WORKSPACE_URL
```

### 5. External API Integration

The application worked locally but initially failed after deployment because the OpenAI API key was unavailable in the Databricks runtime.

**Learning:**

- Local `.env` files are not automatically available in Databricks Apps.
- Application secrets should be managed through Databricks Secrets and App resources.
- Environment variables can be injected into the application at runtime.

### 6. GitHub-Based Deployment

Learned how to maintain application code in GitHub and deploy the application from a repository to Databricks Apps.

**Learning:** Application changes can be committed and pushed to GitHub, then deployed from the latest source revision.

## 10. Security Considerations

- Never commit API keys to GitHub.
- Keep `.env` excluded through `.gitignore`.
- Use Databricks Secrets for application credentials.
- Grant only the required secret permissions.
- Avoid printing credentials in application logs.
- Review OpenAI API usage and spending limits.

## 11. Cost and Resource Management

This project used Databricks Free Edition and the OpenAI API.

Important considerations:

- Databricks Free Edition has usage quotas.
- Databricks Apps consume workspace usage while running.
- Apps automatically stop after 24 hours in Free Edition.
- OpenAI API usage is separately billed.
- Stop the Databricks App when testing is complete.
- Monitor OpenAI API usage and configure spending controls.

## 12. Future Enhancements

Potential improvements to this project:

- Add multiple custom tools.
- Integrate a RAG pipeline using a vector database.
- Add conversation memory.
- Integrate MCP servers.
- Add structured logging and exception handling.
- Implement agent evaluation and tracing.
- Add CI/CD automation using GitHub Actions.
- Explore Databricks-hosted model endpoints instead of external OpenAI APIs.
- Add authentication and application-level access controls.

## 13. Key Takeaways

Through this project, I gained practical experience in:

1. Building a LangChain agent using Python.
2. Integrating an LLM through the OpenAI API.
3. Implementing custom tools for agent execution.
4. Building a chatbot interface using Streamlit.
5. Managing Python dependencies and virtual environments.
6. Using Git and GitHub for source control.
7. Authenticating with Databricks using the CLI.
8. Managing application secrets using Databricks Secrets.
9. Deploying a Python application using Databricks Apps.
10. Understanding the workflow from local development to cloud deployment.

---

**Project Status:** Successfully deployed and tested.

**Environment:** Databricks Free Edition

**Application:** LangChain AI Agent with OpenAI and Streamlit
