# V-Model Workflow (Order of Operations)

Follow this strict sequence for any new feature or module:

1.  **Concept Phase:** `@Innovator` proposes 3+1 designs. -> User Approves.
    - **Sub-phase 1.0: Requirements Gathering & Questioning (MANDATORY - NEW)**
      - **Step 1.0.1:** Analyze initial prompt for completeness
        - Check for missing technical specifications
        - Identify unclear user preferences
        - Note ambiguous requirements
        - Detect missing context (use case, environment, etc.)
        - Flag unspecified constraints
      - **Step 1.0.2:** Identify gaps in information
        - Categorize gaps by question category (User Preferences, Technical Constraints, etc.)
        - Prioritize gaps (focus on User Preferences as PRIMARY FOCUS)
      - **Step 1.0.3:** Present organized questions by category
        - Structure questions with clear headers
        - Focus on User Preferences (aesthetics, ergonomics, UX, interaction methods)
        - Include Technical Constraints, Budget/Cost, Manufacturing, Timeline, Environmental/Regulatory, Integration
        - Provide context for why each question matters
        - Offer examples or ranges when appropriate
        - Make questions conversational, not interrogative
      - **Step 1.0.4:** Wait for user responses
        - DO NOT proceed to concept generation until responses received
        - If user provides partial responses, ask follow-up questions for missing categories
      - **Step 1.0.5:** Synthesize responses into comprehensive requirements summary
        - Document all user preferences, constraints, and requirements
        - Create requirements summary for use in concept generation
        - Verify all critical information is captured
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `project_state.json` with current phase and concept generation status
        - See `@Innovator` persona file for detailed memory update steps
    - **Sub-phase 1.1: Concept Generation (UPDATED)**
      - Now proceeds AFTER requirements gathering is complete (Sub-phase 1.0)
      - Uses gathered information to inform concept generation
      - Generate 3+1 concepts (Conservative, Balanced, High-Performance, Wildcard)
      - Create concept skeleton files (`00_Concepts/skeletons/`)
      - Create 2D skeleton sketches (`00_Concepts/skeletons/2d/`)
      - Generate comparison matrix (Pros/Cons/Complexity/Cost/Manufacturing Feasibility/Existing Solutions/Environmental Impact)
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `decision_log.md` with concept selection rationale
        - See `@Innovator` persona file for detailed memory update steps
    - **Sub-phase 1.2:** Create 2D skeleton sketches (`00_Concepts/skeletons/2d/`) - MOVED to Sub-phase 1.1
    - **Sub-phase 1.3:** Create detailed 2D concept sketches (`00_Concepts/sketches/`) - MOVED to Sub-phase 1.4
    - **Sub-phase 1.4: Post-Concept Refinement (MANDATORY - NEW)**
      - **Step 1.4.1:** Present 3+1 concepts with comparison matrix
        - Show all concepts with their comparison matrix
        - Highlight key differences and trade-offs
      - **Step 1.4.2:** Ask targeted refinement questions
        - Which concept direction resonates most? Why?
        - Specific concerns or hesitations?
        - Trade-offs user is willing to make?
        - Additional features or modifications desired?
        - What aspects of each concept are liked/disliked?
        - Interest in hybrid approaches?
      - **Step 1.4.3:** Gather user feedback on concepts
        - Wait for user responses
        - DO NOT proceed to detailed sketches until feedback received
      - **Step 1.4.4:** Refine concepts or generate variations based on feedback
        - Synthesize user responses
        - Refine selected concept(s) based on feedback
        - Generate additional concept variations if needed
        - Present refined concepts for approval
      - **Step 1.4.5:** Finalize concept selection with user approval
        - Get explicit user approval on selected/refined concept
        - Document final concept selection
        - Proceed to detailed sketches only after approval
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `decision_log.md` with refinement decisions
        - See `@Innovator` persona file for detailed memory update steps
    - **Sub-phase 1.5: Detailed Concept Visualization (UPDATED)**
      - Create detailed 2D concept sketches (6 views per concept as PNG files in `00_Concepts/sketches/`)
      - Only proceed after Sub-phase 1.4 (Post-Concept Refinement) is complete
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `coordination_log.md` with handoff to @SeniorEng
        - See `@Innovator` persona file for detailed memory update steps

