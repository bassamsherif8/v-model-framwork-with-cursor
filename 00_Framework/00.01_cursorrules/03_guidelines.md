# Implementation Guidelines

## Persona Tagging & Activation

- **When a user mentions a persona handle** (e.g., `@Innovator`, `@SeniorEng`):
  - **IMMEDIATELY** adopt that persona's role and behavior
  - Respond in first person as that persona
  - Follow the persona's specific instructions, constraints, and output formats
  - Maintain consistency with the V-Model workflow
  - Use the persona's characteristic language and mindset

- **When multiple personas are tagged:**
  - Address each persona's perspective in sequence
  - Show how they would collaborate or debate
  - Maintain each persona's distinct voice and priorities

- **When no persona is tagged:**
  - Infer the appropriate persona based on the V-Model phase
  - Or default to a neutral engineering assistant role
  - Ask for clarification if the phase is unclear

## When Working on a New Feature

- Always start with the Concept Phase unless explicitly told otherwise
- Do not skip phases in the V-Model workflow
- Ensure traceability between requirements, design, implementation, and tests

## File Organization

- Concepts: `00_Concepts/` directory
  - Skeletons: `00_Concepts/skeletons/` directory (concept skeleton files)
  - 2D Skeletons: `00_Concepts/skeletons/2d/` directory (2D skeleton sketches)
  - Sketches: `00_Concepts/sketches/` directory (detailed 2D concept sketches)
- Requirements: `01_Requirements/` directory
- Design scripts: `02_Design/` directory
  - Common Parts: `02_Design/common_parts/` directory (reusable standard components)
    - cq_warehouse: CadQuery-based standard parts (fasteners, bearings, gears)
    - custom: Custom standard parts using build123d (wheels, axles, hitches)
  - Skeletons: `02_Design/skeletons/` directory (3D initial skeleton files)
  - Parts: `02_Design/parts/` directory (manufacturing-ready 3D files)
  - Assemblies: `02_Design/assemblies/` directory (final assemblies)
  - Visualizations: `02_Design/visualizations/` directory (design renderings and drawings)
  - History: `02_Design/history/` directory (design version history)
  - Reviews: `02_Design/reviews/` directory (design review documentation)
  - Compliance: `02_Design/compliance/` directory (requirements compliance matrices)
  - Manufacturing: `02_Design/manufacturing/` directory (technical drawings, GD&T, manufacturing notes)
- Implementation code: `03_Implementation/` directory
  - Reviews: `03_Implementation/reviews/` directory (code review documentation)
- Tests: `04_Verification/` directory
  - Coverage: `04_Verification/coverage/` directory (test coverage reports)
  - Performance: `04_Verification/performance/` directory (performance benchmark results)
- Logs: `logs/session_log.md`

## Code Standards

- All code must be well-commented
- Function headers must reference requirement IDs when applicable
- Python scripts should follow PEP 8 style guidelines
- Use meaningful variable and function names

## Documentation

- Requirements must use YAML frontmatter with ID, Priority, and Status
- All design decisions should be documented
- Test results should be recorded

## CAD Environment Management (MANDATORY for CAD Projects)

### Standard Pattern

All V-Model projects requiring CAD libraries (build123d, FreeCAD) MUST include:

1. **CAD Virtual Environment:**
   - Location: `cad_env/` (Python 3.11)
   - Purpose: Isolated Python environment for CAD libraries
   - Dependencies: build123d, cadquery-ocp, cadquery, cq-warehouse
   - **Setup:** Run `python setup_cad_env.py` to create and configure

2. **Activation Scripts:**
   - `activate_cad_env.bat` - Windows batch activation (keeps window open)
   - `activate_cad_env.ps1` - PowerShell activation
   - Both scripts verify installation and show Python version

3. **Generic Wrapper Scripts:**
   - `run_with_cad_env.bat` - Run any Python script with CAD env (Windows)
   - `run_with_cad_env.ps1` - PowerShell version
   - Usage: `run_with_cad_env.bat "script.py" [args]`
   - **Benefits:** Automatically activates env, verifies dependencies, keeps window open

