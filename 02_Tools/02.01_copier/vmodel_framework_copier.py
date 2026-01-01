"""
V-Model Framework Copier v2.1
A GUI application to copy reusable framework files from a source project to a new project location.

Usage:
    python vmodel_framework_copier.py
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import json
import fnmatch

class ProjectTemplateCopier:
    def __init__(self, root):
        self.root = root
        self.root.title("V-Model Framework Copier v2.1")
        self.root.geometry("800x700")
        
        # Variables
        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()
        self.copy_status = tk.StringVar(value="Ready to copy")
        
        # Create UI
        self.create_ui()
        
        # Load configuration
        self.load_config()
    
    def create_ui(self):
        """Create the user interface"""
        
        # Title
        title_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="V-Model Framework Copier",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack()
        
        version_label = tk.Label(
            title_frame,
            text="v2.1",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#3498db"
        )
        version_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Copy reusable framework files to start a new project",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        subtitle_label.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Source path
        source_frame = tk.LabelFrame(main_frame, text="Source Project (Template)", padx=10, pady=10)
        source_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(source_frame, text="Source Path:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        source_entry_frame = tk.Frame(source_frame)
        source_entry_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Entry(source_entry_frame, textvariable=self.source_path, font=("Arial", 10)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(
            source_entry_frame,
            text="Browse...",
            command=self.browse_source,
            bg="#3498db",
            fg="white",
            font=("Arial", 10),
            padx=15
        ).pack(side=tk.LEFT)
        
        # Destination path
        dest_frame = tk.LabelFrame(main_frame, text="Destination (New Project)", padx=10, pady=10)
        dest_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(dest_frame, text="Destination Path:", font=("Arial", 10, "bold")).pack(anchor=tk.W)
        
        dest_entry_frame = tk.Frame(dest_frame)
        dest_entry_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Entry(dest_entry_frame, textvariable=self.dest_path, font=("Arial", 10)).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        tk.Button(
            dest_entry_frame,
            text="Browse...",
            command=self.browse_dest,
            bg="#3498db",
            fg="white",
            font=("Arial", 10),
            padx=15
        ).pack(side=tk.LEFT)
        
        # Options
        options_frame = tk.LabelFrame(main_frame, text="Options", padx=10, pady=10)
        options_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.create_empty_dirs = tk.BooleanVar(value=True)
        self.update_project_names = tk.BooleanVar(value=True)
        self.create_readme = tk.BooleanVar(value=True)
        
        tk.Checkbutton(
            options_frame,
            text="Create empty directory structure",
            variable=self.create_empty_dirs,
            font=("Arial", 10)
        ).pack(anchor=tk.W, pady=2)
        
        tk.Checkbutton(
            options_frame,
            text="Create README.md with post-copy instructions",
            variable=self.create_readme,
            font=("Arial", 10)
        ).pack(anchor=tk.W, pady=2)
        
        # Status
        status_frame = tk.LabelFrame(main_frame, text="Status", padx=10, pady=10)
        status_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.status_label = tk.Label(
            status_frame,
            textvariable=self.copy_status,
            font=("Arial", 10),
            anchor=tk.W,
            justify=tk.LEFT
        )
        self.status_label.pack(fill=tk.X)
        
        # Progress bar
        self.progress = ttk.Progressbar(status_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=(10, 0))
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        tk.Button(
            button_frame,
            text="Copy Template Files",
            command=self.copy_files,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="Preview Files",
            command=self.preview_files,
            bg="#f39c12",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="View File Lists",
            command=self.show_file_lists,
            bg="#9b59b6",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        ).pack(side=tk.RIGHT)
    
    def browse_source(self):
        """Browse for source directory"""
        path = filedialog.askdirectory(title="Select Source Project Directory")
        if path:
            self.source_path.set(path)
            self.save_config()
    
    def browse_dest(self):
        """Browse for destination directory"""
        path = filedialog.askdirectory(title="Select Destination Directory")
        if path:
            self.dest_path.set(path)
            self.save_config()
    
    def load_config(self):
        """Load last used paths from config"""
        config_file = Path.home() / ".vmodel_framework_copier.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    self.source_path.set(config.get('source_path', ''))
                    self.dest_path.set(config.get('dest_path', ''))
            except:
                pass
    
    def save_config(self):
        """Save paths to config"""
        config_file = Path.home() / ".vmodel_framework_copier.json"
        try:
            with open(config_file, 'w') as f:
                json.dump({
                    'source_path': self.source_path.get(),
                    'dest_path': self.dest_path.get()
                }, f)
        except:
            pass
    
    def get_files_to_copy(self):
        """Get list of files and directories to copy"""
        source = Path(self.source_path.get())
        
        files_to_copy = []
        dirs_to_copy = []
        
        # Check for new structure first (00_Framework/), fall back to old structure
        has_new_structure = (source / '00_Framework').exists()
        
        if has_new_structure:
            # NEW STRUCTURE: Copy from 00_Framework/
            # Copy entire 00_Framework directory (includes CAD environment, dashboard, memory system, etc.)
            if (source / '00_Framework').exists():
                dirs_to_copy.append('00_Framework')
            
            # Copy .cursorrules (should be at root or in 00_Framework/00.01_cursorrules/)
            if (source / '.cursorrules').exists():
                files_to_copy.append('.cursorrules')
            elif (source / '00_Framework/00.01_cursorrules/.cursorrules').exists():
                files_to_copy.append('00_Framework/00.01_cursorrules/.cursorrules')
            
            # Copy tools
            if (source / '02_Tools').exists():
                dirs_to_copy.append('02_Tools')
            
            # Copy documentation
            if (source / '03_Documentation').exists():
                dirs_to_copy.append('03_Documentation')
            
            # Copy project structure guide
            if (source / 'PROJECT_STRUCTURE.md').exists():
                files_to_copy.append('PROJECT_STRUCTURE.md')
            
            # Copy main README.md (framework-level documentation)
            if (source / 'README.md').exists():
                files_to_copy.append('README.md')
            
            # Copy utility scripts
            if (source / 'reset_dashboard_data.py').exists():
                files_to_copy.append('reset_dashboard_data.py')
            
            # Copy visual reference chart
            if (source / 'v role workflow chart.png').exists():
                files_to_copy.append('v role workflow chart.png')
            
            # Copy CAD environment activation script (if at root)
            if (source / 'cad_env_activate.ps1').exists():
                files_to_copy.append('cad_env_activate.ps1')
        else:
            # OLD STRUCTURE: Copy from old locations (backward compatibility)
            # Core files
            core_files = [
                '.cursorrules',
                'V_MODEL_COMPLETE_GUIDE.html',
                'PROJECT_DASHBOARD.html',
                'generate_dashboard_data.py',
                'start_dashboard_server.bat',
                'start_dashboard_server.ps1',
                'HOW_TO_USE_DASHBOARD.md',
                'DASHBOARD_README.md',
                # CAD Environment files (standardized pattern)
                'activate_cad_env.bat',
                'activate_cad_env.ps1',
                'run_with_cad_env.bat',
                'run_with_cad_env.ps1',
                'setup_cad_env.py',
                'CAD_ENV_SETUP.md',
                # Other core files
                'INSTALLATION_STATUS.md',
                'PROJECT_TEMPLATE_FILES.md',
                'TEMPLATE_COPIER_README.md',
                'reset_dashboard_data.py',
                'reset_project_to_template.py',
                'dashboard_data_template.json',
                'v role workflow chart.png',
            ]
            
            # Launcher scripts
            launcher_files = [
                'launch_vmodel_framework_copier.bat',
                'launch_vmodel_framework_copier.ps1',
                'launch_reset_tool.bat',
                'launch_reset_tool.ps1',
            ]
            
            for file in launcher_files:
                if (source / file).exists():
                    files_to_copy.append(file)
            
            for file in core_files:
                if (source / file).exists():
                    files_to_copy.append(file)
            
            # Directories to copy entirely
            full_dirs = [
                'cursorrules_modules',
                '02_Design/common_parts',
                '02_Design/production',
                '02_Design/visualization_app',
            ]
            
            for dir_path in full_dirs:
                if (source / dir_path).exists():
                    dirs_to_copy.append(dir_path)
        
        # Check for .gitignore
        if (source / '.gitignore').exists():
            files_to_copy.append('.gitignore')
        
        # Note: For NEW STRUCTURE, templates are already included in 00_Framework/
        # No need to add them separately - they will be copied as part of 00_Framework
        # This ensures all framework files (dashboard, templates, memory system, etc.) are copied together
        else:
            # OLD STRUCTURE: Copy from old locations
            # Selective manufacturing files
            manufacturing_files = [
                'manufacturing_standards.md',
                'gdt_system.py',
                'drawing_templates.py',
                'freecad_setup.py',
                'technical_drawing_generator.py',
                'manufacturing_data.py',
                'assembly_instructions.md',
                'manufacturing_notes.md',
                'torque_specifications.md',
                'DFM_checklist.md',
                'DFA_checklist.md',
                'DFM_review_process.md',
                'DFA_review_process.md',
                'process_selection_matrix.md',
                'tooling_requirements.md',
                'lead_time_estimation.md',
                'assembly_time_estimation.md',
                'tolerance_stackup_calculator.py',
                'manufacturing_feedback_db.py',
                'manufacturing_feedback_loop.md',
                'manufacturing_issue_tracker.py',
                'README.md',
                'QUICK_REFERENCE.md',
                'USAGE_GUIDE.md',
                'requirements.txt',
            ]
            
            manufacturing_dir = source / '02_Design' / 'manufacturing'
            if manufacturing_dir.exists():
                for file in manufacturing_files:
                    file_path = manufacturing_dir / file
                    if file_path.exists():
                        files_to_copy.append(f'02_Design/manufacturing/{file}')
            
            # Requirements templates
            req_templates = [
                'compliance_matrix_template.md',
                'ECO_process.md',
            ]
            
            req_dir = source / '01_Requirements'
            if req_dir.exists():
                for file in req_templates:
                    file_path = req_dir / file
                    if file_path.exists():
                        files_to_copy.append(f'01_Requirements/{file}')
                
                # Check for requirements_index.md (if it's a template)
                index_file = req_dir / 'requirements_index.md'
                if index_file.exists():
                    # Check if it's generic (not project-specific)
                    try:
                        content = index_file.read_text()
                        if 'REQ-001' not in content or 'template' in content.lower():
                            files_to_copy.append('01_Requirements/requirements_index.md')
                    except:
                        pass
        
        return files_to_copy, dirs_to_copy
    
    def get_excluded_items(self):
        """Get list of files and directories that are excluded (project-specific)"""
        source = Path(self.source_path.get()) if self.source_path.get() else None
        has_project_specific = source and (source / 'Project_Specific').exists()
        has_old_project = source and (source / '01_Project').exists()
        
        if has_project_specific:
            # NEW STRUCTURE: Exclude Project_Specific/
            excluded_dirs = [
                'Project_Specific',  # All project-specific files
                'cad_env',
                '__pycache__',
            ]
        elif has_old_project:
            # INTERMEDIATE STRUCTURE: Exclude 01_Project/
            excluded_dirs = [
                '01_Project',  # All project-specific files
                'cad_env',
                '__pycache__',
            ]
        else:
            # OLD STRUCTURE: Exclude old project directories
            excluded_dirs = [
                '00_Concepts',
                '01_Requirements/REQ-*.md',  # Pattern for requirements
                '02_Design/parts',
                '02_Design/assemblies',
                '02_Design/skeletons',
                '02_Design/visualizations',
                '02_Design/compliance',
                '03_Implementation',
                '04_Verification',
                'cad_env',
                'logs',
                '__pycache__',
                '02_Design/visualization_app/__pycache__',  # Python cache in visualization_app
                '02_Design/visualization_app/reports',  # Generated reports (project-specific)
            ]
        
        excluded_file_patterns = [
            'REQ-*.md',  # Project-specific requirements
            '*.step',  # STEP files (project-specific parts)
            'dashboard_data.json',  # Project-specific data
            '*_COMPLETE.md',
            '*_STATUS.md',
            '*_SUMMARY.md',
            '*_FIXED.md',
            '*_INVESTIGATION*.md',
            '*_ANALYSIS.md',
            '*_REPORT.md',
            'PLAN_OF_IMPROVEMENT.md',
            'IMPLEMENTATION_SUMMARY.md',
            'QUICK_FIX_*.md',
            # Visualization app project-specific status files
            '02_Design/visualization_app/DEPENDENCIES_INSTALLED.md',
            '02_Design/visualization_app/INSTALLATION_COMPLETE.md',
            '02_Design/visualization_app/INSTALLATION_STATUS.md',
        ]
        
        excluded_manufacturing_patterns = [
            'test_*.py',
            'fix_*.py',
            'diagnose_*.py',
            'batch_*.py',
            'generate_*.py',  # Except templates
            'validate_*.py',
            'simulate_*.py',
            'check_*.py',
            'enhance_*.py',
            'run_*.py',
            'export_*.py',
            'drawings/',
            '*.FCStd',
            '*.FCBak',
        ]
        
        return excluded_dirs, excluded_file_patterns, excluded_manufacturing_patterns
    
    def show_file_lists(self):
        """Show a window with included and excluded files"""
        list_window = tk.Toplevel(self.root)
        list_window.title("Included & Excluded Files - vmodel_framework_copier v2.1")
        list_window.geometry("900x700")
        
        # Create notebook for tabs
        notebook = ttk.Notebook(list_window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Included Files
        included_frame = tk.Frame(notebook)
        notebook.add(included_frame, text="✅ Included Files")
        
        # Included files scrollable text
        included_text_frame = tk.Frame(included_frame)
        included_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        included_scrollbar = tk.Scrollbar(included_text_frame)
        included_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        included_text = tk.Text(
            included_text_frame,
            yscrollcommand=included_scrollbar.set,
            font=("Courier", 9),
            wrap=tk.WORD
        )
        included_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        included_scrollbar.config(command=included_text.yview)
        
        # Tab 2: Excluded Files
        excluded_frame = tk.Frame(notebook)
        notebook.add(excluded_frame, text="❌ Excluded Files")
        
        # Excluded files scrollable text
        excluded_text_frame = tk.Frame(excluded_frame)
        excluded_text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        excluded_scrollbar = tk.Scrollbar(excluded_text_frame)
        excluded_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        excluded_text = tk.Text(
            excluded_text_frame,
            yscrollcommand=excluded_scrollbar.set,
            font=("Courier", 9),
            wrap=tk.WORD
        )
        excluded_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        excluded_scrollbar.config(command=excluded_text.yview)
        
        # Populate included files
        included_text.insert(tk.END, "FILES & DIRECTORIES THAT WILL BE COPIED\n")
        included_text.insert(tk.END, "=" * 80 + "\n\n")
        
        # Core files
        included_text.insert(tk.END, "📄 CORE FRAMEWORK FILES:\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        core_files = [
            '.cursorrules',
            '.gitignore',
            'README.md',
            'PROJECT_STRUCTURE.md',
            'reset_dashboard_data.py',
            'v role workflow chart.png',
            'cad_env_activate.ps1',
            '03_Documentation/03.01_guides/V_MODEL_COMPLETE_GUIDE.html',
            '03_Documentation/03.02_reference/PROJECT_TEMPLATE_FILES.md',
            '03_Documentation/03.01_guides/TEMPLATE_COPIER_README.md',
            '02_Tools/02.02_reset/reset_project_to_template.py',
        ]
        for file in core_files:
            included_text.insert(tk.END, f"  • {file}\n")
        
        # Dashboard files (included in 00_Framework/00.06_dashboard/)
        included_text.insert(tk.END, "\n📊 DASHBOARD FILES (included in 00_Framework/00.06_dashboard/):\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        dashboard_files = [
            'PROJECT_DASHBOARD.html',
            'generate_dashboard_data.py',
            'start_dashboard_server.bat',
            'start_dashboard_server.ps1',
            'HOW_TO_USE_DASHBOARD.md',
            'DASHBOARD_README.md',
            'dashboard_data_template.json',
        ]
        for file in dashboard_files:
            included_text.insert(tk.END, f"  • {file}\n")
        
        # CAD Environment files (included in 00_Framework/00.07_cad_environment/)
        included_text.insert(tk.END, "\n🔧 CAD ENVIRONMENT FILES (included in 00_Framework/00.07_cad_environment/):\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        cad_files = [
            'activate_cad_env.bat',
            'activate_cad_env.ps1',
            'run_with_cad_env.bat',
            'run_with_cad_env.ps1',
            'setup_cad_env.py',
            'CAD_ENV_SETUP.md',
            'CAD_ENVIRONMENT_SOLUTION.md',
        ]
        for file in cad_files:
            included_text.insert(tk.END, f"  • {file}\n")
        
        # Complete directories
        included_text.insert(tk.END, "\n📁 COMPLETE DIRECTORIES (copied entirely):\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        full_dirs = [
            '00_Framework/ (entire framework directory)',
            '  - 00.01_cursorrules/ (personas, workflow, coordination)',
            '  - 00.02_workflow/',
            '  - 00.03_templates/ (concepts, requirements, design, manufacturing)',
            '  - 00.04_common_parts/ (cq_warehouse, custom parts)',
            '  - 00.05_memory_system/ (all 7 memory sections)',
            '  - 00.06_dashboard/ (dashboard HTML, scripts, templates)',
            '  - 00.07_cad_environment/ (CAD environment setup files)',
            '02_Tools/ (copier, reset tools)',
            '03_Documentation/ (guides, reference)',
        ]
        for dir_path in full_dirs:
            included_text.insert(tk.END, f"  • {dir_path}\n")
        
        # Manufacturing templates
        included_text.insert(tk.END, "\n🔧 MANUFACTURING FRAMEWORK TEMPLATES:\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        included_text.insert(tk.END, "  • 00_Framework/00.03_templates/00.03.04_manufacturing/ (entire directory)\n")
        included_text.insert(tk.END, "    Includes: manufacturing_standards.md, gdt_system.py, drawing_templates.py,\n")
        included_text.insert(tk.END, "    freecad_setup.py, technical_drawing_generator.py, DFM/DFA checklists,\n")
        included_text.insert(tk.END, "    process_selection_matrix.md, tolerance_stackup_calculator.py, and more\n")
        
        # Requirements templates
        included_text.insert(tk.END, "\n📋 REQUIREMENTS TEMPLATES:\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        included_text.insert(tk.END, "  • 00_Framework/00.03_templates/00.03.02_requirements/ (entire directory)\n")
        included_text.insert(tk.END, "    Includes: compliance_matrix_template.md, ECO_process.md\n")
        
        # Design templates
        included_text.insert(tk.END, "\n🎨 DESIGN TEMPLATES:\n")
        included_text.insert(tk.END, "-" * 80 + "\n")
        included_text.insert(tk.END, "  • 00_Framework/00.03_templates/00.03.03_design/ (entire directory)\n")
        included_text.insert(tk.END, "    Includes: functional_design/, geometric_state/, visualization_app/\n")
        
        included_text.insert(tk.END, "\n" + "=" * 80 + "\n")
        included_text.insert(tk.END, "Note: Empty directory structure will be created if option is enabled.\n")
        included_text.config(state=tk.DISABLED)
        
        # Populate excluded files
        excluded_text.insert(tk.END, "FILES & DIRECTORIES THAT WILL NOT BE COPIED\n")
        excluded_text.insert(tk.END, "=" * 80 + "\n\n")
        
        excluded_text.insert(tk.END, "🚫 PROJECT-SPECIFIC DIRECTORIES (excluded):\n")
        excluded_text.insert(tk.END, "-" * 80 + "\n")
        excluded_dirs = [
            'Project_Specific/ - All project-specific files (entire directory)',
            '  - 01_Project/01.01_concepts/ - Project-specific concepts and sketches',
            '  - 01_Project/01.02_requirements/REQ-*.md - Project-specific requirements',
            '  - 01_Project/01.03_design/01.03.01_parts/ - Project-specific parts',
            '  - 01_Project/01.03_design/01.03.02_assemblies/ - Project-specific assemblies',
            '  - 01_Project/01.03_design/01.03.03_skeletons/ - Project-specific 3D skeletons',
            '  - 01_Project/01.03_design/01.03.04_visualizations/ - Project-specific visualizations',
            '  - 01_Project/01.03_design/01.03.05_compliance/ - Project-specific compliance',
            '  - 01_Project/01.04_implementation/ - Project-specific implementation code',
            '  - 01_Project/01.05_verification/ - Project-specific verification tests',
            '  - 01_Project/01.06_logs/ - Project-specific session logs',
            'cad_env/ - Virtual environment (recreate in new project)',
            '__pycache__/ - Python cache files',
        ]
        for item in excluded_dirs:
            excluded_text.insert(tk.END, f"  • {item}\n")
        
        excluded_text.insert(tk.END, "\n🚫 PROJECT-SPECIFIC FILES (excluded):\n")
        excluded_text.insert(tk.END, "-" * 80 + "\n")
        excluded_files = [
            'REQ-*.md - All project-specific requirements',
            '*.step - STEP files (project-specific parts)',
            'dashboard_data.json - Project-specific dashboard data',
            '*_COMPLETE.md - Project-specific completion reports',
            '*_STATUS.md - Project-specific status reports',
            '*_SUMMARY.md - Project-specific summaries',
            '*_FIXED.md - Project-specific fixes',
            '*_INVESTIGATION*.md - Project-specific investigations',
            '*_ANALYSIS.md - Project-specific analyses',
            '*_REPORT.md - Project-specific reports',
            'PLAN_OF_IMPROVEMENT.md - Project-specific plans',
            'IMPLEMENTATION_SUMMARY.md - Project-specific summaries',
            'QUICK_FIX_*.md - Project-specific quick fixes',
        ]
        for item in excluded_files:
            excluded_text.insert(tk.END, f"  • {item}\n")
        
        excluded_text.insert(tk.END, "\n🚫 MANUFACTURING PROJECT-SPECIFIC FILES (excluded):\n")
        excluded_text.insert(tk.END, "-" * 80 + "\n")
        excluded_manufacturing = [
            'test_*.py - Test scripts',
            'fix_*.py - Fix scripts',
            'diagnose_*.py - Diagnostic scripts',
            'batch_*.py - Batch processing scripts',
            'generate_*.py - Generation scripts (except templates)',
            'validate_*.py - Validation scripts',
            'simulate_*.py - Simulation scripts',
            'check_*.py - Check scripts',
            'enhance_*.py - Enhancement scripts',
            'run_*.py - Run scripts',
            'export_*.py - Export scripts',
            'drawings/ - Project-specific drawings directory',
            '*.FCStd - FreeCAD project files',
            '*.FCBak - FreeCAD backup files',
        ]
        for item in excluded_manufacturing:
            excluded_text.insert(tk.END, f"  • {item}\n")
        
        excluded_text.insert(tk.END, "\n" + "=" * 80 + "\n")
        excluded_text.insert(tk.END, "Note: These files are project-specific and should not be copied to new projects.\n")
        excluded_text.insert(tk.END, "They will be created fresh for each new project.\n")
        excluded_text.config(state=tk.DISABLED)
    
    def preview_files(self):
        """Preview files that will be copied"""
        if not self.source_path.get() or not Path(self.source_path.get()).exists():
            messagebox.showerror("Error", "Please select a valid source directory")
            return
        
        files, dirs = self.get_files_to_copy()
        
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Files to Copy - Preview")
        preview_window.geometry("600x500")
        
        # Create text widget with scrollbar
        frame = tk.Frame(preview_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, font=("Courier", 9))
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)
        
        # Add content
        text_widget.insert(tk.END, "FILES TO COPY:\n")
        text_widget.insert(tk.END, "=" * 60 + "\n\n")
        
        text_widget.insert(tk.END, f"Core Files ({len([f for f in files if '/' not in f])}):\n")
        for file in files:
            if '/' not in file:
                text_widget.insert(tk.END, f"  • {file}\n")
        
        text_widget.insert(tk.END, f"\nDirectories ({len(dirs)}):\n")
        for dir_path in dirs:
            text_widget.insert(tk.END, f"  • {dir_path}/\n")
        
        text_widget.insert(tk.END, f"\nManufacturing Templates:\n")
        for file in files:
            if 'manufacturing' in file:
                text_widget.insert(tk.END, f"  • {file}\n")
        
        text_widget.insert(tk.END, f"\nRequirements Templates:\n")
        for file in files:
            if 'Requirements' in file:
                text_widget.insert(tk.END, f"  • {file}\n")
        
        text_widget.insert(tk.END, f"\n" + "=" * 60 + "\n")
        text_widget.insert(tk.END, f"Total: {len(files)} files + {len(dirs)} directories\n")
        
        text_widget.config(state=tk.DISABLED)
    
    def should_exclude_file(self, file_path, relative_path):
        """
        Check if a file should be excluded based on patterns
        
        Args:
            file_path: Full path to the file
            relative_path: Relative path from source root
            
        Returns:
            True if file should be excluded, False otherwise
        """
        file_name = file_path.name
        relative_str = str(relative_path).replace('\\', '/')
        
        # Get exclusion patterns
        _, excluded_file_patterns, _ = self.get_excluded_items()
        
        # Check against exclusion patterns
        for pattern in excluded_file_patterns:
            # Handle patterns with paths
            if '/' in pattern:
                if fnmatch.fnmatch(relative_str, pattern):
                    return True
            # Handle filename-only patterns
            elif fnmatch.fnmatch(file_name, pattern):
                return True
        
        # Always exclude __pycache__ directories
        if file_path.is_dir() and file_name == '__pycache__':
            return True
        
        return False
    
    def copy_directory_with_exclusions(self, src_dir, dst_dir, base_path=None):
        """
        Copy directory tree while excluding project-specific files
        
        Args:
            src_dir: Source directory path
            dst_dir: Destination directory path
            base_path: Base path for calculating relative paths (for exclusion matching)
        """
        if base_path is None:
            base_path = src_dir.parent
        
        # Create destination directory
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy files and subdirectories
        for item in src_dir.iterdir():
            relative_path = item.relative_to(base_path)
            
            # Check if should be excluded
            if self.should_exclude_file(item, relative_path):
                continue
            
            dst_item = dst_dir / item.name
            
            if item.is_dir():
                # Recursively copy subdirectory
                self.copy_directory_with_exclusions(item, dst_item, base_path)
            elif item.is_file():
                # Copy file
                shutil.copy2(item, dst_item)
    
    def copy_visualization_app(self, src_dir, dst_dir):
        """
        Copy visualization_app directory while excluding generated/cache files
        
        Args:
            src_dir: Source directory path
            dst_dir: Destination directory path
        """
        # Exclude patterns for visualization_app
        exclude_patterns = [
            '__pycache__',
            'reports',
            '*.pyc',
            '*.pyo',
        ]
        
        exclude_files = [
            'DEPENDENCIES_INSTALLED.md',
            'INSTALLATION_COMPLETE.md',
            'INSTALLATION_STATUS.md',
        ]
        
        # Create destination directory
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy files and subdirectories
        for item in src_dir.iterdir():
            # Skip excluded directories
            if item.is_dir():
                if item.name in ['__pycache__', 'reports']:
                    continue
                # Recursively copy subdirectory
                shutil.copytree(item, dst_dir / item.name, dirs_exist_ok=True)
            # Skip excluded files
            elif item.is_file():
                if item.name in exclude_files:
                    continue
                # Copy file
                shutil.copy2(item, dst_dir / item.name)
    
    def create_empty_directories(self, dest_root):
        """Create empty directory structure"""
        # Check if destination uses new structure (has 00_Framework/)
        has_new_structure = (dest_root / '00_Framework').exists()
        
        has_project_specific = (dest_root / 'Project_Specific').exists()
        
        if has_new_structure and has_project_specific:
            # NEW STRUCTURE: Create complete project directory structure in Project_Specific/01_Project/
            empty_dirs = [
                # Concepts
                'Project_Specific/01_Project/01.01_concepts',
                'Project_Specific/01_Project/01.01_concepts/skeletons',
                'Project_Specific/01_Project/01.01_concepts/skeletons/2d',
                'Project_Specific/01_Project/01.01_concepts/sketches',
                # Requirements
                'Project_Specific/01_Project/01.02_requirements',
                # Design
                'Project_Specific/01_Project/01.03_design',
                'Project_Specific/01_Project/01.03_design/01.03.01_parts',
                'Project_Specific/01_Project/01.03_design/01.03.02_assemblies',
                'Project_Specific/01_Project/01.03_design/01.03.02_assemblies/purchased_components',
                'Project_Specific/01_Project/01.03_design/01.03.03_skeletons',
                'Project_Specific/01_Project/01.03_design/01.03.04_visualizations',
                'Project_Specific/01_Project/01.03_design/01.03.05_compliance',
                # Implementation
                'Project_Specific/01_Project/01.04_implementation',
                # Verification
                'Project_Specific/01_Project/01.05_verification',
                # Logs
                'Project_Specific/01_Project/01.06_logs',
            ]
        elif has_new_structure:
            # INTERMEDIATE STRUCTURE: Create project directories in 01_Project/
            empty_dirs = [
                '01_Project/01.01_concepts/skeletons/2d',
                '01_Project/01.01_concepts/sketches',
                '01_Project/01.03_design/01.03.01_parts',
                '01_Project/01.03_design/01.03.02_assemblies',
                '01_Project/01.03_design/01.03.03_skeletons',
                '01_Project/01.03_design/01.03.04_visualizations',
                '01_Project/01.03_design/01.03.05_compliance',
                '01_Project/01.04_implementation',
                '01_Project/01.05_verification',
                '01_Project/01.06_logs',
            ]
        else:
            # OLD STRUCTURE: Create old directory structure
            empty_dirs = [
                '00_Concepts/components',
                '00_Concepts/skeletons/2d',
                '00_Concepts/sketches',
                '02_Design/parts',
                '02_Design/assemblies',
                '02_Design/skeletons',
                '02_Design/visualizations',
                '02_Design/compliance',
                '03_Implementation',
                '04_Verification/compliance',
                '04_Verification/manufacturing',
                '04_Verification/production',
                'logs',
            ]
        
        for dir_path in empty_dirs:
            full_path = dest_root / dir_path
            full_path.mkdir(parents=True, exist_ok=True)
    
    def create_readme_file(self, dest_root):
        """Create README.md with post-copy instructions"""
        readme_content = """# New V-Model Project

