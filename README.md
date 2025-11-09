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

### Web Application (Recommended)

Run the web application:
```bash
python web_app.py
```

Then open your browser and navigate to: http://localhost:5000

The web interface provides:
- Modern, user-friendly interface
- AI-powered chat with BJJ assistant
- Comprehensive BJJ reference browser
- Notes management with categories and related notes linking
- Quick technique search
- All features from the CLI in an easy-to-use web interface

### Command Line Interface

Run the CLI application:
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
- Create training notes with titles, content, tags, and categories
- Organize notes by category (technique, training, competition, concept, etc.)
- List all saved notes
- View specific notes by ID
- Discover related notes based on category and tags
- Search notes by keywords
- Delete old notes

#### 4. Search Techniques
- Quick search across all technique categories
- Find techniques by name
- View technique details including position and type

## Project Structure

```
BJJ-notebook/
├── web_app.py               # Flask web application
├── bjj_notebook.py          # CLI application
├── src/
│   ├── __init__.py          # Package initialization
│   ├── chat_handler.py      # OpenAI chat integration
│   ├── notes_manager.py     # Note-taking system with categories
│   └── bjj_reference.py     # BJJ reference data
├── templates/               # HTML templates for web interface
│   ├── base.html           # Base template with navigation
│   ├── index.html          # Home page
│   ├── chat.html           # Chat interface
│   ├── reference.html      # BJJ reference browser
│   ├── notes.html          # Notes management
│   ├── view_note.html      # Individual note view with related notes
│   └── search.html         # Technique search
├── static/
│   └── css/
│       └── style.css       # Styling for web interface
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
- Category (technique, training, competition, concept, general, chat)
- Tags for organization
- Creation and update timestamps
- Automatic linking to related notes based on category and tags

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

## Features Highlights

### Web Interface
The web application provides a modern, responsive interface with:
- **Category Organization**: Organize notes by technique, training, competition, concept, or custom categories
- **Related Notes Linking**: Automatically discover related notes based on shared categories and tags
- **Responsive Design**: Works on desktop and mobile browsers
- **Clean UI**: Modern, card-based layout with intuitive navigation

### Note Categories
Notes can be organized into categories:
- **Technique**: For specific BJJ techniques and moves
- **Training**: For training session notes and observations
- **Competition**: For competition strategies and experiences
- **Concept**: For conceptual understanding and principles
- **General**: For general notes
- **Chat**: Automatically assigned to saved conversations

Related notes are automatically linked when they share:
- The same category
- Common tags

## Future Enhancements

Potential features to add:
- Training log with calendar
- Progress tracking
- Video reference links
- Mobile app
- Drill timer
- Competition preparation tools