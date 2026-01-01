"""
Master Memory Update Script

Updates master_memory.json with current file counts, timestamps, and file lists
for all memory sections. Run this script regularly to keep master memory synchronized.
"""

import json
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def get_file_info(file_path):
    """Get file modification time and size."""
    if os.path.exists(file_path):
        stat = os.stat(file_path)
        return {
            "name": os.path.basename(file_path),
            "path": str(file_path),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
            "size": stat.st_size
        }
    return None

def scan_directory(directory, extensions=None):
    """Scan directory for files and return file info."""
    files = []
    if not os.path.exists(directory):
        return files
    
    for root, dirs, filenames in os.walk(directory):
        for filename in filenames:
            if extensions is None or any(filename.endswith(ext) for ext in extensions):
                file_path = Path(root) / filename
                file_info = get_file_info(file_path)
                if file_info:
                    files.append(file_info)
    
    return files

def update_master_memory():
    """Update master memory JSON with current file information."""
    
    # Load current master memory
    master_memory_path = Path("project_memory/master_memory.json")
    if master_memory_path.exists():
        with open(master_memory_path, 'r') as f:
            master_memory = json.load(f)
    else:
        # Initialize if doesn't exist
        master_memory = {
            "project_name": "[PROJECT_NAME]",
            "last_updated": datetime.now().isoformat(),
            "version": "1.0",
            "memory_sections": {},
            "statistics": {}
        }
    
    # Define memory sections and their locations
    memory_sections = {
        "project_state": {
            "name": "Project State Memory",
            "description": "Tracks current phase, completed work, pending tasks",
            "location": "project_memory/project_state.json",
            "directories": ["project_memory"]
        },
        "decisions": {
            "name": "Decision Memory",
            "description": "Records critical decisions and rationale",
            "location": "project_memory/decisions/decision_log.md",
            "directories": ["project_memory/decisions"]
        },
        "coordination": {
            "name": "Coordination Memory",
            "description": "Tracks persona interactions and agreements",
            "location": "coordination/coordination_log.md",
            "directories": ["coordination"]
        },
        "changes": {
            "name": "Change History Memory",
            "description": "Tracks design changes and impacts",
            "location": "changes/change_log.md",
            "directories": ["changes"]
        },
        "interfaces": {
            "name": "Interface Memory",
            "description": "Single source of truth for interfaces",
            "location": "interfaces/interface_registry.md",
            "directories": ["interfaces"]
        },
        "geometric_state": {
            "name": "Geometric State Memory",
            "description": "Persistent geometric state tracking",
            "location": "02_Design/geometric_state/state_ledger.md",
            "directories": ["02_Design/geometric_state"]
        },
        "validation": {
            "name": "Validation Memory",
            "description": "Tracks validation checkpoints and results",
            "location": "validation/validation_log.md",
            "directories": ["validation"]
        }
    }
    
    # Update each memory section
    total_files = 0
    statistics = defaultdict(int)
    
    for section_id, section_info in memory_sections.items():
        files = []
        last_update = None
        
        # Scan directories for files
        for directory in section_info["directories"]:
            dir_files = scan_directory(directory)
            files.extend(dir_files)
        
        # Find most recent update
        if files:
            last_update = max(files, key=lambda f: f["modified"])["modified"]
        
        # Update section in master memory
        if section_id not in master_memory["memory_sections"]:
            master_memory["memory_sections"][section_id] = {}
        
        master_memory["memory_sections"][section_id].update({
            "name": section_info["name"],
            "description": section_info["description"],
            "location": section_info["location"],
            "files": files,
            "file_count": len(files),
            "last_file_update": last_update
        })
        
        total_files += len(files)
    
    # Update statistics
    master_memory["statistics"] = {
        "total_memory_files": total_files,
        "total_decisions": len([f for f in master_memory["memory_sections"].get("decisions", {}).get("files", [])]),
        "total_coordination_events": 0,  # Would need to parse coordination_log.md
        "total_changes": len([f for f in master_memory["memory_sections"].get("changes", {}).get("files", [])]),
        "total_interfaces": 0,  # Would need to parse interface_registry.md
        "total_validations": len([f for f in master_memory["memory_sections"].get("validation", {}).get("files", [])])
    }
    
    # Update timestamp
    master_memory["last_updated"] = datetime.now().isoformat()
    
    # Save updated master memory
    with open(master_memory_path, 'w') as f:
        json.dump(master_memory, f, indent=2)
    
    print(f"Master memory updated: {total_files} files tracked")
    return master_memory

if __name__ == "__main__":
    update_master_memory()

