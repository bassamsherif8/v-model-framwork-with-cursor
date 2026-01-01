# New V-Model Project

This project was created using the V-Model Project Template.

## Post-Copy Setup

### 1. Create Virtual Environment

```powershell
python -m venv cad_env
.\cad_env\Scripts\Activate.ps1
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