2.  **Definition Phase:** `@SeniorEng` converts the concept to Markdown Requirements (`REQ-XXX`) and defines the roadmap.
    - **Requirements Completeness Process (MANDATORY):**
      - Systematically review concept document and identify ALL subsystems
      - Create one requirement per major subsystem (do not consolidate)
      - Create interface requirements for each subsystem interface
      - Create cross-cutting requirements (testing, documentation, maintenance, etc.)
      - Verify completeness using Requirements Completeness Checklist
      - Cross-reference concept document to ensure no subsystems missed
    - **Requirements Phase Completion Verification (MANDATORY):**
      - Before declaring phase complete, MUST complete all verification steps
      - Verify subsystem coverage (all subsystems from concept have requirements)
      - Verify interface coverage (all interfaces have requirements)
      - Verify cross-cutting requirements (testing, documentation, maintenance, etc.)
      - Update requirements index and compliance matrix
      - Document any gaps with justification
      - See `cursorrules_modules/01_personas/senior_eng.md` for complete verification process
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `project_state.json` with requirements phase completion
        - Update `decision_log.md` with requirements decisions
        - See `@SeniorEng` persona file for detailed memory update steps

3.  **Design Phase:** `@DesignEng` writes Python scripts to model the physics/geometry and prove feasibility. `@ElectroMechEng` handles electro-mechanical integration if system has electronics.
    - **Sub-phase 3.0: Geometric State Initialization (MANDATORY - NEW)**
      - **Step 3.0.1:** Establish Global Coordinate System (GCS)
        - Define origin (0,0,0) location with clear reference point
        - Document in `02_Design/geometric_state/gcs_definition.md`
        - Define Gravity Vector (usually -Z) and User Facing Vector (usually -Y or +X)
        - Format: "Origin (0,0,0) is located at [specific location]"
      - **Step 3.0.2:** Create Geometric State Ledger
        - Initialize ledger file: `02_Design/geometric_state/state_ledger.md`
        - Set up tracking structure with table format
      - **Step 3.0.3:** Define Orientation Lock
        - Document orientation vectors in GCS definition
        - Prevent incorrect component placement
    - **Sub-phase 3.1:** Create 3D initial skeleton files (`02_Design/skeletons/`)
      - **Skeleton Ownership:** @DesignEng owns master skeleton. @ElectroMechEng provides input and can challenge if needed.
      - **Step 3.1.1:** Create mechanical skeleton files (`@DesignEng`)
        - @DesignEng creates initial mechanical skeleton
        - Includes basic geometry, rough dimensions, key features
      - **Memory Update Checkpoint (MANDATORY):**
        - Update `project_state.json` with skeleton completion status
        - See `@DesignEng` persona file for detailed memory update steps
        - Document in: `02_Design/skeletons/[part]_skeleton.step` and `.py`
        - **If @ElectroMechEng NOT activated:** Proceed to Step 3.1.2 (no electro-mechanical integration needed)
        - **If @ElectroMechEng activated:** Proceed to Step 3.1.2, then Step 3.1.3
      - **Step 3.1.2:** Update Geometric State Ledger with skeleton positions
        - @DesignEng updates ledger with mechanical skeleton positions
        - Document component locations relative to GCS origin
      - **Step 3.1.3:** Electro-Mechanical Integration (MANDATORY if @ElectroMechEng activated - SEQUENTIAL)
        - **CRITICAL:** This step occurs AFTER @DesignEng creates mechanical skeleton
        - **Step 3.1.3.1:** System Definition & Constraints (Space Claim) - `@ElectroMechEng`
          - Review @DesignEng's mechanical skeleton
          - Identify Keep-Out Zones (tall capacitors, user IO ports)
          - Define Black Box volume for PCB/battery
          - Thermal strategy (enclosure as heat sink? ventilation required?)
          - Document in: `02_Design/electro_mechanical/space_claim_[system].md`
          - Provide input to @DesignEng via: `coordination/inputs/input_[ID].md`
        - **Step 3.1.3.2:** Logic & Architecture (Schematic) - `@ElectroMechEng`
          - Interface mapping (PCB mounting to mechanical frame)
          - Cable routing logic (plan service loops and cable paths)
          - Grounding & shielding (conductive plating, grounding points)
          - Document in: `02_Design/electro_mechanical/interface_mapping_[system].md`
          - Provide input to @DesignEng via: `coordination/inputs/input_[ID].md`
        - **Step 3.1.3.3:** Master Skeleton Review & Challenge - `@ElectroMechEng`
          - Review @DesignEng's mechanical skeleton
          - Identify required modifications for electro-mechanical integration:
            - PCB mounting holes (from ECAD DXF/IDF export)
            - Connector centerlines
            - Keep-out zones
            - Thermal management features
          - **If modifications needed:**
            - Create challenge document: `coordination/challenges/challenge_[ID].md`
            - Provide technical justification
            - Request specific modifications
            - **If @DesignEng accepts:** @DesignEng modifies skeleton
            - **If @DesignEng rejects:** Escalate to user for decision
          - **If no modifications needed:** Document approval
          - Document in: `02_Design/electro_mechanical/master_skeleton_[system].md`
        - **Step 3.1.3.4:** Skeleton Finalization - `@DesignEng`
          - Incorporate @ElectroMechEng input (if challenge accepted or input provided)
          - Finalize master skeleton with electro-mechanical features
          - Update Geometric State Ledger with electro-mechanical component positions
          - Document final skeleton in: `02_Design/skeletons/[part]_skeleton_final.step`
    - **Sub-phase 3.2:** Create manufacturing-ready 3D files (`02_Design/parts/`)
      - **Step 3.2.0: Geometric State Update (MANDATORY - NEW)**
        - Update Geometric State Ledger after every part design
        - Verify coordinate system consistency
        - Check orientation lock compliance
      - **CRITICAL:** Follow this logical sequence - each step reviews against overall project plan before proceeding
      - **Step 3.2.1:** Standard Parts Review (MANDATORY)
        - Check `02_Design/common_parts/cq_warehouse/` catalog first
        - Check large-scale library (McMaster-Carr style) via Python API if available
        - Review library index: `02_Design/common_parts/cq_warehouse/README.md`
        - Identify standard components needed (fasteners, bearings, gears, etc.)
        - Document standard parts selection in design notes
        - Use CAD library selection decision tree:
          1. Is this a standard mechanical component? → Check cq_warehouse first
          2. Available in cq_warehouse? → Use common_parts wrappers (do NOT design custom)
          3. Not available? → Check external libraries (McMaster-Carr, GrabCAD, etc.)
          4. Still not available? → Proceed to custom design with build123d
      - **Step 3.2.2:** Functional Design Review (MANDATORY)
        - **Step 3.2.2.1:** Functional Requirements Analysis
          - Analyze what part needs to do (function, purpose, role in system)
          - Identify loads, forces, constraints (static, dynamic, thermal)
          - **Review against overall project plan requirements (MANDATORY)**
          - Verify compliance with all relevant REQ-XXX requirements
          - Document functional requirements in: `02_Design/parts/[part_number]_functional_design.md`
        - **Step 3.2.2.2:** Load Analysis
          - Create force diagrams (Free Body Diagrams - FBD)
          - Calculate expected loads (forces, moments, torques)
          - Identify load paths through part
          - Calculate stress concentrations
          - **Verify against project requirements (MANDATORY)**
          - Document load analysis in functional design document
        - **Step 3.2.2.3:** Interface Design
          - Design connection interfaces (mounting points, mating surfaces)
          - Verify mounting features (holes, threads, clearances)
          - Check alignment requirements
          - Design for assembly (DFA) considerations
          - **Review against assembly requirements (MANDATORY)**
          - Verify interface compatibility with mating parts
          - Document interface design in functional design document
        - **Step 3.2.2.4:** Structural Design
          - Design load paths (direct, efficient paths from load to support)
          - Add reinforcements (gussets, ribs, fillets) based on load analysis
          - Optimize geometry for strength/weight ratio
          - Minimize stress concentrations (fillets ≥2mm radius, chamfers)
          - Verify structural adequacy (hand calculations or FEA)
          - Material selection based on loads and requirements
          - Safety factor selection (typically 2-4 for static, higher for dynamic)
          - Document structural design rationale in functional design document
        - **Step 3.2.2.5:** Project Plan Compliance Review (MANDATORY)
          - Review design against ALL project requirements (REQ-XXX)
          - Verify compliance with overall project plan
          - Check consistency with other parts in project
          - Verify interface compatibility across all related parts
          - Document any deviations with justification
          - Use project plan reviewer: `02_Design/compliance/project_plan_reviewer.py`
        - **Memory Update Checkpoint (MANDATORY):**
          - Update `decision_log.md` with functional design decisions
          - See `@DesignEng` persona file for detailed memory update steps
          - **BLOCKING:** Cannot proceed if major non-compliance
          - Document compliance status in functional design document
      - **Step 3.2.3:** Manufacturing Process Selection (MANDATORY)
        - Evaluate options (CNC, 3D printing, welding, casting, sheet metal)
        - Use process selection matrix: `02_Design/manufacturing/process_selection_matrix.md`
        - Use automated process selector: `02_Design/manufacturing/manufacturing_process_selector.py`
        - Consider: quantity, cost, lead time, capabilities, DFAM opportunities
        - Select optimal process based on requirements
        - Document selection rationale in: `02_Design/manufacturing/process_selection_[part].md`
        - **Review against project plan constraints (MANDATORY)**
        - Verify process selection aligns with project budget, timeline, and capabilities
        - **Memory Update Checkpoint (MANDATORY):**
          - Update `decision_log.md` with process selection rationale
          - See `@DesignEng` persona file for detailed memory update steps
      - **Step 3.2.4:** Process-Specific Design (MANDATORY)
        - **If CNC Machining:**
          - Apply CNC constraints (tool access, undercuts, internal radii)
          - Optimize for setup minimization (design for single setup when possible)
          - Design for efficient tool paths (avoid sharp corners, optimize feeds/speeds)
          - Minimum internal corner radius = tool radius (typically 0.5-3mm)
          - Thread milling vs. tapping selection (M12+ = thread mill, M6- = tap)
        - **If 3D Printing:**
          - Apply DFAM principles (see `02_Design/manufacturing/process_specific_design_guidelines.md`)
          - Optimize build orientation (minimize supports, maximize strength)
          - Minimize supports (45° overhang rule, self-supporting features)
          - Consider topology optimization (remove material where loads are low)
          - Design for layer orientation (strength anisotropy)
          - Minimum feature sizes (walls ≥0.5mm FDM, ≥0.3mm SLA, ≥0.4mm SLS)
        - **If Welding:**
          - Design weld joints (butt, fillet, lap, corner, edge)
          - Add weld symbols (AWS D1.1, D1.2 standards)
          - Consider distortion control (tack welding, sequencing, fixturing)
          - Design for weld accessibility (minimum 150mm clearance for torch)
          - Weld size calculations (leg length, throat thickness)
        - **If Sheet Metal:**
          - Apply bend radii and K-factors
          - Design for forming limits
          - Consider tooling constraints
        - See `02_Design/manufacturing/process_specific_design_guidelines.md` for detailed guidelines
      - **Step 3.2.5:** Design Custom Parts (if not standard)
        - Design using build123d
        - Apply process-specific constraints from Step 3.2.4
        - Include functional design elements from Step 3.2.2 (gussets, ribs, fillets, reinforcements)
        - Include tolerances, GD&T, surface finish, threads, holes
        - Generate manufacturing-ready STEP files with PMI
        - **Memory Update Checkpoint (MANDATORY if interfaces change):**
          - Update `interface_registry.md` if interfaces change
          - See `@DesignEng` persona file for detailed memory update steps
      - **Step 3.2.6:** Final Project Plan Review (MANDATORY)
        - Comprehensive review against overall project plan
        - Verify all requirements met (REQ-XXX)
        - Check consistency across all parts
        - Verify interface compatibility
        - Use project plan reviewer: `02_Design/compliance/project_plan_reviewer.py`
        - Document final compliance status
        - **BLOCKING:** Cannot proceed to assembly if non-compliant
      - **Step 3.2.7:** Generate manufacturing-ready STEP files
        - Export STEP files with PMI (Product Manufacturing Information)
        - Generate technical drawings (DXF, DWG, PDF)
        - Create manufacturing notes
        - Include functional design documentation
      - **Step 3.2.8: Interference Check (MANDATORY - NEW)**
        - Calculate bounds for all components
        - Run interference math check: `Clearance = (Inner_Dim_Housing) - (Outer_Dim_Component)`
        - If `Clearance < 0`, STOP and flag INTERFERENCE ERROR
        - Document results in `02_Design/geometric_state/interference_checks.md`
        - Use automated script: `02_Design/geometric_state/check_interference.py`
        - **BLOCKING:** Cannot proceed to assembly if interference detected
        - **Memory Update Checkpoint (MANDATORY):**
          - Update `state_ledger.md` with geometric state
          - See `@DesignEng` persona file for detailed memory update steps
    - **Sub-phase 3.3:** Create assembly (`02_Design/assemblies/`)
      - **Assembly Ownership:** @DesignEng owns assembly. @ElectroMechEng provides input and can modify electro-mechanical aspects if needed.
      - **Assembly Creation Sequence:**
        1. @DesignEng creates base mechanical assembly
        2. @ElectroMechEng reviews and provides input (if activated)
        3. @ElectroMechEng can modify electro-mechanical aspects
        4. Conflicts escalate to user for approval
        5. @DesignEng finalizes assembly
      - **Step 3.3.1:** Load custom manufacturing-ready parts (`@DesignEng`)
        - Import STEP files from `02_Design/parts/`
        - Position parts according to skeleton layout
        - Create base mechanical assembly
      - **Step 3.3.2:** Import standard parts from common_parts library (MANDATORY) (`@DesignEng`)
        - Use wrapper functions from common_parts:
          ```python
          from common_parts.cq_warehouse.fasteners import get_bolt_m12x40
          from common_parts.cq_warehouse.bearings import get_bearing_2inch
          ```
        - Import all required standard components (fasteners, bearings, etc.)
        - Position standard parts in assembly
        - Assign proper part numbers (format: `[PROJECT]-COMMON-[CATEGORY]-[SPEC]-[REVISION]`)
      - **Step 3.3.3:** Import purchased components with detailed representation (MANDATORY)
        - **CRITICAL:** Even if components are purchased (not custom-designed), they MUST be represented in detail in the assembly
        - Create detailed 3D models of purchased components (axles, wheels, motors, pumps, generators, etc.)
        - Use accurate dimensions from supplier datasheets or standard specifications
        - Include all mounting interfaces, connection points, and critical dimensions
        - Purpose: Enable clearance/interference checking, interface verification, and complete assembly visualization
        - Store purchased component models in `02_Design/common_parts/custom/` or `02_Design/assemblies/purchased_components/`
        - File naming: `[PROJECT]-[COMPONENT-TYPE]-[SPEC]-[REVISION].step`
        - Example: `DCS-TRLR-AXLE-STD-2500KG-A001.step` for standard 2500kg axle
        - Include metadata: Supplier part number, specifications, source, purchase notes
        - **DO NOT use placeholders** - all purchased components must have detailed 3D representation
      - **Step 3.3.4:** Assembly Completeness Check (MANDATORY)
        - Verify all subsystems included:
          - [ ] Structural subsystem (frame, cross members, brackets)
          - [ ] Mobility subsystem (wheels, axles, suspension, bearings) - if applicable
          - [ ] Coupling subsystem (hitch, safety chains) - if applicable
          - [ ] Braking subsystem - if applicable
          - [ ] Electrical subsystem (lights, wiring) - if applicable
        - Verify standard components:
          - [ ] All fasteners specified using common_parts wrappers
          - [ ] All bearings specified using common_parts wrappers
          - [ ] Standard components checked against cq_warehouse library
          - [ ] Part numbers assigned to all standard components
        - Verify purchased components (MANDATORY):
          - [ ] All purchased components have detailed 3D models (NOT placeholders)
          - [ ] All purchased components positioned correctly in assembly
          - [ ] All interfaces and mounting points verified
          - [ ] Clearance/interference checks completed for purchased components
          - [ ] Supplier part numbers and specifications documented
          - [ ] Critical dimensions from purchased components included in assembly
        - Document in: `02_Design/assemblies/[assembly]_completeness_check.md`
      - **Step 3.3.4:** Generate complete BOM (MANDATORY)
        - Include all custom parts from Sub-phase 3.2
        - Include all standard parts from common_parts library
        - Verify quantities match assembly
        - Include part numbers, materials, suppliers
        - Export to CSV and Markdown formats
      - **Step 3.3.5:** Export assembly STEP file
        - Include all custom parts, standard parts, AND purchased components
        - Verify assembly integrity (all components properly positioned)
        - Verify clearance/interference for all interfaces (including purchased components)
        - Generate assembly documentation
      - **Step 3.3.6: Assembly Geometric State Verification (MANDATORY - NEW)**
        - Verify all components positioned relative to GCS
        - Update Geometric State Ledger with assembly positions
        - Run assembly-level interference check
        - Verify orientation lock compliance
        - Document in: `02_Design/geometric_state/assembly_state_[assembly].md`
      - **Step 3.3.7: Electro-Mechanical Assembly Review (MANDATORY if @ElectroMechEng activated)**
        - **Step 3.3.7.1:** @ElectroMechEng reviews @DesignEng's assembly
          - Review base mechanical assembly created by @DesignEng
          - Validate PCB mounting interfaces
          - Verify connector alignment
          - Check cable routing clearances
          - Validate thermal management (heat paths, ventilation)
          - Check keep-out zones
        - **Step 3.3.7.2:** @ElectroMechEng provides input or modifications
          - **If modifications needed:**
            - Create challenge document: `coordination/challenges/challenge_[ID].md`
            - Request specific modifications to assembly
            - **If @DesignEng accepts:** @DesignEng modifies assembly
            - **If @DesignEng rejects:** Escalate to user for decision
          - **If no modifications needed:** Document approval
        - **Step 3.3.7.3:** @DesignEng finalizes assembly
          - Incorporate @ElectroMechEng input (if challenge accepted)
          - Finalize assembly with all electro-mechanical aspects
          - Document in: `02_Design/electro_mechanical/assembly_validation_[system].md`

