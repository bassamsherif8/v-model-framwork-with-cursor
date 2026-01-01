# V-Model Project Template - Reusable Files & Folders

This document lists all reusable framework files and folders that should be copied when starting a new project.

## 📋 Core Framework Files (Root Level)

### Essential Configuration
- `.cursorrules` - Main project rules file
- `.gitignore` - Git ignore patterns (if exists)

### Dashboard & Documentation
- `V_MODEL_COMPLETE_GUIDE.html` - Complete V-Model workflow guide
- `PROJECT_DASHBOARD.html` - Interactive project dashboard
- `generate_dashboard_data.py` - Dashboard data generator script
- `start_dashboard_server.bat` - Windows batch script for dashboard
- `start_dashboard_server.ps1` - PowerShell script for dashboard
- `HOW_TO_USE_DASHBOARD.md` - Dashboard usage instructions
- `DASHBOARD_README.md` - Dashboard documentation
- `reset_dashboard_data.py` - Script to reset dashboard data to zero state
- `dashboard_data_template.json` - Template for zero-state dashboard data

### Framework Tools
- `vmodel_framework_copier.py` - Framework copier application (v2.0)
- `reset_project_to_template.py` - Project reset tool
- `launch_vmodel_framework_copier.bat` - Launcher for framework copier (Windows)
- `launch_vmodel_framework_copier.ps1` - Launcher for framework copier (PowerShell)
- `launch_reset_tool.bat` - Launcher for reset tool (Windows)
- `launch_reset_tool.ps1` - Launcher for reset tool (PowerShell)
- `TEMPLATE_COPIER_README.md` - Framework copier documentation
- `PROJECT_TEMPLATE_FILES.md` - This file (list of template files)

### Visual Assets
- `v role workflow chart.png` - V-Model workflow visualization

### Environment Setup
- `activate_cad_env.bat` - Windows CMD script to activate the CAD environment (Python 3.11)
- `activate_cad_env.ps1` - PowerShell script to activate the CAD environment (Python 3.11)
- `INSTALLATION_STATUS.md` - Installation status + detailed setup/verification guide for CAD libraries

---

## 📁 Framework Directories

### 1. `cursorrules_modules/` (ENTIRE DIRECTORY)
Complete persona and workflow definitions:
- `00_core.md` - Core tagging rules
- `01_personas/` - All persona definitions:
  - `innovator.md` - @Innovator persona (includes mandatory questioning phases)
  - `innovator_question_templates.md` - Question templates for @Innovator
  - `senior_eng.md` - @SeniorEng persona
  - `design_eng.md` - @DesignEng persona
  - `builder.md` - @Builder persona
  - `skeptic.md` - @Skeptic persona
- `02_workflow.md` - Complete V-Model workflow (includes questioning phases)
- `03_guidelines.md` - Implementation guidelines
- `04_logging.md` - Session logging requirements
- `README.md` - Module documentation

### 2. `02_Design/common_parts/` (ENTIRE DIRECTORY)
Reusable standard parts library:
- `__init__.py`
- `README.md` - Common parts documentation
- `USAGE_EXAMPLES.md` - Usage examples
- `cq_warehouse/` - Standard parts from cq_warehouse library
  - `__init__.py`
  - `README.md` - Catalog of available parts
  - `converters/` - CadQuery to build123d converter
  - `fasteners/` - Standard fasteners library
  - `bearings/` - Standard bearings library
  - `gears/` - Standard gears library
- `custom/` - Custom standard parts templates
  - `wheels/` - Wheel assembly templates
  - `axles/` - Axle assembly templates
  - `hitches/` - Hitch assembly templates

### 3. `02_Design/production/` (ENTIRE DIRECTORY)
Production templates and processes:
- `change_management_workflow.md` - Change management process
- `ECO_log.md` - Engineering Change Order log template
- `generate_supplier_package.py` - Supplier package generator
- `release_documentation_template.md` - Release documentation template
- `release_gate_checklist.md` - Release gate checklist
- `release_log.md` - Release log template
- `supplier_communication_templates.md` - Supplier communication templates

### 4. `02_Design/manufacturing/` (SELECTIVE - Templates Only)
Manufacturing framework templates (NOT project-specific parts):
- `manufacturing_standards.md` - Manufacturing standards reference
- `gdt_system.py` - GD&T system framework
- `drawing_templates.py` - Drawing template definitions
- `freecad_setup.py` - FreeCAD environment setup
- `technical_drawing_generator.py` - Drawing generator framework
- `manufacturing_data.py` - Manufacturing data structure template
- `assembly_instructions.md` - Assembly instructions template
- `manufacturing_notes.md` - Manufacturing notes template
- `torque_specifications.md` - Torque specifications template
- `DFM_checklist.md` - Design for Manufacturing checklist
- `DFA_checklist.md` - Design for Assembly checklist
- `DFM_review_process.md` - DFM review process
- `DFA_review_process.md` - DFA review process
- `process_selection_matrix.md` - Manufacturing process selection
- `tooling_requirements.md` - Tooling requirements template
- `lead_time_estimation.md` - Lead time estimation template
- `assembly_time_estimation.md` - Assembly time estimation template
- `tolerance_stackup_calculator.py` - Tolerance stackup calculator
- `manufacturing_feedback_db.py` - Manufacturing feedback database template
- `manufacturing_feedback_loop.md` - Feedback loop process
- `manufacturing_issue_tracker.py` - Issue tracker template
- `README.md` - Manufacturing framework documentation
- `QUICK_REFERENCE.md` - Quick reference guide
- `USAGE_GUIDE.md` - Usage guide
- `requirements.txt` - Manufacturing dependencies

