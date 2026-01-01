"""
Reset Project to Template
Safely removes project-specific files and folders, keeping only the reusable framework.

WARNING: This will delete project-specific content. Make sure you have backups!
"""

import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

class ProjectResetTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Reset Project to Template - vmodel_framework_copier v2.0")
        self.root.geometry("700x600")
        
        self.project_root = Path(__file__).parent
        
        self.create_ui()
    
    def create_ui(self):
        """Create the user interface"""
        
        # Title
        title_frame = tk.Frame(self.root, bg="#e74c3c", padx=20, pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="⚠️ Reset Project to Template",
            font=("Arial", 18, "bold"),
            bg="#e74c3c",
            fg="white"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Remove project-specific files, keep only framework",
            font=("Arial", 10),
            bg="#e74c3c",
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Warning
        warning_frame = tk.LabelFrame(main_frame, text="⚠️ WARNING", padx=10, pady=10, fg="#e74c3c")
        warning_frame.pack(fill=tk.X, pady=(0, 15))
        
        warning_text = tk.Label(
            warning_frame,
            text="This will PERMANENTLY DELETE project-specific files and folders!\n"
                 "Make sure you have backups before proceeding.\n"
                 "Only reusable framework files will be kept.",
            font=("Arial", 10, "bold"),
            fg="#e74c3c",
            justify=tk.LEFT
        )
        warning_text.pack(anchor=tk.W)
        
        # What will be deleted
        delete_frame = tk.LabelFrame(main_frame, text="Files & Folders to DELETE", padx=10, pady=10)
        delete_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Scrollable list
        scroll_frame = tk.Frame(delete_frame)
        scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(scroll_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.delete_list = tk.Text(
            scroll_frame,
            yscrollcommand=scrollbar.set,
            font=("Courier", 9),
            wrap=tk.WORD,
            bg="#fff3cd"
        )
        self.delete_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.delete_list.yview)
        
        # Populate deletion list
        self.populate_deletion_list()
        
        # What will be kept
        keep_frame = tk.LabelFrame(main_frame, text="Files & Folders to KEEP", padx=10, pady=10)
        keep_frame.pack(fill=tk.X, pady=(0, 15))
        
        keep_text = tk.Label(
            keep_frame,
            text="✅ Framework files (.cursorrules, cursorrules_modules/, common_parts/, production/, templates, dashboard files, etc.)",
            font=("Arial", 9),
            justify=tk.LEFT,
            wraplength=650
        )
        keep_text.pack(anchor=tk.W)
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        tk.Button(
            button_frame,
            text="⚠️ RESET PROJECT",
            command=self.reset_project,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 14, "bold"),
            padx=30,
            pady=15
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=self.root.quit,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        ).pack(side=tk.RIGHT)
    
    def populate_deletion_list(self):
        """Populate the list of files/folders to delete"""
        items_to_delete = []
        
        # Directories to delete entirely
        dirs_to_delete = [
            '00_Concepts',
            '02_Design/parts',
            '02_Design/assemblies',
            '02_Design/skeletons',
            '02_Design/visualizations',
            '02_Design/compliance',
            '03_Implementation',
            '04_Verification',
            'cad_env',
            'logs',
        ]
        
        for dir_path in dirs_to_delete:
            full_path = self.project_root / dir_path
            if full_path.exists():
                items_to_delete.append(f"📁 {dir_path}/")
        
        # Project-specific requirements
        req_dir = self.project_root / '01_Requirements'
        if req_dir.exists():
            req_files = list(req_dir.glob('REQ-*.md'))
            if req_files:
                items_to_delete.append(f"\n📄 01_Requirements/REQ-*.md ({len(req_files)} files)")
        
        # Root level project-specific files
        root_files = [
            'dashboard_data.json',
            'PLAN_OF_IMPROVEMENT.md',
            'IMPLEMENTATION_SUMMARY.md',
            'QUICK_FIX_PATH_ISSUE.md',
        ]
        
        for file in root_files:
            if (self.project_root / file).exists():
                items_to_delete.append(f"📄 {file}")
        
        # Manufacturing project-specific files
        manufacturing_dir = self.project_root / '02_Design' / 'manufacturing'
        if manufacturing_dir.exists():
            # Project-specific patterns
            patterns = [
                ('test_*.py', 'Test scripts'),
                ('fix_*.py', 'Fix scripts'),
                ('diagnose_*.py', 'Diagnostic scripts'),
                ('batch_*.py', 'Batch scripts'),
                ('validate_*.py', 'Validation scripts'),
                ('simulate_*.py', 'Simulation scripts'),
                ('check_*.py', 'Check scripts'),
                ('enhance_*.py', 'Enhancement scripts'),
                ('run_*.py', 'Run scripts'),
                ('export_*.py', 'Export scripts'),
                ('*_COMPLETE.md', 'Completion reports'),
                ('*_STATUS.md', 'Status reports'),
                ('*_SUMMARY.md', 'Summary reports'),
                ('*_FIXED.md', 'Fix reports'),
                ('*_INVESTIGATION*.md', 'Investigation reports'),
                ('*_ANALYSIS.md', 'Analysis reports'),
                ('*_REPORT.md', 'Report files'),
            ]
            
            manufacturing_items = []
            for pattern, desc in patterns:
                files = list(manufacturing_dir.glob(pattern))
                if files:
                    manufacturing_items.append(f"  • {pattern} ({len(files)} files) - {desc}")
            
            if manufacturing_items:
                items_to_delete.append("\n🔧 02_Design/manufacturing/ project-specific files:")
                items_to_delete.extend(manufacturing_items)
            
            # Drawings directory
            drawings_dir = manufacturing_dir / 'drawings'
            if drawings_dir.exists():
                items_to_delete.append(f"  • drawings/ directory")
            
            # FreeCAD files
            fcad_files = list(manufacturing_dir.glob('*.FCStd')) + list(manufacturing_dir.glob('*.FCBak'))
            if fcad_files:
                items_to_delete.append(f"  • *.FCStd, *.FCBak ({len(fcad_files)} files)")
        
        # __pycache__ directories
        pycache_dirs = list(self.project_root.rglob('__pycache__'))
        if pycache_dirs:
            items_to_delete.append(f"\n🗑️ __pycache__/ directories ({len(pycache_dirs)} found)")
        
        # Display in text widget
        self.delete_list.insert(tk.END, "ITEMS TO BE DELETED:\n")
        self.delete_list.insert(tk.END, "=" * 70 + "\n\n")
        
        if items_to_delete:
            for item in items_to_delete:
                self.delete_list.insert(tk.END, item + "\n")
        else:
            self.delete_list.insert(tk.END, "No project-specific files found.\n")
        
        self.delete_list.config(state=tk.DISABLED)
    
    def reset_project(self):
        """Perform the reset operation"""
        # Double confirmation
        response = messagebox.askyesno(
            "⚠️ FINAL CONFIRMATION",
            "Are you ABSOLUTELY SURE you want to delete all project-specific files?\n\n"
            "This action CANNOT be undone!\n\n"
            "Make sure you have backups before proceeding.",
            icon='warning'
        )
        
        if not response:
            return
        
        # Triple confirmation
        response2 = messagebox.askyesno(
            "⚠️ LAST CHANCE",
            "This is your LAST CHANCE to cancel.\n\n"
            "Clicking YES will PERMANENTLY DELETE project-specific files.\n\n"
            "Continue?",
            icon='warning'
        )
        
        if not response2:
            return
        
        deleted_count = 0
        errors = []
        
        try:
            # Delete entire directories
            dirs_to_delete = [
                '00_Concepts',
                '02_Design/parts',
                '02_Design/assemblies',
                '02_Design/skeletons',
                '02_Design/visualizations',
                '02_Design/compliance',
                '03_Implementation',
                '04_Verification',
                'cad_env',
                'logs',
            ]
            
            for dir_path in dirs_to_delete:
                full_path = self.project_root / dir_path
                if full_path.exists():
                    try:
                        shutil.rmtree(full_path)
                        deleted_count += 1
                    except Exception as e:
                        errors.append(f"Error deleting {dir_path}: {str(e)}")
            
            # Delete project-specific requirements
            req_dir = self.project_root / '01_Requirements'
            if req_dir.exists():
                req_files = list(req_dir.glob('REQ-*.md'))
                for req_file in req_files:
                    try:
                        req_file.unlink()
                        deleted_count += 1
                    except Exception as e:
                        errors.append(f"Error deleting {req_file.name}: {str(e)}")
            
            # Delete root level project-specific files
            root_files = [
                'dashboard_data.json',
                'PLAN_OF_IMPROVEMENT.md',
                'IMPLEMENTATION_SUMMARY.md',
                'QUICK_FIX_PATH_ISSUE.md',
            ]
            
            for file in root_files:
                file_path = self.project_root / file
                if file_path.exists():
                    try:
                        file_path.unlink()
                        deleted_count += 1
                    except Exception as e:
                        errors.append(f"Error deleting {file}: {str(e)}")
            
            # Delete manufacturing project-specific files
            manufacturing_dir = self.project_root / '02_Design' / 'manufacturing'
            if manufacturing_dir.exists():
                # Delete files matching patterns
                patterns = [
                    'test_*.py',
                    'fix_*.py',
                    'diagnose_*.py',
                    'batch_*.py',
                    'validate_*.py',
                    'simulate_*.py',
                    'check_*.py',
                    'enhance_*.py',
                    'run_*.py',
                    'export_*.py',
                    '*_COMPLETE.md',
                    '*_STATUS.md',
                    '*_SUMMARY.md',
                    '*_FIXED.md',
                    '*_INVESTIGATION*.md',
                    '*_ANALYSIS.md',
                    '*_REPORT.md',
                ]
                
                for pattern in patterns:
                    files = list(manufacturing_dir.glob(pattern))
                    for file in files:
                        try:
                            file.unlink()
                            deleted_count += 1
                        except Exception as e:
                            errors.append(f"Error deleting {file.name}: {str(e)}")
                
                # Delete drawings directory
                drawings_dir = manufacturing_dir / 'drawings'
                if drawings_dir.exists():
                    try:
                        shutil.rmtree(drawings_dir)
                        deleted_count += 1
                    except Exception as e:
                        errors.append(f"Error deleting drawings/: {str(e)}")
                
                # Delete FreeCAD files
                for pattern in ['*.FCStd', '*.FCBak']:
                    files = list(manufacturing_dir.glob(pattern))
                    for file in files:
                        try:
                            file.unlink()
                            deleted_count += 1
                        except Exception as e:
                            errors.append(f"Error deleting {file.name}: {str(e)}")
            
            # Delete __pycache__ directories
            pycache_dirs = list(self.project_root.rglob('__pycache__'))
            for pycache_dir in pycache_dirs:
                try:
                    shutil.rmtree(pycache_dir)
                    deleted_count += 1
                except Exception as e:
                    errors.append(f"Error deleting {pycache_dir}: {str(e)}")
            
            # Success message
            message = f"✅ Project reset complete!\n\n"
            message += f"Deleted: {deleted_count} items\n"
            
            if errors:
                message += f"\n⚠️ Errors: {len(errors)}\n"
                message += "\n".join(errors[:5])
                if len(errors) > 5:
                    message += f"\n... and {len(errors) - 5} more"
            
            messagebox.showinfo("Reset Complete", message)
            self.root.quit()
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during reset:\n\n{str(e)}")

def main():
    root = tk.Tk()
    app = ProjectResetTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()