4.  **Implementation Phase:** `@Builder` writes the functional software/firmware.
    - **Memory Update Checkpoint (MANDATORY):**
      - Update `project_state.json` with implementation status
      - Update `decision_log.md` after code review
      - Update `change_log.md` if design changes required
      - See `@Builder` persona file for detailed memory update steps

5.  **Verification Phase:** `@Skeptic` writes test scripts against the Requirements.
    - **Memory Update Checkpoint (MANDATORY):**
      - Update `validation_log.md` with test plans, test results, performance benchmarks, FAI, production validation
      - Update `decision_log.md` after FMEA
      - See `@Skeptic` persona file for detailed memory update steps

6.  **Pre-Production Review Phase:** `@SeniorEng`, `@DesignEng`, and `@Skeptic` conduct comprehensive review before production release.
    - **Sub-phase 6.1:** DFM/DFA review (`@DesignEng`)
    - **Sub-phase 6.2:** Cost analysis (`@DesignEng`)
    - **Sub-phase 6.3:** Production validation planning (`@Skeptic`)
    - **Sub-phase 6.4:** Compliance verification (`@SeniorEng`)
    - **Sub-phase 6.5:** Final review and approval (`@SeniorEng`)

7.  **Production Release Phase:** `@SeniorEng` acts as gatekeeper for production release.
    - **Sub-phase 7.1:** Release package creation (all documentation, drawings, BOM)
    - **Sub-phase 7.2:** Production release gate checklist review
    - **Sub-phase 7.3:** Sign-off and approval process
    - **Sub-phase 7.4:** Production version control (PROD-v1.0)
    - **Sub-phase 7.5:** Release documentation package

