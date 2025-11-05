# BJJ Notebook 🥋

A Brazilian Jiu-Jitsu workbook and reference application with OpenAI-powered chat assistant for learning techniques, taking notes, and getting personalized BJJ guidance.

## Features

- **🤖 AI-Powered BJJ Assistant**: Chat with an OpenAI-powered assistant that knows BJJ positions, techniques, and concepts
- **📚 Comprehensive BJJ Reference**: Browse positions, techniques, sweeps, passes, escapes, and submissions
- **📝 Note Taking System**: Save training notes, conversations, and personal insights
- **🔍 Technique Search**: Quickly find specific techniques across all categories
- **💾 Persistent Storage**: All notes are saved locally as JSON files

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ajharris/BJJ-notebook.git
   cd BJJ-notebook
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up OpenAI API key**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```
   - Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)

## Usage

Run the application:
```bash
python bjj_notebook.py
```

### Main Features

#### 1. Chat with BJJ Assistant
- Ask questions about BJJ techniques and positions
- Get personalized guidance and explanations
- Save conversations as notes
- Clear conversation history to start fresh

Example questions:
- "Explain the closed guard position"
- "How do I escape from mount?"
- "What are the key concepts for passing guard?"

#### 2. Browse BJJ Reference
- **Positions**: Guard, Mount, Side Control, Back Control, Turtle
- **Key Concepts**: Position before submission, Base and posture, Frames and angles, etc.
- **Techniques**: 
  - Submissions (Chokes, Armlocks, Leglocks)
  - Sweeps
  - Guard Passes
  - Escapes

#### 3. Manage Notes
- Create training notes with titles, content, and tags
- List all saved notes
- View specific notes by ID
- Search notes by keywords
- Delete old notes

#### 4. Search Techniques
- Quick search across all technique categories
- Find techniques by name
- View technique details including position and type

## Project Structure

```
BJJ-notebook/
├── bjj_notebook.py          # Main CLI application
├── src/
│   ├── __init__.py          # Package initialization
│   ├── chat_handler.py      # OpenAI chat integration
│   ├── notes_manager.py     # Note-taking system
│   └── bjj_reference.py     # BJJ reference data
├── notes/                   # Saved notes (created on first use)
├── .env.example             # Example environment variables
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Requirements

- Python 3.7+
- OpenAI API key (for chat features)
- Dependencies listed in `requirements.txt`

## Configuration

The application uses environment variables for configuration:

- `OPENAI_API_KEY`: Your OpenAI API key (required for chat)
- `OPENAI_MODEL`: OpenAI model to use (default: `gpt-4o-mini`)

## Notes Storage

Notes are stored as JSON files in the `notes/` directory. Each note contains:
- Unique ID with timestamp
- Title and content
- Tags for organization
- Creation and update timestamps

## Safety Note

BJJ is a physical martial art that should be practiced under the supervision of qualified instructors. This application is for educational reference only and does not replace proper training.

## Contributing

Contributions are welcome! Feel free to:
- Add more BJJ techniques and positions
- Improve the chat assistant's knowledge
- Add new features
- Fix bugs

## License

This project is open source and available for educational purposes.

## Future Enhancements

Potential features to add:
- Web interface (Flask/Django)
- Training log with calendar
- Progress tracking
- Video reference links
- Mobile app
- Drill timer
- Competition preparation tools