This project was created using the V-Model Project Template.

## Post-Copy Setup

### 1. Create Virtual Environment

```powershell
python -m venv cad_env
.\\cad_env\\Scripts\\Activate.ps1
pip install build123d cadquery cq-warehouse
```

### 2. Update Project Information

Edit `00_Framework/00.06_dashboard/generate_dashboard_data.py` and update:
- Project name
- Project concept
- Project description

### 3. Initialize Dashboard

```bash
python 00_Framework/00.06_dashboard/generate_dashboard_data.py
```

### 4. Start Your Project

Begin with Phase 1 (Concept) using `@Innovator`:
- Follow the V-Model workflow from `00_Framework/00.01_cursorrules/02_workflow.md`
- Use `03_Documentation/03.01_guides/V_MODEL_COMPLETE_GUIDE.html` as your reference

## Project Structure

- `Project_Specific/01_Project/01.01_concepts/` - Concepts and sketches
- `Project_Specific/01_Project/01.02_requirements/` - Requirements (REQ-XXX)
- `Project_Specific/01_Project/01.03_design/` - Design scripts, visualizations, BOMs
  - `01.03.01_parts/` - Custom parts
  - `01.03.02_assemblies/` - Assemblies
  - `01.03.03_skeletons/` - 3D skeletons
  - `01.03.04_visualizations/` - Visualizations
  - `01.03.05_compliance/` - Compliance documents