8.  **Post-Production Phase:** `@Skeptic` monitors production and handles issues.
    - **Memory Update Checkpoint (MANDATORY):**
      - Update `validation_log.md` with production monitoring results
      - See `@Skeptic` persona file for detailed memory update steps
    - **Sub-phase 8.1:** Production monitoring and quality control
    - **Sub-phase 8.2:** Issue tracking and resolution
    - **Sub-phase 8.3:** Continuous improvement process
    - **Sub-phase 8.4:** Field failure analysis (if applicable)

9.  **Manufacturing Feedback Loop Phase:** `@DesignEng` and `@SeniorEng` collect and analyze manufacturing feedback.
    - **Sub-phase 9.1:** Feedback collection from suppliers, internal, and customers
    - **Sub-phase 9.2:** Feedback analysis and trend identification
    - **Sub-phase 9.3:** Design iteration based on feedback
      - **If design changes required:**
        - Follow ECO process (`01_Requirements/ECO_process.md`)
        - Return to Phase 3 (Design Phase) for design updates
        - Update affected parts in Sub-phase 3.2
        - Update assemblies in Sub-phase 3.3
        - Re-run Assembly Completeness Check
      - **If new standard parts identified:**
        - Add to `02_Design/common_parts/` library
        - Update common_parts catalog
        - Document in library index
    - **Sub-phase 9.4:** ECO process for production changes (if required)
    - **Sub-phase 9.5:** Continuous improvement implementation
    - **Tools:**
      - Manufacturing issue tracker: `02_Design/manufacturing/manufacturing_issue_tracker.py`
      - Feedback database: `02_Design/manufacturing/manufacturing_feedback_db.py`
      - Supplier communication templates: `02_Design/production/supplier_communication_templates.md`
      - See: `02_Design/manufacturing/design_iteration_workflow.md`

