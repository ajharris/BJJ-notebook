"""OpenAI chat integration for BJJ assistant."""

import os
from openai import OpenAI
from dotenv import load_dotenv
from .bjj_reference import (
    get_all_positions, 
    get_all_concepts, 
    BJJ_TECHNIQUES
)

# Load environment variables
load_dotenv()

class BJJChatHandler:
    """Handles OpenAI chat interactions for BJJ assistance."""
    
    def __init__(self):
        """Initialize the chat handler with OpenAI client."""
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found in environment variables. "
                "Please create a .env file with your OpenAI API key."
            )
        
        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.conversation_history = []
        
        # Initialize with BJJ context
        self._initialize_system_context()
    
    def _initialize_system_context(self):
        """Set up the system message with BJJ knowledge."""
        positions = get_all_positions()
        concepts = get_all_concepts()
        
        system_message = f"""You are a knowledgeable Brazilian Jiu-Jitsu (BJJ) instructor and assistant. 
Your role is to help students learn BJJ techniques, understand positions, and improve their practice.

You have access to a reference database containing:
- BJJ Positions: {', '.join(positions.keys())}
- Key Concepts: {', '.join(concepts)}
- Technique Categories: Submissions (chokes, armlocks, leglocks), Sweeps, Passes, Escapes

When answering questions:
1. Be clear and instructional
2. Focus on proper technique and safety
3. Reference positions and concepts from the database when relevant
4. Encourage proper training under qualified instruction
5. Take notes of important points the user wants to remember

Always prioritize safety and remind users to train under supervision."""

        self.conversation_history.append({
            "role": "system",
            "content": system_message
        })
    
    def chat(self, user_message):
        """Send a message and get a response from the BJJ assistant."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        try:
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=1000
            )
            
            # Extract assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add to conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            return f"Error communicating with OpenAI: {str(e)}"
    
    def get_conversation_history(self):
        """Get the full conversation history."""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history and reinitialize."""
        self.conversation_history = []
        self._initialize_system_context()
    
    def export_conversation(self):
        """Export conversation history as text."""
        exported = []
        for msg in self.conversation_history:
            if msg["role"] == "system":
                continue
            role = "You" if msg["role"] == "user" else "BJJ Assistant"
            exported.append(f"{role}: {msg['content']}\n")
        return "\n".join(exported)
