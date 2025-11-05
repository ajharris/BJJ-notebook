#!/usr/bin/env python3
"""BJJ Notebook - Web Application."""

import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from src.chat_handler import BJJChatHandler
from src.notes_manager import NotesManager
from src.bjj_reference import (
    get_all_positions,
    get_all_concepts,
    search_techniques,
    BJJ_TECHNIQUES
)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize managers
notes_manager = NotesManager()

def get_chat_handler():
    """Get or create chat handler for the session."""
    if 'chat_initialized' not in session:
        try:
            session['chat_handler'] = True
            session['chat_initialized'] = True
            return BJJChatHandler()
        except Exception as e:
            session['chat_error'] = str(e)
            return None
    return BJJChatHandler()

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html')

@app.route('/chat')
def chat():
    """Chat interface page."""
    chat_available = True
    error_message = None
    
    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        chat_available = False
        error_message = "OpenAI API key not configured. Please set OPENAI_API_KEY in your .env file."
    
    return render_template('chat.html', chat_available=chat_available, error_message=error_message)

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """Handle chat API requests."""
    data = request.get_json()
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400
    
    try:
        chat_handler = BJJChatHandler()
        response = chat_handler.chat(user_message)
        
        # Store conversation in session for potential saving
        if 'conversation' not in session:
            session['conversation'] = []
        session['conversation'].append({
            'user': user_message,
            'assistant': response
        })
        session.modified = True
        
        return jsonify({
            'response': response,
            'success': True
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/chat/clear', methods=['POST'])
def clear_chat():
    """Clear chat history."""
    session.pop('conversation', None)
    session.modified = True
    return jsonify({'success': True})

@app.route('/api/chat/save', methods=['POST'])
def save_conversation():
    """Save current conversation as a note."""
    conversation = session.get('conversation', [])
    
    if not conversation:
        return jsonify({'error': 'No conversation to save'}), 400
    
    # Format conversation text
    conversation_text = []
    for msg in conversation:
        conversation_text.append(f"You: {msg['user']}\n")
        conversation_text.append(f"BJJ Assistant: {msg['assistant']}\n")
    
    formatted_text = "\n".join(conversation_text)
    
    try:
        note_id = notes_manager.save_conversation(formatted_text)
        return jsonify({
            'success': True,
            'note_id': note_id
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/reference')
def reference():
    """BJJ reference browser page."""
    positions = get_all_positions()
    concepts = get_all_concepts()
    techniques = BJJ_TECHNIQUES
    
    return render_template('reference.html', 
                         positions=positions, 
                         concepts=concepts,
                         techniques=techniques)

@app.route('/notes')
def notes():
    """Notes management page."""
    all_notes = notes_manager.list_notes()
    return render_template('notes.html', notes=all_notes)

@app.route('/notes/view/<note_id>')
def view_note(note_id):
    """View a specific note."""
    note = notes_manager.get_note(note_id)
    if not note:
        return "Note not found", 404
    return render_template('view_note.html', note=note)

@app.route('/api/notes', methods=['POST'])
def create_note():
    """Create a new note via API."""
    data = request.get_json()
    title = data.get('title', '').strip()
    content = data.get('content', '').strip()
    tags_str = data.get('tags', '').strip()
    
    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400
    
    tags = [tag.strip() for tag in tags_str.split(',')] if tags_str else []
    
    try:
        note_id = notes_manager.save_note(title, content, tags)
        return jsonify({
            'success': True,
            'note_id': note_id
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note via API."""
    try:
        notes_manager.delete_note(note_id)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/search')
def search():
    """Search techniques page."""
    query = request.args.get('q', '').strip()
    results = []
    
    if query:
        results = search_techniques(query)
    
    return render_template('search.html', query=query, results=results)

@app.route('/api/notes/search')
def search_notes_api():
    """Search notes via API."""
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify({'results': []})
    
    try:
        results = notes_manager.search_notes(query)
        return jsonify({
            'success': True,
            'results': results
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

def main():
    """Run the Flask application."""
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("\n⚠️  Warning: No .env file found.")
        print("To use the OpenAI chat feature, create a .env file with your API key.")
        print("See .env.example for reference.\n")
    
    print("\n🥋 Starting BJJ Notebook Web Application...")
    print("🌐 Open your browser and navigate to: http://localhost:5000\n")
    
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