4. **Project-Specific Wrappers:**
   - For frequently used scripts, create wrappers:
   - Pattern: `[script_name]_with_cad_env.bat`
   - Example: `generate_step_files_with_cad_env.bat`
   - Activates env → Runs script → Shows results → Pauses

### Best Practices

- **Always use wrapper scripts** for scripts requiring CAD libraries
- **Never assume environment is activated** - always activate in wrapper
- **Keep windows open** - Use `pause` in batch files to see results
- **Verify dependencies** - Check build123d/OCP before running scripts
- **Document in README** - Include CAD env activation instructions in project README
- **Use Python 3.11** - OCP has pre-built wheels for Python 3.11 (not 3.14+)

### Setup Process for New Projects

1. **Copy framework** using V-Model Framework Copier (includes CAD env files)
2. **Run setup:** `python setup_cad_env.py`
3. **Verify:** `.\activate_cad_env.ps1` then `python -c "import build123d; print('OK')"`
4. **Use wrappers:** `.\run_with_cad_env.bat "your_script.py"`

### Documentation

- See `CAD_ENV_SETUP.md` for complete setup and troubleshooting guide
- All CAD environment files are automatically included by framework copier

## Common Parts Library

- **Purpose:** Standardized, reusable components that can be used across multiple projects
- **Location:** `02_Design/common_parts/` directory
- **Structure:**
  - `cq_warehouse/` - CadQuery-based standard parts (fasteners, bearings, gears)
  - `custom/` - Custom standard parts using build123d (wheels, axles, hitches)
  - Each category has wrapper functions and specifications database

- **Usage:**
  - When designing assemblies, ALWAYS check common_parts library first
  - Use standard components from library when possible
  - Add new standard components to library for future use
  - Reference common parts in BOM with part numbers

- **Purchased Components (MANDATORY):**
  - **CRITICAL:** Even if components are purchased (not custom-designed), they MUST be represented in detail in assemblies
  - Create detailed 3D models of purchased components (axles, wheels, motors, pumps, generators, etc.)
  - Use accurate dimensions from supplier datasheets or standard specifications
  - Include all mounting interfaces, connection points, and critical dimensions
  - Store purchased component models in `02_Design/common_parts/custom/` or `02_Design/assemblies/purchased_components/`
  - File naming: `[PROJECT]-[COMPONENT-TYPE]-[SPEC]-[REVISION].step`
  - **DO NOT use placeholders** - all purchased components must have detailed 3D representation
  - Purpose: Enable clearance/interference checking, interface verification, and complete assembly visualization

- **CAD Library Selection:**
  - Standard parts → Use cq_warehouse via common_parts wrappers
  - Custom parts → Use build123d directly
  - Assemblies → Use build123d as primary, import cq_warehouse parts via converter

- **Installation:**
  ```bash
  # Activate CAD environment first
  .\activate_cad_env.ps1
  pip install cadquery cq-warehouse
  ```

- **Part Numbering:**
  - Format: `[PROJECT]-COMMON-[CATEGORY]-[SPEC]-[REVISION]`
  - Example: `DCS-COMMON-FAST-M6X20-SS-A001`
  - Categories: FAST (fasteners), BRG (bearings), GEAR (gears), WHEEL (wheels), AXLE (axles), HITCH (hitches)

- **Import Pattern:**
  ```python
  # Standard parts from cq_warehouse
  from common_parts.cq_warehouse.fasteners.standard_fasteners import get_bolt_m6x20
  
  # Custom parts (build123d)
  from build123d import *
  
  # Custom standard parts (build123d-based)
  from common_parts.custom.wheels.wheel_assembly import get_standard_wheel_15in
  ```

- **Documentation:**
  - See `02_Design/common_parts/README.md` for setup and usage
  - See `02_Design/common_parts/cq_warehouse/README.md` for parts catalog
  - See `02_Design/common_parts/USAGE_EXAMPLES.md` for usage examples

