"""
Manufacturing Feedback Database
Stores and analyzes manufacturing feedback from suppliers, internal, and customers

This module provides a database system for storing manufacturing feedback,
linking it to part numbers and revisions, and generating analysis reports.

Usage:
    from manufacturing_feedback_db import ManufacturingFeedbackDB
    db = ManufacturingFeedbackDB()
    db.add_feedback(part_number, source, category, feedback_text)
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional

# Feedback database file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDBACK_FILE = os.path.join(SCRIPT_DIR, "manufacturing_feedback.json")

class ManufacturingFeedbackDB:
    """
    Manufacturing feedback database
    """
    
    def __init__(self, feedback_file=None):
        """
        Initialize feedback database
        
        Args:
            feedback_file (str): Path to feedback JSON file (optional)
        """
        self.feedback_file = feedback_file or FEEDBACK_FILE
        self.feedback = self.load_feedback()
        self.next_feedback_id = self._get_next_id()
    
    def _get_next_id(self):
        """Get next feedback ID"""
        if not self.feedback:
            return 1
        max_id = max(entry.get("id", 0) for entry in self.feedback)
        return max_id + 1
    
    def load_feedback(self) -> List[Dict]:
        """Load feedback from file"""
        if os.path.exists(self.feedback_file):
            try:
                with open(self.feedback_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"WARNING: Failed to load feedback: {e}")
                return []
        return []
    
    def save_feedback(self):
        """Save feedback to file"""
        os.makedirs(os.path.dirname(self.feedback_file), exist_ok=True)
        with open(self.feedback_file, 'w', encoding='utf-8') as f:
            json.dump(self.feedback, f, indent=2, ensure_ascii=False)
    
    def add_feedback(self, part_number: str, source: str, category: str,
                     feedback_text: str, revision: Optional[str] = None,
                     impact: Optional[str] = None) -> int:
        """
        Add feedback entry
        
        Args:
            part_number (str): Part number
            source (str): Feedback source (Supplier, Internal, Customer)
            category (str): Category (Design Issue, Cost Optimization, Quality Improvement)
            feedback_text (str): Feedback text
            revision (str): Part revision (optional)
            impact (str): Impact description (optional)
            
        Returns:
            int: Feedback ID
        """
        entry = {
            "id": self.next_feedback_id,
            "part_number": part_number,
            "revision": revision,
            "source": source,
            "category": category,
            "feedback": feedback_text,
            "impact": impact,
            "date": datetime.now().isoformat(),
            "status": "New",
            "action_taken": None,
            "resolved": False
        }
        
        self.feedback.append(entry)
        self.next_feedback_id += 1
        self.save_feedback()
        
        return entry["id"]
    
    def update_feedback(self, feedback_id: int, **kwargs):
        """
        Update feedback entry
        
        Args:
            feedback_id (int): Feedback ID
            **kwargs: Fields to update
        """
        for entry in self.feedback:
            if entry["id"] == feedback_id:
                for key, value in kwargs.items():
                    if key in entry:
                        entry[key] = value
                self.save_feedback()
                return True
        return False
    
    def get_feedback(self, part_number: Optional[str] = None,
                     source: Optional[str] = None,
                     category: Optional[str] = None,
                     resolved: Optional[bool] = None) -> List[Dict]:
        """
        Get feedback with optional filters
        
        Args:
            part_number (str): Filter by part number (optional)
            source (str): Filter by source (optional)
            category (str): Filter by category (optional)
            resolved (bool): Filter by resolved status (optional)
            
        Returns:
            list: List of matching feedback entries
        """
        filtered = self.feedback
        
        if part_number:
            filtered = [f for f in filtered if f["part_number"] == part_number]
        
        if source:
            filtered = [f for f in filtered if f["source"] == source]
        
        if category:
            filtered = [f for f in filtered if f["category"] == category]
        
        if resolved is not None:
            filtered = [f for f in filtered if f["resolved"] == resolved]
        
        return filtered
    
    def analyze_trends(self) -> Dict:
        """
        Analyze feedback trends
        
        Returns:
            dict: Trend analysis results
        """
        analysis = {
            "total_feedback": len(self.feedback),
            "by_source": {},
            "by_category": {},
            "by_part": {},
            "common_issues": [],
            "unresolved_count": 0
        }
        
        for entry in self.feedback:
            # By source
            source = entry["source"]
            analysis["by_source"][source] = analysis["by_source"].get(source, 0) + 1
            
            # By category
            category = entry["category"]
            analysis["by_category"][category] = analysis["by_category"].get(category, 0) + 1
            
            # By part
            part = entry["part_number"]
            analysis["by_part"][part] = analysis["by_part"].get(part, 0) + 1
            
            # Unresolved
            if not entry["resolved"]:
                analysis["unresolved_count"] += 1
        
        return analysis
    
    def generate_analysis_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate feedback analysis report
        
        Args:
            output_file (str): Output file path (optional)
            
        Returns:
            str: Report content
        """
        if output_file is None:
            output_file = os.path.join(SCRIPT_DIR, "manufacturing_feedback_analysis.md")
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        analysis = self.analyze_trends()
        
        lines = [
            "# Manufacturing Feedback Analysis Report",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            "",
            f"- **Total Feedback Entries:** {analysis['total_feedback']}",
            f"- **Unresolved:** {analysis['unresolved_count']}",
            "",
            "## Feedback by Source",
            ""
        ]
        
        for source, count in sorted(analysis["by_source"].items(), key=lambda x: -x[1]):
            percentage = (count / analysis["total_feedback"] * 100) if analysis["total_feedback"] > 0 else 0
            lines.append(f"- **{source}:** {count} ({percentage:.1f}%)")
        
        lines.extend([
            "",
            "## Feedback by Category",
            ""
        ])
        
        for category, count in sorted(analysis["by_category"].items(), key=lambda x: -x[1]):
            percentage = (count / analysis["total_feedback"] * 100) if analysis["total_feedback"] > 0 else 0
            lines.append(f"- **{category}:** {count} ({percentage:.1f}%)")
        
        lines.extend([
            "",
            "## Feedback by Part",
            ""
        ])
        
        for part, count in sorted(analysis["by_part"].items(), key=lambda x: -x[1])[:10]:  # Top 10
            lines.append(f"- **{part}:** {count} entries")
        
        lines.extend([
            "",
            "## Recommendations",
            ""
        ])
        
        if analysis["unresolved_count"] > 0:
            lines.append(f"- ⚠️ {analysis['unresolved_count']} unresolved feedback entries - review and take action")
        
        # Identify common issues
        category_counts = analysis["by_category"]
        if category_counts:
            most_common = max(category_counts.items(), key=lambda x: x[1])
            lines.append(f"- Most common category: **{most_common[0]}** ({most_common[1]} entries)")
            lines.append(f"  - Consider design improvements in this area")
        
        lines.append("")
        
        # Write report
        content = '\n'.join(lines)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Feedback analysis report saved to: {output_file}")
        return content

if __name__ == "__main__":
    print("Manufacturing Feedback Database")
    print("="*60)
    print()
    
    db = ManufacturingFeedbackDB()
    
    # Example usage
    print("Example: Adding feedback...")
    feedback_id = db.add_feedback(
        part_number="DCNC-BASE-PLATFORM-A001",
        source="Supplier",
        category="Design Issue",
        feedback_text="Tolerance on actuator mount holes is too tight for standard tooling",
        impact="Requires special tooling, increases cost"
    )
    print(f"Added feedback ID: {feedback_id}")
    
    # Generate analysis
    db.generate_analysis_report()
    
    print()
    print("Feedback database ready for use.")

