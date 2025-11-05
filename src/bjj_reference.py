"""BJJ reference data including positions, techniques, and concepts."""

BJJ_POSITIONS = {
    "guard": {
        "name": "Guard",
        "description": "Bottom position with legs controlling opponent",
        "types": ["Closed Guard", "Open Guard", "Half Guard", "Butterfly Guard", "Spider Guard", "De La Riva"],
        "key_concepts": ["Distance control", "Hip mobility", "Grip fighting"]
    },
    "mount": {
        "name": "Mount",
        "description": "Top position sitting on opponent's torso",
        "types": ["Full Mount", "High Mount", "S-Mount", "Technical Mount"],
        "key_concepts": ["Weight distribution", "Base", "Posture"]
    },
    "side_control": {
        "name": "Side Control",
        "description": "Top position perpendicular to opponent",
        "types": ["Standard Side Control", "Kesa Gatame", "North-South", "Reverse Kesa Gatame"],
        "key_concepts": ["Pressure", "Shoulder of justice", "Hip control"]
    },
    "back_control": {
        "name": "Back Control",
        "description": "Position behind opponent with hooks",
        "types": ["Standard Back Control", "Body Triangle"],
        "key_concepts": ["Hooks", "Seat belt grip", "Head control"]
    },
    "turtle": {
        "name": "Turtle",
        "description": "Defensive position on hands and knees",
        "types": ["Standard Turtle", "Sitting Turtle"],
        "key_concepts": ["Posture", "Hand fighting", "Preventing back take"]
    }
}

BJJ_TECHNIQUES = {
    "submissions": {
        "chokes": [
            {"name": "Rear Naked Choke", "position": "back_control", "type": "blood choke"},
            {"name": "Guillotine", "position": "guard", "type": "blood choke"},
            {"name": "Triangle Choke", "position": "guard", "type": "blood choke"},
            {"name": "Ezekiel Choke", "position": "mount", "type": "blood choke"},
            {"name": "Bow and Arrow Choke", "position": "back_control", "type": "blood choke"},
        ],
        "armlocks": [
            {"name": "Armbar", "position": "guard", "target": "elbow"},
            {"name": "Kimura", "position": "side_control", "target": "shoulder"},
            {"name": "Americana", "position": "mount", "target": "shoulder"},
            {"name": "Straight Armbar", "position": "mount", "target": "elbow"},
        ],
        "leglocks": [
            {"name": "Straight Ankle Lock", "target": "ankle"},
            {"name": "Heel Hook", "target": "knee"},
            {"name": "Knee Bar", "target": "knee"},
        ]
    },
    "sweeps": [
        {"name": "Scissor Sweep", "from_position": "closed_guard"},
        {"name": "Hip Bump Sweep", "from_position": "closed_guard"},
        {"name": "Butterfly Sweep", "from_position": "butterfly_guard"},
        {"name": "Flower Sweep", "from_position": "closed_guard"},
    ],
    "passes": [
        {"name": "Toreando Pass", "type": "standing"},
        {"name": "Knee Slice", "type": "pressure"},
        {"name": "Over-Under Pass", "type": "pressure"},
        {"name": "X-Pass", "type": "standing"},
    ],
    "escapes": [
        {"name": "Bridge and Roll", "from_position": "mount"},
        {"name": "Elbow Escape (Shrimp)", "from_position": "side_control"},
        {"name": "Hip Escape", "from_position": "side_control"},
        {"name": "Back Escape", "from_position": "back_control"},
    ]
}

BJJ_CONCEPTS = [
    "Position before submission",
    "Base and posture",
    "Frames and angles",
    "Hip mobility and movement",
    "Grip fighting",
    "Weight distribution",
    "Breathing and staying calm",
    "Timing and leverage over strength"
]

def get_position_info(position_key):
    """Get information about a specific BJJ position."""
    return BJJ_POSITIONS.get(position_key.lower().replace(" ", "_"))

def get_techniques_by_type(technique_type):
    """Get techniques by type (submissions, sweeps, passes, escapes)."""
    return BJJ_TECHNIQUES.get(technique_type.lower())

def search_techniques(query):
    """Search for techniques by name."""
    query_lower = query.lower()
    results = []
    
    for category, items in BJJ_TECHNIQUES.items():
        if category == "submissions":
            for sub_category, techniques in items.items():
                for technique in techniques:
                    if query_lower in technique["name"].lower():
                        results.append({**technique, "category": category, "sub_category": sub_category})
        else:
            for technique in items:
                if query_lower in technique["name"].lower():
                    results.append({**technique, "category": category})
    
    return results

def get_all_positions():
    """Get all BJJ positions."""
    return BJJ_POSITIONS

def get_all_concepts():
    """Get all BJJ concepts."""
    return BJJ_CONCEPTS
