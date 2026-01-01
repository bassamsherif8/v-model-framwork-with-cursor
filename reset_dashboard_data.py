"""
Reset Dashboard Data to Zero
Resets dashboard_data.json to initial/zero state for a new project.
"""

import json
from pathlib import Path
from datetime import datetime

def reset_dashboard_data():
    """Reset dashboard data to zero state"""
    
    project_root = Path(__file__).parent
    dashboard_file = project_root / "dashboard_data.json"
    template_file = project_root / "dashboard_data_template.json"
    
    # Create zero-state template
    zero_state = {
        "projectName": "New V-Model Project",
        "projectConcept": "Concept Phase",
        "projectDescription": "Enter your project description here",
        "currentPhase": {
            "number": 1,
            "name": "Concept Phase",
            "subPhase": "Initial Concept Development",
            "progress": 0
        },
        "requirements": {
            "total": 0,
            "approved": 0,
            "inProgress": 0,
            "pending": 0,
            "list": []
        },
        "design": {
            "conceptSketches": "pending",
            "skeletons": "pending",
            "manufacturing": "pending",
            "assemblies": "pending",
            "drawings": "pending",
            "dfm": "pending",
            "dfa": "pending",
            "stepValidation": "pending",
            "assemblyValidation": "pending",
            "gdtDrawings": "pending",
            "commonParts": "active"
        },
        "production": {
            "preReview": "pending",
            "releaseGate": "pending",
            "releasePackage": "pending",
            "version": None
        },
        "changeManagement": {
            "openECOs": 0,
            "pendingApproval": 0,
            "approved": 0,
            "list": []
        },
        "compliance": {
            "matrix": "pending",
            "testing": "pending",
            "certification": "pending"
        },
        "manufacturingFeedback": {
            "tools": "pending",
            "data": "pending",
            "status": "pending"
        },
        "recentActivity": [],
        "timeline": {
            "projectInitiated": None,
            "events": []
        },
        "lastUpdated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Write to dashboard_data.json
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        json.dump(zero_state, f, indent=2, ensure_ascii=False)
    
    # Also save as template for future use
    with open(template_file, 'w', encoding='utf-8') as f:
        json.dump(zero_state, f, indent=2, ensure_ascii=False)
    
    print("[OK] Dashboard data reset to zero state!")
    print(f"   File: {dashboard_file}")
    print(f"   Phase: Concept Phase (0% progress)")
    print(f"   All statuses: pending/zero")
    print(f"   Last updated: {zero_state['lastUpdated']}")

if __name__ == "__main__":
    reset_dashboard_data()