10. **Logging:** AUTOMATIC. Every session must end with a log entry in `logs/session_log.md`.

## Design Phase Checkpoints

### Checkpoint: Before Sub-phase 3.3 (Assembly Creation)
Before proceeding to assembly creation, verify:
- [ ] Common parts library reviewed (`02_Design/common_parts/cq_warehouse/`)
- [ ] Standard parts identified and documented
- [ ] Custom parts designed (only parts NOT in common_parts)
- [ ] CAD library selection verified (build123d vs cq_warehouse)
- [ ] All manufacturing-ready parts exported to STEP
- [ ] Technical drawings generated for custom parts

## Skeleton Method Workflow

The skeleton method ensures progressive refinement from rough concepts to manufacturing-ready designs:

1. **Concept Skeleton** (`@Innovator`)
   - Create `00_Concepts/skeletons/[concept]_skeleton.md`
   - Include: topology, rough dimensions, part count, placeholder part numbers
   - Create 2D skeleton sketches (`00_Concepts/skeletons/2d/`)

2. **2D Detailed Sketches** (`@Innovator`)
   - Refine skeleton sketches into detailed 2D concept sketches
   - Create `00_Concepts/sketches/[concept]_[view].png`

3. **3D Initial Skeleton** (`@DesignEng`)
   - Create `02_Design/skeletons/[part]_skeleton.step`
   - Include: basic geometry, rough dimensions, part number, basic material
   - No tolerances, no GD&T, no manufacturing details

