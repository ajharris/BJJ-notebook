import os
import requests

# ----------------------------
# CONFIGURATION
# ----------------------------
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN environment variable not set")

REPO_OWNER = "ajharris"
REPO_NAME = "BJJ-notebook"

features = [
    "Set up React app with Vite",
    "Configure Tailwind CSS styling",
    "Create basic app layout (chat panel + notebook panel)",
    "Implement chat UI with message history",
    "Integrate OpenAI API for conversational note taking",
    "Design structured note schema (topics, techniques, insights, gear)",
    "Parse AI responses into structured notes",
    "Persist notes using localStorage",
    "Display notes grouped by date",
    "Add Gi / No Gi filtering",
    "Enable editing existing notes",
    "Enable deleting notes",
    "Implement search across notes by topic or technique",
    "Add export notes to Markdown",
    "Add export notes to PDF",
    "Add error handling for OpenAI API failures",
    "Add basic README with setup and usage instructions",
]

labels = ["enhancement"]
assignees = ["ajharris"]

# ----------------------------
# SCRIPT
# ----------------------------
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

for feature in features:
    issue = {
        "title": feature,
        "body": (
            "### Feature Description\n"
            f"{feature}\n\n"
            "### Acceptance Criteria\n"
            "- [ ] Feature implemented\n"
            "- [ ] Works as expected in the UI\n"
            "- [ ] Code reviewed / refactored if needed\n"
            "- [ ] Documented where appropriate\n"
        ),
        "labels": labels,
        "assignees": assignees,
    }

    response = requests.post(url, headers=headers, json=issue)

    if response.status_code == 201:
        print(f"Created issue: {feature}")
    else:
        print(f"Failed to create issue: {feature}")
        print(response.status_code, response.json())
