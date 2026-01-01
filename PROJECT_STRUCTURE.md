# Project Structure Guide

**Purpose:** This document explains the numbered folder structure and helps navigate the project.

**Last Updated:** [Current Date]

---

## Structure Overview

The project is organized into four main numbered sections:

```
00_Framework/          # Framework/template files (always copied to new projects)
Project_Specific/      # Project-specific files (never copied)
  └── 01_Project/      # Project-specific content
02_Tools/              # Utility tools and scripts
03_Documentation/      # Documentation files
```

---

## 00_Framework/ - Framework & Templates

**Purpose:** All reusable framework files, templates, and system files that should be copied to new projects.

### 00.01_cursorrules/
- **Contents:** Cursor rules modules and persona definitions
- **Files:** All files from `cursorrules_modules/`
- **Purpose:** AI persona definitions and workflow rules
- **Copied to new projects:** Yes

### 00.02_workflow/
- **Contents:** Workflow definitions
- **Files:** `02_workflow.md`
- **Purpose:** V-Model workflow sequence definitions
- **Copied to new projects:** Yes

### 00.03_templates/ - Template Files
- **00.03.01_concepts/** - Concept templates
- **00.03.02_requirements/** - Requirements templates (compliance_matrix_template.md, ECO_process.md)
- **00.03.03_design/** - Design templates (geometric_state, functional_design, visualization_app)
- **00.03.04_manufacturing/** - Manufacturing templates (standards, checklists, processes)
- **Purpose:** All template files for concepts, requirements, design, and manufacturing
- **Copied to new projects:** Yes

### 00.04_common_parts/
- **Contents:** Common parts library
- **Files:** All files from `02_Design/common_parts/`
- **Purpose:** Reusable standard components (fasteners, bearings, etc.)
- **Copied to new projects:** Yes

### 00.05_memory_system/ - Memory System Templates
- **00.05.01_coordination/** - Coordination templates (coordination_log.md, challenge templates)
- **00.05.02_changes/** - Change management templates (change_log.md, change notification templates)
- **00.05.03_interfaces/** - Interface templates (ICD templates, interface_registry.md)
- **00.05.04_validation/** - Validation templates (validation_log.md)
- **00.05.05_project_memory/** - Project memory templates (master_memory.json, decision_log.md)
- **Purpose:** Memory system for tracking decisions, coordination, changes, interfaces, and validation
- **Copied to new projects:** Yes

### 00.06_dashboard/
- **Contents:** Dashboard files
- **Files:** PROJECT_DASHBOARD.html, generate_dashboard_data.py, dashboard_data_template.json, server scripts
- **Purpose:** Project dashboard and data generation
- **Copied to new projects:** Yes

### 00.07_cad_environment/
- **Contents:** CAD environment setup files
- **Files:** activate_cad_env.*, run_with_cad_env.*, setup_cad_env.py, CAD_ENV_SETUP.md
- **Purpose:** CAD virtual environment setup and activation
- **Copied to new projects:** Yes

---

## Project_Specific/ - Project-Specific Files

**Purpose:** All project-specific files that should NOT be copied to new projects.

### Project_Specific/01_Project/01.01_concepts/
- **Contents:** Project concepts and sketches
- **Files:** All files from old `00_Concepts/`
- **Purpose:** Project-specific concept documents
- **Copied to new projects:** No

### Project_Specific/01_Project/01.02_requirements/
- **Contents:** Project requirements
- **Files:** All REQ-*.md files from old `01_Requirements/`
- **Purpose:** Project-specific requirements
- **Copied to new projects:** No

### Project_Specific/01_Project/01.03_design/ - Project Design Files
- **01.03.01_parts/** - Project parts (STEP files, Python scripts)
- **01.03.02_assemblies/** - Project assemblies (STEP files, BOMs)
- **01.03.03_skeletons/** - Project 3D skeletons
- **01.03.04_visualizations/** - Project visualizations
- **01.03.05_compliance/** - Project compliance documents
- **Purpose:** All project-specific design files
- **Copied to new projects:** No

### Project_Specific/01_Project/01.04_implementation/
- **Contents:** Project implementation code
- **Files:** All files from old `03_Implementation/`
- **Purpose:** Project-specific code
- **Copied to new projects:** No

### Project_Specific/01_Project/01.05_verification/
- **Contents:** Project verification tests
- **Files:** All files from old `04_Verification/`
- **Purpose:** Project-specific tests and validation
- **Copied to new projects:** No

### Project_Specific/01_Project/01.06_logs/
- **Contents:** Project session logs
- **Files:** All files from old `logs/`
- **Purpose:** Project-specific session logs
- **Copied to new projects:** No

---

## 02_Tools/ - Utility Tools

**Purpose:** Tools and scripts for project management.

### 02.01_copier/
- **Contents:** Framework copier tool
- **Files:** vmodel_framework_copier.py, launch scripts
- **Purpose:** Copy framework files to new projects
- **Copied to new projects:** Yes

### 02.02_reset/
- **Contents:** Reset tools
- **Files:** reset_project_to_template.py, launch scripts
- **Purpose:** Reset project to template state
- **Copied to new projects:** Yes

### 02.03_dashboard/
- **Contents:** Dashboard tools
- **Files:** Dashboard server scripts
- **Purpose:** Dashboard management tools
- **Copied to new projects:** Yes

---

## 03_Documentation/ - Documentation

**Purpose:** User guides and reference documentation.

### 03.01_guides/
- **Contents:** User guides
- **Files:** V_MODEL_COMPLETE_GUIDE.html, HOW_TO_USE_DASHBOARD.md, etc.
- **Purpose:** Step-by-step guides for users
- **Copied to new projects:** Yes

### 03.02_reference/
- **Contents:** Reference documentation
- **Files:** CAD_ENV_SETUP.md, PROJECT_TEMPLATE_FILES.md, etc.
- **Purpose:** Reference documentation
- **Copied to new projects:** Yes

---

## File Mapping (Old → New)

### Framework Files
| Old Location | New Location |
| :--- | :--- |
| cursorrules_modules/ | 00_Framework/00.01_cursorrules/ |
| .cursorrules | 00_Framework/00.01_cursorrules/ (also at root) |
| coordination/ | 00_Framework/00.05_memory_system/00.05.01_coordination/ |
| changes/ | 00_Framework/00.05_memory_system/00.05.02_changes/ |
| interfaces/ | 00_Framework/00.05_memory_system/00.05.03_interfaces/ |
| validation/ | 00_Framework/00.05_memory_system/00.05.04_validation/ |
| project_memory/ | 00_Framework/00.05_memory_system/00.05.05_project_memory/ |
| 02_Design/common_parts/ | 00_Framework/00.04_common_parts/ |
| 02_Design/manufacturing/ (templates) | 00_Framework/00.03_templates/00.03.04_manufacturing/ |
| 02_Design/production/ | 00_Framework/00.03_templates/00.03.04_manufacturing/production/ |
| 02_Design/geometric_state/ (templates) | 00_Framework/00.03_templates/00.03.03_design/geometric_state/ |
| PROJECT_DASHBOARD.html | 00_Framework/00.06_dashboard/ |
| generate_dashboard_data.py | 00_Framework/00.06_dashboard/ |

### Project Files
| Old Location | New Location |
| :--- | :--- |
| 00_Concepts/ | Project_Specific/01_Project/01.01_concepts/ |
| 01_Requirements/REQ-*.md | Project_Specific/01_Project/01.02_requirements/ |
| 02_Design/parts/ | Project_Specific/01_Project/01.03_design/01.03.01_parts/ |
| 02_Design/assemblies/ | Project_Specific/01_Project/01.03_design/01.03.02_assemblies/ |
| 02_Design/skeletons/ | Project_Specific/01_Project/01.03_design/01.03.03_skeletons/ |
| 02_Design/visualizations/ | Project_Specific/01_Project/01.03_design/01.03.04_visualizations/ |
| 02_Design/compliance/ | Project_Specific/01_Project/01.03_design/01.03.05_compliance/ |
| 03_Implementation/ | Project_Specific/01_Project/01.04_implementation/ |
| 04_Verification/ | Project_Specific/01_Project/01.05_verification/ |
| logs/ | Project_Specific/01_Project/01.06_logs/ |

### Tools
| Old Location | New Location |
| :--- | :--- |
| vmodel_framework_copier.py | 02_Tools/02.01_copier/ |
| reset_project_to_template.py | 02_Tools/02.02_reset/ |

### Documentation
| Old Location | New Location |
| :--- | :--- |
| V_MODEL_COMPLETE_GUIDE.html | 03_Documentation/03.01_guides/ |
| HOW_TO_USE_DASHBOARD.md | 03_Documentation/03.01_guides/ |
| CAD_ENV_SETUP.md | 03_Documentation/03.02_reference/ |

---

## Navigation Tips

1. **Looking for framework files?** → Check `00_Framework/`
2. **Looking for project files?** → Check `Project_Specific/01_Project/`
3. **Looking for tools?** → Check `02_Tools/`
4. **Looking for documentation?** → Check `03_Documentation/`
5. **Numbering system:** First number = main category, second number = subcategory
6. **Template vs Project:** If it's in `00_Framework/`, it's a template. If it's in `Project_Specific/`, it's project-specific.

---

## Migration Status

**Migration Complete:**
- Old structure folders have been removed
- All files moved to new numbered structure
- **Use new structure for all work**

---

## For New Projects

When copying framework to a new project:
- Copy everything from `00_Framework/`
- Copy tools from `02_Tools/`
- Copy documentation from `03_Documentation/`
- **DO NOT copy** anything from `Project_Specific/` (project-specific)

---

## See Also

- `STRUCTURE_MIGRATION.md` - Migration guide
- `00_Framework/00.01_cursorrules/README.md` - Cursor rules documentation
- `03_Documentation/03.01_guides/V_MODEL_COMPLETE_GUIDE.html` - Complete workflow guide

