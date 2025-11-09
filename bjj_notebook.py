#!/usr/bin/env python3
"""BJJ Notebook - Main CLI application."""

import sys
import os
from src.chat_handler import BJJChatHandler
from src.notes_manager import NotesManager
from src.bjj_reference import (
    get_all_positions,
    get_all_concepts,
    search_techniques,
    BJJ_TECHNIQUES
)

class BJJNotebook:
    """Main application class for BJJ Notebook."""
    
    def __init__(self):
        """Initialize the application."""
        self.chat_handler = None
        self.notes_manager = NotesManager()
        self.running = True
    
    def initialize_chat(self):
        """Initialize OpenAI chat handler."""
        if self.chat_handler is None:
            try:
                self.chat_handler = BJJChatHandler()
                print("✓ OpenAI chat initialized successfully!\n")
                return True
            except Exception as e:
                print(f"✗ Error initializing chat: {e}")
                print("You can still use the reference and notes features.\n")
                return False
        return True
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*60)
        print("BJJ NOTEBOOK - Your Brazilian Jiu-Jitsu Assistant")
        print("="*60)
        print("\n📚 Main Menu:")
        print("  1. Chat with BJJ Assistant (OpenAI)")
        print("  2. Browse BJJ Reference")
        print("  3. Manage Notes")
        print("  4. Search Techniques")
        print("  5. Exit")
        print()
    
    def chat_menu(self):
        """Handle chat interactions."""
        if not self.initialize_chat():
            return
        
        print("\n💬 Chat with BJJ Assistant")
        print("-" * 60)
        print("Ask questions about BJJ techniques, positions, or concepts.")
        print("Type 'back' to return to main menu")
        print("Type 'save' to save conversation as a note")
        print("Type 'clear' to start a new conversation")
        print("-" * 60)
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'back':
                break
            
            if user_input.lower() == 'save':
                conversation = self.chat_handler.export_conversation()
                note_id = self.notes_manager.save_conversation(conversation)
                print(f"✓ Conversation saved as note: {note_id}")
                continue
            
            if user_input.lower() == 'clear':
                self.chat_handler.clear_history()
                print("✓ Conversation cleared. Starting fresh!")
                continue
            
            # Get response from AI
            print("\nBJJ Assistant: ", end="", flush=True)
            response = self.chat_handler.chat(user_input)
            print(response)
    
    def reference_menu(self):
        """Browse BJJ reference information."""
        while True:
            print("\n📖 BJJ Reference")
            print("-" * 60)
            print("  1. View Positions")
            print("  2. View Key Concepts")
            print("  3. View Techniques by Category")
            print("  4. Back to Main Menu")
            print()
            
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.show_positions()
            elif choice == '2':
                self.show_concepts()
            elif choice == '3':
                self.show_techniques()
            elif choice == '4':
                break
    
    def show_positions(self):
        """Display BJJ positions."""
        positions = get_all_positions()
        print("\n🥋 BJJ Positions:")
        print("-" * 60)
        
        for key, pos in positions.items():
            print(f"\n{pos['name']}:")
            print(f"  Description: {pos['description']}")
            print(f"  Types: {', '.join(pos['types'])}")
            print(f"  Key Concepts: {', '.join(pos['key_concepts'])}")
    
    def show_concepts(self):
        """Display key BJJ concepts."""
        concepts = get_all_concepts()
        print("\n💡 Key BJJ Concepts:")
        print("-" * 60)
        
        for i, concept in enumerate(concepts, 1):
            print(f"  {i}. {concept}")
    
    def show_techniques(self):
        """Display techniques by category."""
        print("\n🎯 Technique Categories:")
        print("-" * 60)
        print("  1. Submissions")
        print("  2. Sweeps")
        print("  3. Passes")
        print("  4. Escapes")
        print()
        
        choice = input("Select category: ").strip()
        
        if choice == '1':
            self.show_submissions()
        elif choice == '2':
            self.show_category('sweeps')
        elif choice == '3':
            self.show_category('passes')
        elif choice == '4':
            self.show_category('escapes')
    
    def show_submissions(self):
        """Display submissions."""
        subs = BJJ_TECHNIQUES['submissions']
        print("\n🔒 Submissions:")
        print("-" * 60)
        
        print("\nChokes:")
        for tech in subs['chokes']:
            print(f"  • {tech['name']} (from {tech['position']})")
        
        print("\nArmlocks:")
        for tech in subs['armlocks']:
            print(f"  • {tech['name']} (from {tech['position']})")
        
        print("\nLeglocks:")
        for tech in subs['leglocks']:
            print(f"  • {tech['name']}")
    
    def show_category(self, category):
        """Display techniques from a category."""
        techniques = BJJ_TECHNIQUES.get(category, [])
        print(f"\n🎯 {category.title()}:")
        print("-" * 60)
        
        for tech in techniques:
            if 'from_position' in tech:
                print(f"  • {tech['name']} (from {tech['from_position']})")
            elif 'type' in tech:
                print(f"  • {tech['name']} ({tech['type']})")
            else:
                print(f"  • {tech['name']}")
    
    def notes_menu(self):
        """Manage notes."""
        while True:
            print("\n📝 Notes Management")
            print("-" * 60)
            print("  1. Create New Note")
            print("  2. List All Notes")
            print("  3. View Note")
            print("  4. Search Notes")
            print("  5. Delete Note")
            print("  6. Back to Main Menu")
            print()
            
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.create_note()
            elif choice == '2':
                self.list_notes()
            elif choice == '3':
                self.view_note()
            elif choice == '4':
                self.search_notes()
            elif choice == '5':
                self.delete_note()
            elif choice == '6':
                break
    
    def create_note(self):
        """Create a new note."""
        print("\n📝 Create New Note")
        print("-" * 60)
        
        title = input("Note title: ").strip()
        if not title:
            print("✗ Title cannot be empty")
            return
        
        print("Enter note content (press Enter twice to finish):")
        lines = []
        empty_count = 0
        while empty_count < 2:
            line = input()
            if line:
                lines.append(line)
                empty_count = 0
            else:
                empty_count += 1
        
        content = "\n".join(lines).strip()
        if not content:
            print("✗ Content cannot be empty")
            return
        
        category_input = input("Category (general/technique/training/competition/concept): ").strip()
        category = category_input if category_input else "general"
        
        tags_input = input("Tags (comma-separated, optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(',')] if tags_input else []
        
        try:
            note_id = self.notes_manager.save_note(title, content, tags, category)
            print(f"✓ Note saved successfully! ID: {note_id}")
        except Exception as e:
            print(f"✗ Error saving note: {e}")
    
    def list_notes(self):
        """List all notes."""
        notes = self.notes_manager.list_notes()
        
        if not notes:
            print("\n📝 No notes found.")
            return
        
        print(f"\n📝 All Notes ({len(notes)}):")
        print("-" * 60)
        
        for note in notes:
            category_str = f" 📂 {note.get('category', 'general')}"
            tags_str = f" [{', '.join(note['tags'])}]" if note['tags'] else ""
            print(f"  • {note['title']}{category_str}{tags_str}")
            print(f"    ID: {note['id']}")
            print(f"    Created: {note['created_at'][:10]}")
            print()
    
    def view_note(self):
        """View a specific note."""
        note_id = input("\nEnter note ID: ").strip()
        
        try:
            note = self.notes_manager.get_note(note_id)
            if not note:
                print("✗ Note not found")
                return
            
            print(f"\n📝 {note['title']}")
            print("-" * 60)
            print(f"Created: {note['created_at']}")
            print(f"Updated: {note['updated_at']}")
            print(f"Category: {note.get('category', 'general')}")
            if note.get('tags'):
                print(f"Tags: {', '.join(note['tags'])}")
            print("\nContent:")
            print(note['content'])
            print("-" * 60)
            
            # Show related notes
            related_notes = self.notes_manager.get_related_notes(note_id)
            if related_notes:
                print("\n🔗 Related Notes:")
                for related in related_notes[:5]:  # Show up to 5 related notes
                    print(f"  • {related['title']} (Category: {related['category']})")
                    if related.get('common_tags'):
                        print(f"    Common tags: {', '.join(related['common_tags'])}")
                print()
            
        except Exception as e:
            print(f"✗ Error viewing note: {e}")
    
    def search_notes(self):
        """Search notes."""
        query = input("\nSearch query: ").strip()
        
        if not query:
            print("✗ Search query cannot be empty")
            return
        
        results = self.notes_manager.search_notes(query)
        
        if not results:
            print(f"\n📝 No notes found matching '{query}'")
            return
        
        print(f"\n📝 Search Results ({len(results)}):")
        print("-" * 60)
        
        for note in results:
            print(f"  • {note['title']}")
            print(f"    ID: {note['id']}")
            print()
    
    def delete_note(self):
        """Delete a note."""
        note_id = input("\nEnter note ID to delete: ").strip()
        
        confirm = input(f"Are you sure you want to delete '{note_id}'? (yes/no): ").strip().lower()
        
        if confirm != 'yes':
            print("✗ Deletion cancelled")
            return
        
        try:
            self.notes_manager.delete_note(note_id)
            print("✓ Note deleted successfully")
        except Exception as e:
            print(f"✗ Error deleting note: {e}")
    
    def search_techniques_menu(self):
        """Search for techniques."""
        print("\n🔍 Search Techniques")
        print("-" * 60)
        
        query = input("Enter technique name to search: ").strip()
        
        if not query:
            print("✗ Search query cannot be empty")
            return
        
        results = search_techniques(query)
        
        if not results:
            print(f"\n✗ No techniques found matching '{query}'")
            return
        
        print(f"\n🎯 Search Results ({len(results)}):")
        print("-" * 60)
        
        for tech in results:
            print(f"\n  • {tech['name']}")
            print(f"    Category: {tech['category']}")
            if 'sub_category' in tech:
                print(f"    Type: {tech['sub_category']}")
            if 'position' in tech:
                print(f"    From: {tech['position']}")
            if 'type' in tech and tech['category'] != 'submissions':
                print(f"    Type: {tech['type']}")
    
    def run(self):
        """Run the main application loop."""
        print("\n🥋 Welcome to BJJ Notebook!")
        
        # Check if .env file exists
        if not os.path.exists('.env'):
            print("\n⚠️  Warning: No .env file found.")
            print("To use the OpenAI chat feature, create a .env file with your API key.")
            print("See .env.example for reference.\n")
        
        while self.running:
            self.display_menu()
            choice = input("Select option: ").strip()
            
            if choice == '1':
                self.chat_menu()
            elif choice == '2':
                self.reference_menu()
            elif choice == '3':
                self.notes_menu()
            elif choice == '4':
                self.search_techniques_menu()
            elif choice == '5':
                print("\n👋 Thank you for using BJJ Notebook! Train hard!")
                self.running = False
            else:
                print("\n✗ Invalid option. Please try again.")

def main():
    """Main entry point."""
    try:
        app = BJJNotebook()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
