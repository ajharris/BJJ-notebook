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
    
    def save_note(self, title, content, tags=None, category=None):
        """Save a new note with timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        note_id = f"{timestamp}_{title.replace(' ', '_').lower()}"
        
        note = {
            "id": note_id,
            "title": title,
            "content": content,
            "tags": tags or [],
            "category": category or "general",
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
        # Validate note_id to prevent path traversal attacks
        if not note_id or '..' in note_id or '/' in note_id or '\\' in note_id:
            return None
        
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        # Ensure the resolved path is still within notes_dir
        if not os.path.abspath(filename).startswith(os.path.abspath(self.notes_dir)):
            return None
        
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
                            "tags": note.get("tags", []),
                            "category": note.get("category", "general")
                        })
                except Exception:
                    continue
        
        # Sort by creation date, newest first
        notes.sort(key=lambda x: x["created_at"], reverse=True)
        return notes
    
    def update_note(self, note_id, title=None, content=None, tags=None, category=None):
        """Update an existing note."""
        # Validate note_id to prevent path traversal attacks
        if not note_id or '..' in note_id or '/' in note_id or '\\' in note_id:
            raise ValueError(f"Invalid note ID")
        
        note = self.get_note(note_id)
        
        if not note:
            raise ValueError(f"Note with ID {note_id} not found")
        
        if title:
            note["title"] = title
        if content:
            note["content"] = content
        if tags is not None:
            note["tags"] = tags
        if category is not None:
            note["category"] = category
        
        note["updated_at"] = datetime.now().isoformat()
        
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        # Ensure the resolved path is still within notes_dir
        if not os.path.abspath(filename).startswith(os.path.abspath(self.notes_dir)):
            raise ValueError(f"Invalid note ID")
        
        try:
            with open(filename, 'w') as f:
                json.dump(note, f, indent=2)
            return note
        except Exception as e:
            raise Exception(f"Error updating note: {str(e)}")
    
    def delete_note(self, note_id):
        """Delete a note by ID."""
        # Validate note_id to prevent path traversal attacks
        if not note_id or '..' in note_id or '/' in note_id or '\\' in note_id:
            raise ValueError(f"Invalid note ID")
        
        filename = os.path.join(self.notes_dir, f"{note_id}.json")
        
        # Ensure the resolved path is still within notes_dir
        if not os.path.abspath(filename).startswith(os.path.abspath(self.notes_dir)):
            raise ValueError(f"Invalid note ID")
        
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
    
    def get_related_notes(self, note_id):
        """Get notes related to the given note based on category and tags."""
        note = self.get_note(note_id)
        if not note:
            return []
        
        related = []
        note_category = note.get("category", "general")
        note_tags = set(note.get("tags", []))
        
        if not os.path.exists(self.notes_dir):
            return related
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.notes_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        other_note = json.load(f)
                        
                        # Skip the same note
                        if other_note["id"] == note_id:
                            continue
                        
                        # Check if same category or has common tags
                        other_category = other_note.get("category", "general")
                        other_tags = set(other_note.get("tags", []))
                        common_tags = note_tags.intersection(other_tags)
                        
                        if other_category == note_category or len(common_tags) > 0:
                            related.append({
                                "id": other_note["id"],
                                "title": other_note["title"],
                                "category": other_category,
                                "common_tags": list(common_tags),
                                "match_type": "category" if other_category == note_category else "tags"
                            })
                except Exception:
                    continue
        
        # Sort by number of common tags (descending), then by match type
        related.sort(key=lambda x: (len(x.get("common_tags", [])), x["match_type"] == "category"), reverse=True)
        return related
    
    def get_notes_by_category(self, category):
        """Get all notes in a specific category."""
        results = []
        
        if not os.path.exists(self.notes_dir):
            return results
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.notes_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        note = json.load(f)
                        if note.get("category", "general") == category:
                            results.append(note)
                except Exception:
                    continue
        
        return results
    
    def get_all_categories(self):
        """Get list of all categories used in notes."""
        categories = set()
        
        if not os.path.exists(self.notes_dir):
            return []
        
        for filename in os.listdir(self.notes_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(self.notes_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        note = json.load(f)
                        categories.add(note.get("category", "general"))
                except Exception:
                    continue
        
        return sorted(list(categories))
    
    def save_conversation(self, conversation_text):
        """Save a conversation as a note."""
        title = f"Chat_{datetime.now().strftime('%Y-%m-%d_%H-%M')}"
        return self.save_note(title, conversation_text, tags=["conversation", "chat"], category="chat")