4. **3D Manufacturing-Ready** (`@DesignEng`)
   - Check common_parts library first for standard components
   - Refine skeleton into `02_Design/parts/[part].step` (only for custom parts)
   - Include: detailed geometry, tolerances, GD&T, surface finish, threads, holes
   - Generate technical drawings (DXF, DWG, PDF)

5. **Assembly** (`@DesignEng` / `@Builder`)
   - Load custom manufacturing-ready parts
   - Import standard parts from common_parts library
   - Assembly Completeness Check (MANDATORY)
   - Create final assembly with all parts (custom + standard)
   - Generate assembly documentation and complete BOM (including standard parts)

## Workflow Dependencies

- **@Innovator** → Creates concept skeletons → detailed concepts that @SeniorEng converts to requirements
- **@SeniorEng** → Defines requirements that @DesignEng must satisfy → Acts as production release gatekeeper
- **@DesignEng** → Creates 3D skeletons → Checks common_parts library → Designs custom parts → Creates assemblies with standard parts → Conducts DFM/DFA review → Assembly Completeness Check → @Builder implements and @Skeptic tests
- **@Builder** → Implements code that @Skeptic verifies
- **@Skeptic** → Validates against requirements from @SeniorEng → Production validation → Post-production monitoring → Feedback collection
- **Feedback Loop** → If design changes needed → ECO process → Return to Phase 3 (Design Phase)