- `Project_Specific/01_Project/01.04_implementation/` - Code and reviews
- `Project_Specific/01_Project/01.05_verification/` - Tests, coverage, performance
- `Project_Specific/01_Project/01.06_logs/` - Session logs

## Available Resources

- **Common Parts Library:** `00_Framework/00.04_common_parts/`
- **Manufacturing Templates:** `00_Framework/00.03_templates/00.03.04_manufacturing/`
- **Design Templates:** `00_Framework/00.03_templates/00.03.03_design/`
- **Requirements Templates:** `00_Framework/00.03_templates/00.03.02_requirements/`
- **Workflow Guide:** `03_Documentation/03.01_guides/V_MODEL_COMPLETE_GUIDE.html`
- **Dashboard:** `00_Framework/00.06_dashboard/PROJECT_DASHBOARD.html`
- **Personas & Workflow:** `00_Framework/00.01_cursorrules/`

## Getting Started

1. Review `03_Documentation/03.02_reference/PROJECT_TEMPLATE_FILES.md` for a complete list of copied files
2. Read `00_Framework/00.01_cursorrules/README.md` for persona and workflow information
3. Start with `@Innovator` to create your first concept

Good luck with your project!
"""
        
        readme_path = dest_root / 'README.md'
        readme_path.write_text(readme_content)
    
    def copy_files(self):
        """Copy template files to destination"""
        source = Path(self.source_path.get())
        dest = Path(self.dest_path.get())
        
        # Validation
        if not source.exists():
            messagebox.showerror("Error", "Source directory does not exist")
            return
        
        if not dest.exists():
            response = messagebox.askyesno(
                "Create Directory?",
                f"Destination directory does not exist.\n\nCreate '{dest}'?"
            )
            if response:
                dest.mkdir(parents=True, exist_ok=True)
            else:
                return
        
        # Check if destination is empty
        if any(dest.iterdir()):
            response = messagebox.askyesno(
                "Directory Not Empty",
                f"Destination directory is not empty.\n\nContinue anyway?"
            )
            if not response:
                return
        
        # Get files to copy
        files, dirs = self.get_files_to_copy()
        
        if not files and not dirs:
            messagebox.showwarning("Warning", "No files found to copy")
            return
        
        # Start progress
        self.progress.start()
        self.copy_status.set("Copying files...")
        self.root.update()
        
        copied_files = 0
        copied_dirs = 0
        errors = []
        
        try:
            # Copy individual files
            for file_path in files:
                try:
                    src_file = source / file_path
                    dst_file = dest / file_path
                    
                    # Create parent directory
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    
                    # Copy file
                    shutil.copy2(src_file, dst_file)
                    copied_files += 1
                except Exception as e:
                    errors.append(f"Error copying {file_path}: {str(e)}")
            
            # Copy directories
            for dir_path in dirs:
                try:
                    src_dir = source / dir_path
                    dst_dir = dest / dir_path
                    
                    # Special handling for visualization_app to exclude generated files
                    if dir_path == '02_Design/visualization_app':
                        self.copy_visualization_app(src_dir, dst_dir)
                    elif dir_path == '00_Framework':
                        # Use custom copy function for 00_Framework to exclude project-specific files
                        # but ensure all important framework files (including dashboard) are copied
                        self.copy_directory_with_exclusions(src_dir, dst_dir, source)
                    else:
                        # Copy entire directory tree
                        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
                    copied_dirs += 1
                except Exception as e:
                    errors.append(f"Error copying {dir_path}/: {str(e)}")
            
            # Create empty directories
            if self.create_empty_dirs.get():
                self.create_empty_directories(dest)
            
            # Create README
            if self.create_readme.get():
                self.create_readme_file(dest)
            
            # Save config
            self.save_config()
            
            # Success message
            self.progress.stop()
            self.copy_status.set(f"✅ Successfully copied {copied_files} files and {copied_dirs} directories")
            
            message = f"Template files copied successfully!\n\n"
            message += f"Files copied: {copied_files}\n"
            message += f"Directories copied: {copied_dirs}\n"
            
            if errors:
                message += f"\nErrors: {len(errors)}\n"
                message += "\n".join(errors[:5])
                if len(errors) > 5:
                    message += f"\n... and {len(errors) - 5} more"
            
            messagebox.showinfo("Success", message)
            
        except Exception as e:
            self.progress.stop()
            self.copy_status.set(f"❌ Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")

def main():
    root = tk.Tk()
    app = ProjectTemplateCopier(root)
    root.mainloop()

if __name__ == "__main__":
    main()

