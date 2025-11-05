# Quick Start Guide

Get started with BJJ Notebook in 3 simple steps!

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Set Up OpenAI API Key (Optional)

If you want to use the AI chat feature:

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Get your key from: https://platform.openai.com/api-keys
nano .env  # or use your preferred editor
```

Your `.env` file should contain:
```
OPENAI_API_KEY=sk-your-actual-key-here
OPENAI_MODEL=gpt-4o-mini
```

**Note:** The chat feature requires an OpenAI API key, but you can still use all other features (reference, notes, search) without it!

## 3. Run the Application

```bash
python bjj_notebook.py
```

## What Can You Do?

### Without API Key:
- 📚 Browse comprehensive BJJ reference (positions, techniques, concepts)
- 📝 Take and manage training notes
- 🔍 Search for specific techniques

### With API Key:
- 🤖 All of the above, plus chat with an AI BJJ instructor
- 💾 Save your AI conversations as notes
- 🎓 Get personalized explanations and guidance

## Example Usage

### Browse BJJ Positions
```
Main Menu > 2 (Browse BJJ Reference) > 1 (View Positions)
```

### Search for a Technique
```
Main Menu > 4 (Search Techniques) > Type: "armbar"
```

### Create a Training Note
```
Main Menu > 3 (Manage Notes) > 1 (Create New Note)
Title: My First Training Session
Content: Learned the basics of closed guard today...
Tags: guard, fundamentals
```

### Chat with BJJ Assistant (requires API key)
```
Main Menu > 1 (Chat with BJJ Assistant)
You: How do I escape from side control?
BJJ Assistant: [Provides detailed explanation]
```

## Tips

- Type `back` in any submenu to return to the main menu
- In chat mode, type `save` to save the conversation as a note
- Notes are saved in the `notes/` directory as JSON files
- You can search notes by title, content, or tags

## Need Help?

Check the full [README.md](README.md) for detailed documentation and project structure.

Happy training! 🥋