## Production Release Gate Process

Before any design can be released for production, it MUST pass through the Production Release Gate:

1. **Pre-Production Review** - All documentation, DFM/DFA, cost analysis complete
2. **Production Release Gate Checklist** - All items verified and signed off
3. **Release Documentation Package** - Complete package ready for supplier/manufacturer
4. **Version Control** - Production version assigned (PROD-v1.0)
5. **Sign-Off** - @SeniorEng approval required

**No design proceeds to production without passing the Production Release Gate.**

## Change Management After Production Release

Once a design is released for production, changes follow the Engineering Change Order (ECO) process:

- **Minor Changes** (A001 → A002): Clarifications, typos, non-functional changes
- **Major Changes** (A001 → B001): Functional changes, design modifications
- **ECO Required**: All changes must go through impact analysis and approval
- **Change Tracking**: All changes documented and tracked

See `01_Requirements/ECO_process.md` for detailed process.

## Important Notes

- Do NOT skip phases. Always follow the strict sequence.
- **Skeleton files are MANDATORY** - they establish structure before detailed design
- **Production Release Gate is MANDATORY** - no production without gate approval
- Each phase depends on the previous one's completion.
- Ensure traceability between requirements, design, implementation, and tests.
- Skeleton files include minimal metadata: part numbers, basic dimensions, material suggestions.
- Changes after production release require ECO process.

