"""
Manufacturing Issue Tracker
Tracks manufacturing issues by part number with categorization and resolution tracking

This module provides a system for tracking manufacturing issues, linking them to ECOs,
and generating reports.

Usage:
    from manufacturing_issue_tracker import ManufacturingIssueTracker
    tracker = ManufacturingIssueTracker()
    tracker.add_issue(part_number, category, description, severity)
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional

# Issue tracker data file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ISSUES_FILE = os.path.join(SCRIPT_DIR, "manufacturing_issues.json")

class ManufacturingIssueTracker:
    """
    Manufacturing issue tracking system
    """
    
    def __init__(self, issues_file=None):
        """
        Initialize issue tracker
        
        Args:
            issues_file (str): Path to issues JSON file (optional)
        """
        self.issues_file = issues_file or ISSUES_FILE
        self.issues = self.load_issues()
        self.next_issue_id = self._get_next_id()
    
    def _get_next_id(self):
        """Get next issue ID"""
        if not self.issues:
            return 1
        max_id = max(issue.get("id", 0) for issue in self.issues)
        return max_id + 1
    
    def load_issues(self) -> List[Dict]:
        """Load issues from file"""
        if os.path.exists(self.issues_file):
            try:
                with open(self.issues_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"WARNING: Failed to load issues: {e}")
                return []
        return []
    
    def save_issues(self):
        """Save issues to file"""
        os.makedirs(os.path.dirname(self.issues_file), exist_ok=True)
        with open(self.issues_file, 'w', encoding='utf-8') as f:
            json.dump(self.issues, f, indent=2, ensure_ascii=False)
    
    def add_issue(self, part_number: str, category: str, description: str,
                  severity: str = "Medium", source: str = "Internal",
                  eco_number: Optional[str] = None) -> int:
        """
        Add a new manufacturing issue
        
        Args:
            part_number (str): Part number
            category (str): Issue category (design, tolerance, material, process)
            description (str): Issue description
            severity (str): Severity level (High, Medium, Low)
            source (str): Issue source (Supplier, Internal, Customer)
            eco_number (str): Associated ECO number (optional)
            
        Returns:
            int: Issue ID
        """
        issue = {
            "id": self.next_issue_id,
            "part_number": part_number,
            "category": category,
            "description": description,
            "severity": severity,
            "source": source,
            "status": "Open",
            "eco_number": eco_number,
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
            "resolved_date": None,
            "resolution": None,
            "assigned_to": None
        }
        
        self.issues.append(issue)
        self.next_issue_id += 1
        self.save_issues()
        
        return issue["id"]
    
    def update_issue(self, issue_id: int, **kwargs):
        """
        Update an issue
        
        Args:
            issue_id (int): Issue ID
            **kwargs: Fields to update
        """
        for issue in self.issues:
            if issue["id"] == issue_id:
                for key, value in kwargs.items():
                    if key in issue:
                        issue[key] = value
                issue["updated_date"] = datetime.now().isoformat()
                if kwargs.get("status") == "Resolved":
                    issue["resolved_date"] = datetime.now().isoformat()
                self.save_issues()
                return True
        return False
    
    def resolve_issue(self, issue_id: int, resolution: str):
        """
        Resolve an issue
        
        Args:
            issue_id (int): Issue ID
            resolution (str): Resolution description
        """
        return self.update_issue(issue_id, status="Resolved", resolution=resolution)
    
    def get_issues(self, part_number: Optional[str] = None,
                   status: Optional[str] = None,
                   category: Optional[str] = None) -> List[Dict]:
        """
        Get issues with optional filters
        
        Args:
            part_number (str): Filter by part number (optional)
            status (str): Filter by status (optional)
            category (str): Filter by category (optional)
            
        Returns:
            list: List of matching issues
        """
        filtered = self.issues
        
        if part_number:
            filtered = [i for i in filtered if i["part_number"] == part_number]
        
        if status:
            filtered = [i for i in filtered if i["status"] == status]
        
        if category:
            filtered = [i for i in filtered if i["category"] == category]
        
        return filtered
    
    def get_open_issues(self) -> List[Dict]:
        """Get all open issues"""
        return self.get_issues(status="Open")
    
    def get_issues_by_part(self, part_number: str) -> List[Dict]:
        """Get all issues for a part"""
        return self.get_issues(part_number=part_number)
    
    def generate_report(self, output_file: Optional[str] = None) -> str:
        """
        Generate issue tracking report
        
        Args:
            output_file (str): Output file path (optional)
            
        Returns:
            str: Report content
        """
        if output_file is None:
            output_file = os.path.join(SCRIPT_DIR, "manufacturing_issues_report.md")
        
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Statistics
        total = len(self.issues)
        open_count = len(self.get_open_issues())
        resolved_count = len(self.get_issues(status="Resolved"))
        
        by_category = {}
        by_severity = {}
        by_status = {}
        
        for issue in self.issues:
            category = issue["category"]
            severity = issue["severity"]
            status = issue["status"]
            
            by_category[category] = by_category.get(category, 0) + 1
            by_severity[severity] = by_severity.get(severity, 0) + 1
            by_status[status] = by_status.get(status, 0) + 1
        
        lines = [
            "# Manufacturing Issues Report",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            "",
            f"- **Total Issues:** {total}",
            f"- **Open:** {open_count}",
            f"- **Resolved:** {resolved_count}",
            "",
            "## Statistics",
            "",
            "### By Category",
            ""
        ]
        
        for category, count in sorted(by_category.items()):
            lines.append(f"- **{category}:** {count}")
        
        lines.extend([
            "",
            "### By Severity",
            ""
        ])
        
        for severity, count in sorted(by_severity.items()):
            lines.append(f"- **{severity}:** {count}")
        
        lines.extend([
            "",
            "## Open Issues",
            "",
            "| ID | Part Number | Category | Severity | Description | Created |",
            "|----|------------|----------|----------|-------------|---------|"
        ])
        
        open_issues = self.get_open_issues()
        for issue in sorted(open_issues, key=lambda x: x["id"]):
            created = issue["created_date"][:10]  # Just date
            desc = issue["description"][:50] + "..." if len(issue["description"]) > 50 else issue["description"]
            lines.append(
                f"| {issue['id']} | {issue['part_number']} | {issue['category']} | "
                f"{issue['severity']} | {desc} | {created} |"
            )
        
        lines.append("")
        
        # Write report
        content = '\n'.join(lines)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Issue report saved to: {output_file}")
        return content

if __name__ == "__main__":
    print("Manufacturing Issue Tracker")
    print("="*60)
    print()
    
    tracker = ManufacturingIssueTracker()
    
    # Example usage
    print("Example: Adding an issue...")
    issue_id = tracker.add_issue(
        part_number="DCNC-BASE-PLATFORM-A001",
        category="tolerance",
        description="Tolerance too tight for manufacturing process",
        severity="High",
        source="Supplier"
    )
    print(f"Added issue ID: {issue_id}")
    
    # Generate report
    tracker.generate_report()
    
    print()
    print("Issue tracker ready for use.")