**EXCLUDE from manufacturing/ (Project-Specific):**
- `__pycache__/` - Python cache
- `drawings/` - Project-specific drawings
- `*_COMPLETE.md` - Project-specific completion reports
- `*_STATUS.md` - Project-specific status reports
- `*_FIXED.md` - Project-specific fixes
- `*_INVESTIGATION*.md` - Project-specific investigations
- `*_SUMMARY.md` - Project-specific summaries
- `*_ANALYSIS.md` - Project-specific analyses
- `*_REPORT.md` - Project-specific reports
- `test_*.py` - Test files
- `fix_*.py` - Fix scripts
- `diagnose_*.py` - Diagnostic scripts
- `batch_*.py` - Batch processing scripts (project-specific)
- `generate_*.py` - Generation scripts (except templates)
- `validate_*.py` - Validation scripts (except templates)
- `simulate_*.py` - Simulation scripts
- `check_*.py` - Check scripts
- `enhance_*.py` - Enhancement scripts
- `run_*.py` - Run scripts
- `export_*.py` - Export scripts (except templates)

### 5. `01_Requirements/` (Templates Only)
Requirements templates:
- `compliance_matrix_template.md` - Compliance matrix template
- `ECO_process.md` - ECO process template
- `requirements_index.md` - Requirements index template (if generic)

**EXCLUDE from requirements/ (Project-Specific):**
- `REQ-*.md` - All project-specific requirements

---

## 📁 Empty Directory Structure (Create but Don't Copy Content)

These directories should be created empty in the new project:

- `00_Concepts/`
  - `components/`
  - `skeletons/`
    - `2d/`
  - `sketches/`
- `01_Requirements/` (already has templates)
- `02_Design/`
  - `parts/` - Project-specific parts
  - `assemblies/` - Project-specific assemblies
  - `skeletons/` - Project-specific 3D skeletons
  - `visualizations/` - Project-specific visualizations
  - `compliance/` - Project-specific compliance
- `03_Implementation/` - Implementation code
- `04_Verification/`
  - `compliance/` - Project-specific compliance tests
  - `manufacturing/` - Project-specific manufacturing verification
  - `production/` - Project-specific production verification
- `logs/` - Session logs

---

## 🚫 Files/Folders to NEVER Copy (Project-Specific)

- `00_Concepts/` - Project-specific concepts
- `01_Requirements/REQ-*.md` - Project-specific requirements
- `02_Design/parts/` - Project-specific parts
- `02_Design/assemblies/` - Project-specific assemblies (except templates)
- `02_Design/skeletons/` - Project-specific skeletons
- `02_Design/compliance/` - Project-specific compliance
- `02_Design/visualizations/` - Project-specific visualizations
- `03_Implementation/` - Project-specific implementation
- `04_Verification/` - Project-specific verification
- `cad_env/` - Virtual environment (recreate in new project)
- `dashboard_data.json` - Project-specific dashboard data
- `logs/` - Project-specific logs
- `*.md` files in root (except templates):
  - `PLAN_OF_IMPROVEMENT.md`
  - `IMPLEMENTATION_SUMMARY.md`
  - `QUICK_FIX_PATH_ISSUE.md`
  - Any project-specific status/summary files

---

## 📝 Post-Copy Actions

After copying the template files:

1. **Update Project Name:**
   - Edit `generate_dashboard_data.py` - Update project name, concept, description
   - Edit `PROJECT_DASHBOARD.html` - Update project name references (if hardcoded)
   - Edit `V_MODEL_COMPLETE_GUIDE.html` - Update project name references (if hardcoded)

2. **Create/Activate CAD Environment (Python 3.11):**
   - First time on a machine, create the environment:
     ```powershell
     py -3.11 -m venv cad_env
     .\cad_env\Scripts\Activate.ps1
     pip install build123d cadquery
     pip install git+https://github.com/gumyr/cq_warehouse.git
     ```
   - Afterwards, use the helper scripts:
     ```powershell
     .\activate_cad_env.ps1      # PowerShell
     :: or, in CMD
     activate_cad_env.bat
     ```
   - For details, see `INSTALLATION_STATUS.md`.

3. **Create Empty Directories:**
   - Create all empty directory structure listed above

4. **Initialize Dashboard:**
   ```bash
   python generate_dashboard_data.py
   ```

5. **Start New Project:**
   - Begin with Phase 1 (Concept) using `@Innovator`
   - Follow V-Model workflow from `cursorrules_modules/02_workflow.md`

---

## 📊 Summary

**Total Files/Folders to Copy:**
- Core files: ~20 files (includes framework tools, launchers, PNG image)
- `cursorrules_modules/`: ~11 files (includes innovator_question_templates.md)
- `common_parts/`: ~15 files
- `production/`: ~7 files
- `manufacturing/` templates: ~25 files
- `requirements/` templates: ~3 files

**Total: ~81 files** (excluding empty directories)

**Total Directories to Create Empty:**
- ~15 directories

