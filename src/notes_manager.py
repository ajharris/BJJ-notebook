"""Notes management for BJJ training sessions and techniques."""

import os
import json
from datetime import datetime

class NotesManager:
    """Manages user notes for BJJ training."""
    
    def __init__(self, notes_dir="notes"):
        """Initialize notes manager with storage directory."""
        self.notes_dir = notes_dir
        self._ensure_notes_directory()
    
    def _ensure_notes_directory(self):
        """Create notes directory if it doesn't exist."""
        if not os.path.exists(self.notes_dir):
            os.makedirs(self.notes_dir)
    
    def save_note(self, title, content, tags=None):
        """Save a new note with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        note_id = f"{timestamp}_{title.replace(' ', '_').lower()}"
        
        note = {
            "id": note_id,
            "title": title,
            "content": content,
            "tags": tags or [],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        try:
            with open(filename, 'w') as f:
                json.dump(note, f, indent=2)
            return note_id
        except Exception as e:
            raise Exception(f"Error saving note: {str(e)}")
    
    def get_note(self, note_id):
        """Retrieve a note by ID."""
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        if not os.path.exists(filename):
            return None
        
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(f"Error reading note: {str(e)}")
    
    def list_notes(self):
        """List all notes with metadata."""
        notes = []
        
        if not os.path.exists(self.notes_dir):
            return notes
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.notes_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        note = json.load(f)
                        notes.append({
                            "id": note["id"],
                            "title": note["title"],
                            "created_at": note["created_at"],
                            "tags": note.get("tags", [])
                        })
                except Exception:
                    continue
        
        # Sort by creation date, newest first
        notes.sort(key=lambda x: x["created_at"], reverse=True)
        return notes
    
    def update_note(self, note_id, title=None, content=None, tags=None):
        """Update an existing note."""
        note = self.get_note(note_id)
        
        if not note:
            raise ValueError(f"Note with ID {note_id} not found")
        
        if title:
            note["title"] = title
        if content:
            note["content"] = content
        if tags is not None:
            note["tags"] = tags
        
        note["updated_at"] = datetime.now().isoformat()
        
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        try:
            with open(filename, 'w') as f:
                json.dump(note, f, indent=2)
            return note
        except Exception as e:
            raise Exception(f"Error updating note: {str(e)}")
    
    def delete_note(self, note_id):
        """Delete a note by ID."""
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        if not os.path.exists(filename):
            raise ValueError(f"Note with ID {note_id} not found")
        
        try:
            os.remove(filename)
            return True
        except Exception as e:
            raise Exception(f"Error deleting note: {str(e)}")
    
    def search_notes(self, query):
        """Search notes by title, content, or tags."""
        results = []
        query_lower = query.lower()
        
        if not os.path.exists(self.notes_dir):
            return results
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.notes_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        note = json.load(f)
                        
                        # Search in title, content, and tags
                        if (query_lower in note["title"].lower() or
                            query_lower in note["content"].lower() or
                            any(query_lower in tag.lower() for tag in note.get("tags", []))):
                            results.append(note)
                except Exception:
                    continue
        
        return results
    
    def save_conversation(self, conversation_text):
        """Save a conversation as a note."""
        title = f"Chat_{datetime.now().strftime('%Y-%m-%d_%H-%M')}"
        return self.save_note(title, conversation_text, tags=["conversation", "chat"])
