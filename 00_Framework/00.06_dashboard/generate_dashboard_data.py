"""
Generate Dashboard Data for PROJECT_DASHBOARD.html
Scans project files and generates JSON data for dashboard display

Run this script to update dashboard_data.json which the dashboard reads.
"""

import os
import json
import glob
import re
from datetime import datetime
from pathlib import Path

def calculate_overall_progress(requirements, design, production, implementation, verification):
    """Calculate overall project progress based on V-Model phases"""
    weights = {
        "concept": 0.10,      # Phase 1: Concept (10%)
        "requirements": 0.15, # Phase 2: Requirements (15%)
        "design": 0.30,        # Phase 3: Design (30%)
        "implementation": 0.20, # Phase 4: Implementation (20%)
        "verification": 0.15,  # Phase 5: Verification (15%)
        "production": 0.10    # Phase 6-8: Production (10%)
    }
    
    # Calculate phase progress
    req_progress = (requirements["approved"] / max(requirements["total"], 1)) * 100 if requirements["total"] > 0 else 0
    
    # Design progress: average of key design milestones
    design_items = [
        design.get("conceptSketches", "pending"),
        design.get("skeletons", "pending"),
        design.get("manufacturing", "pending"),
        design.get("assemblies", "pending"),
        design.get("drawings", "pending"),
        design.get("dfm", "pending"),
        design.get("dfa", "pending")
    ]
    design_complete = sum(1 for item in design_items if item == "complete")
    design_in_progress = sum(1 for item in design_items if item == "in-progress")
    design_progress = ((design_complete * 100 + design_in_progress * 50) / max(len(design_items), 1))
    
    # Production progress
    prod_items = [
        production.get("preReview", "pending"),
        production.get("releaseGate", "pending"),
        production.get("releasePackage", "pending")
    ]
    prod_complete = sum(1 for item in prod_items if item == "complete")
    prod_in_progress = sum(1 for item in prod_items if item == "in-progress")
    prod_progress = ((prod_complete * 100 + prod_in_progress * 50) / max(len(prod_items), 1))
    
    # Implementation and verification (simplified for now)
    impl_progress = 0  # Will be calculated if implementation directory exists
    verif_progress = 0  # Will be calculated if verification directory exists
    
    # Overall weighted progress
    overall = (
        weights["requirements"] * req_progress +
        weights["design"] * design_progress +
        weights["production"] * prod_progress +
        weights["implementation"] * impl_progress +
        weights["verification"] * verif_progress
    ) / (weights["requirements"] + weights["design"] + weights["production"] + 
         weights["implementation"] + weights["verification"])
    
    return round(overall, 1)

def scan_implementation_status(project_root):
    """Scan implementation phase status"""
    # Check new structure first, fall back to old structure
    impl_dir = project_root / "Project_Specific" / "01_Project" / "01.04_implementation"
    if not impl_dir.exists():
        impl_dir = project_root / "03_Implementation"
    
    if not impl_dir.exists():
        return {
            "status": "pending",
            "codeFiles": 0,
            "reviews": 0,
            "progress": 0
        }
    
    code_files = list(impl_dir.rglob("*.py"))
    review_files = list(impl_dir.rglob("*review*.md")) + list(impl_dir.rglob("*REVIEW*.md"))
    
    # Estimate progress based on file count (heuristic)
    progress = min(100, len(code_files) * 5) if code_files else 0
    
    return {
        "status": "in-progress" if code_files else "pending",
        "codeFiles": len(code_files),
        "reviews": len(review_files),
        "progress": min(progress, 100)
    }

def scan_verification_status(project_root):
    """Scan verification phase status"""
    # Check for new structure first
    verif_dir = project_root / "Project_Specific" / "01_Project" / "01.05_verification"
    if not verif_dir.exists():
        verif_dir = project_root / "04_Verification"
    
    if not verif_dir.exists():
        return {
            "status": "pending",
            "testFiles": 0,
            "coverage": 0,
            "progress": 0
        }
    
    test_files = list(verif_dir.rglob("test_*.py")) + list(verif_dir.rglob("*test*.py"))
    coverage_files = list(verif_dir.rglob("*coverage*.md")) + list(verif_dir.rglob("*coverage*.html"))
    
    # Estimate progress
    progress = min(100, len(test_files) * 10) if test_files else 0
    
    return {
        "status": "in-progress" if test_files else "pending",
        "testFiles": len(test_files),
        "coverage": len(coverage_files),
        "progress": min(progress, 100)
    }

def scan_memory_system(project_root):
    """Scan memory system files and return status"""
    memory_system = {
        "coordination": {"status": "active", "event_count": 0, "last_update": None},
        "changes": {"status": "active", "change_count": 0, "last_update": None},
        "interfaces": {"status": "active", "interface_count": 0, "last_update": None},
        "validation": {"status": "active", "validation_count": 0, "last_update": None},
        "project_memory": {"status": "active", "decision_count": 0, "last_update": None}
    }
    
    # Check for new structure (Project_Specific) or old structure
    project_specific = project_root / "Project_Specific" / "01_Project"
    framework_memory = project_root / "00_Framework" / "00.05_memory_system"
    
    # Try new structure first
    if project_specific.exists():
        # Coordination log
        coord_log = framework_memory / "00.05.01_coordination" / "coordination_log.md"
        if coord_log.exists():
            try:
                with open(coord_log, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Count table rows (approximate count)
                    event_count = content.count('|') // 5  # Rough estimate
                    memory_system["coordination"]["event_count"] = max(0, event_count - 1)  # Subtract header
                    stat = coord_log.stat()
                    memory_system["coordination"]["last_update"] = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
        
        # Change log
        change_log = framework_memory / "00.05.02_changes" / "change_log.md"
        if change_log.exists():
            try:
                with open(change_log, 'r', encoding='utf-8') as f:
                    content = f.read()
                    change_count = content.count('|') // 7  # Rough estimate
                    memory_system["changes"]["change_count"] = max(0, change_count - 1)
                    stat = change_log.stat()
                    memory_system["changes"]["last_update"] = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
        
        # Interface registry
        interface_reg = framework_memory / "00.05.03_interfaces" / "interface_registry.md"
        if interface_reg.exists():
            try:
                with open(interface_reg, 'r', encoding='utf-8') as f:
                    content = f.read()
                    interface_count = content.count('|') // 5  # Rough estimate
                    memory_system["interfaces"]["interface_count"] = max(0, interface_count - 1)
                    stat = interface_reg.stat()
                    memory_system["interfaces"]["last_update"] = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
        
        # Validation log
        validation_log = framework_memory / "00.05.04_validation" / "validation_log.md"
        if validation_log.exists():
            try:
                with open(validation_log, 'r', encoding='utf-8') as f:
                    content = f.read()
                    validation_count = content.count('|') // 7  # Rough estimate
                    memory_system["validation"]["validation_count"] = max(0, validation_count - 1)
                    stat = validation_log.stat()
                    memory_system["validation"]["last_update"] = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
        
        # Project memory - decision log
        decision_log = framework_memory / "00.05.05_project_memory" / "decisions" / "decision_log.md"
        if decision_log.exists():
            try:
                with open(decision_log, 'r', encoding='utf-8') as f:
                    content = f.read()
                    decision_count = content.count('|') // 6  # Rough estimate
                    memory_system["project_memory"]["decision_count"] = max(0, decision_count - 1)
                    stat = decision_log.stat()
                    memory_system["project_memory"]["last_update"] = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            except:
                pass
    
    return memory_system

def scan_project():
    """Scan project and generate dashboard data"""
    
    project_root = Path(__file__).parent.parent.parent  # Go up to project root
    
    # Scan all phases
    requirements = scan_requirements(project_root)
    design = scan_design_status(project_root)
    production = scan_production_status(project_root)
    implementation = scan_implementation_status(project_root)
    verification = scan_verification_status(project_root)
    current_phase = determine_current_phase(project_root)
    memory_system = scan_memory_system(project_root)
    
    # Calculate overall progress
    overall_progress = calculate_overall_progress(requirements, design, production, implementation, verification)
    
    dashboard_data = {
        "metadata": {
            "projectName": "Drone Cleaning System Trailer",
            "projectConcept": "Balanced Design",
            "projectDescription": "DJI M350 RTK drone-based facade cleaning system with customized trailer-mounted ground station (1000L square water tank, high-pressure pump, generator, motorized hose reel, articulated guide arm)",
            "lastUpdated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "overallProgress": overall_progress
        },
        "currentPhase": current_phase,
        "vModelPhases": {
            "phase1_concept": {
                "name": "Concept Phase",
                "concepts_dir": project_root / "Project_Specific" / "01_Project" / "01.01_concepts",
                "old_concepts_dir": project_root / "00_Concepts",
                "status": "complete" if ((project_root / "Project_Specific" / "01_Project" / "01.01_concepts").exists() and list((project_root / "Project_Specific" / "01_Project" / "01.01_concepts").glob("*.md"))) or ((project_root / "00_Concepts").exists() and list((project_root / "00_Concepts").glob("*.md"))) else "pending",
                "progress": 100 if (((project_root / "Project_Specific" / "01_Project" / "01.01_concepts" / "sketches").exists() and len(list((project_root / "Project_Specific" / "01_Project" / "01.01_concepts" / "sketches").glob("*.png"))) >= 6) or ((project_root / "00_Concepts" / "sketches").exists() and len(list((project_root / "00_Concepts" / "sketches").glob("*.png"))) >= 6)) else 50
            },
            "phase2_requirements": {
                "name": "Requirements Phase",
                "status": "complete" if requirements["approved"] == requirements["total"] and requirements["total"] > 0 else "in-progress" if requirements["total"] > 0 else "pending",
                "progress": (requirements["approved"] / max(requirements["total"], 1)) * 100 if requirements["total"] > 0 else 0
            },
            "phase3_design": {
                "name": "Design Phase",
                "status": "complete" if design.get("manufacturing") == "complete" and design.get("assemblies") == "complete" else ("in-progress" if current_phase["number"] == 3 or design.get("skeletons") == "complete" else "pending"),
                "progress": current_phase["progress"] if current_phase["number"] == 3 else (100 if design.get("manufacturing") == "complete" and design.get("assemblies") == "complete" else 0)
            },
            "phase4_implementation": {
                "name": "Implementation Phase",
                "status": implementation["status"],
                "progress": implementation["progress"]
            },
            "phase5_verification": {
                "name": "Verification Phase",
                "status": verification["status"],
                "progress": verification["progress"]
            },
            "phase6_production": {
                "name": "Production Phase",
                "status": "complete" if production.get("version") != "Not Assigned" else "in-progress" if production.get("releaseGate") == "complete" else "pending",
                "progress": 100 if production.get("version") != "Not Assigned" else 50 if production.get("releaseGate") == "complete" else 0
            }
        },
        "requirements": requirements,
        "design": design,
        "implementation": implementation,
        "verification": verification,
        "production": production,
        "changeManagement": scan_change_management(project_root),
        "compliance": scan_compliance(project_root),
        "manufacturingFeedback": scan_manufacturing_feedback(project_root),
        "recentActivity": scan_recent_activity(project_root),
        "timeline": scan_timeline_data(project_root),
        "memory_system": memory_system
    }
    
    return dashboard_data

def determine_current_phase(project_root):
    """Determine current workflow phase"""
    
    # PRIORITY: Check design phase first if manufacturing-ready parts exist (most concrete indicator)
    # Check new structure first, fall back to old structure
    parts_dir = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "01.03.01_parts"
    if not parts_dir.exists():
        parts_dir = project_root / "02_Design" / "parts"
    if parts_dir.exists():
        # Check for STEP files first (most complete)
        step_files = list(parts_dir.glob("*.step"))
        if step_files:
            return {
                "number": 3,
                "name": "Design Phase",
                "subPhase": "Manufacturing-Ready Files (STEP Exported)",
                "progress": 40
            }
        # Check for manufacturing-ready Python scripts (Sub-Phase 3.2)
        part_scripts = [f for f in parts_dir.glob("*_A001.py") if f.stem not in ["export_all_parts_step", "generate_all_drawings", "generate_BOM", "validate_all_step_files"]]
        if part_scripts and len(part_scripts) >= 5:  # At least 5 manufacturing-ready parts
            return {
                "number": 3,
                "name": "Design Phase",
                "subPhase": "Sub-Phase 3.2: Manufacturing-Ready Files",
                "progress": 35
            }
    
    # Check for production release (only if design is complete)
    # Check new structure first, fall back to old structure
    release_log = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "production" / "release_log.md"
    if not release_log.exists():
        release_log = project_root / "02_Design" / "production" / "release_log.md"
    if release_log.exists():
        # Check if release approved
        try:
            with open(release_log, 'r', encoding='utf-8') as f:
                content = f.read()
                if "PROD-v" in content and "Approved" in content:
                    return {
                        "number": 8,
                        "name": "Post-Production Phase",
                        "subPhase": "Production Released",
                        "progress": 89
                    }
        except:
            pass
        return {
            "number": 7,
            "name": "Production Release Phase",
            "subPhase": "Release Package Creation",
            "progress": 78
        }
    
    release_gate = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "production" / "release_gate_checklist.md"
    if not release_gate.exists():
        release_gate = project_root / "02_Design" / "production" / "release_gate_checklist.md"
    if release_gate.exists():
        return {
            "number": 6,
            "name": "Pre-Production Review Phase",
            "subPhase": "Release Gate Preparation",
            "progress": 67
        }
    
    # Check for verification phase (only if design is substantially complete)
    # Check new structure first, fall back to old structure
    verif_dir = project_root / "Project_Specific" / "01_Project" / "01.05_verification"
    if not verif_dir.exists():
        verif_dir = project_root / "04_Verification"
    if verif_dir.exists() and list(verif_dir.glob("**/*.md")):
        # Only consider verification phase if we have actual test results, not just templates
        verification_production = verif_dir / "production"
        if verification_production.exists() and list(verification_production.glob("*.md")):
            # Check if these are actual production monitoring files (not just templates)
            # For now, only show post-production if release is approved
            pass  # Skip - handled by release_log check above
        else:
            return {
                "number": 5,
                "name": "Verification Phase",
                "subPhase": "Test Development",
                "progress": 56
            }
    
    impl_dir = project_root / "Project_Specific" / "01_Project" / "01.04_implementation"
    if not impl_dir.exists():
        impl_dir = project_root / "03_Implementation"
    if impl_dir.exists() and list(impl_dir.glob("**/*.py")):
        return {
            "number": 4,
            "name": "Implementation Phase",
            "subPhase": "Code Development",
            "progress": 44
        }
    
    # Check for design skeletons (STEP files or Python scripts)
    # Check new structure first, fall back to old structure
    skeletons_dir = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "01.03.03_skeletons"
    if not skeletons_dir.exists():
        skeletons_dir = project_root / "02_Design" / "skeletons"
    if skeletons_dir.exists():
        skeleton_step_files = list(skeletons_dir.glob("*.step"))
        if skeleton_step_files:
            return {
                "number": 3,
                "name": "Design Phase",
                "subPhase": "3D Skeleton Creation (STEP)",
                "progress": 30
            }
        skeleton_scripts = list(skeletons_dir.glob("*.py"))
        if skeleton_scripts:
            return {
                "number": 3,
                "name": "Design Phase",
                "subPhase": "3D Skeleton Creation",
                "progress": 28
            }
    
    req_dir = project_root / "Project_Specific" / "01_Project" / "01.02_requirements"
    if not req_dir.exists():
        req_dir = project_root / "01_Requirements"
    if req_dir.exists() and list(req_dir.glob("REQ-*.md")):
        return {
            "number": 2,
            "name": "Definition Phase",
            "subPhase": "Requirements Creation",
            "progress": 22
        }
    
    # Check for concept phase (only if no more advanced phases found)
    # Check new structure first, fall back to old structure
    concepts_dir = project_root / "Project_Specific" / "01_Project" / "01.01_concepts"
    if not concepts_dir.exists():
        concepts_dir = project_root / "00_Concepts"
    if (concepts_dir / "sketches").exists():
        sketch_files = list((concepts_dir / "sketches").glob("*.png"))
        if sketch_files and len(sketch_files) >= 6:  # Technical sketches complete
            return {
                "number": 1,
                "name": "Concept Phase",
                "subPhase": "Technical Sketches Complete",
                "progress": 25
            }
    
    # Check for concept skeletons
    if (concepts_dir / "skeletons").exists():
        skeleton_files = list((concepts_dir / "skeletons").glob("*.md"))
        if skeleton_files:
            return {
                "number": 1,
                "name": "Concept Phase",
                "subPhase": "Concept Skeleton Created",
                "progress": 15
            }
    
    if concepts_dir.exists():
        return {
            "number": 1,
            "name": "Concept Phase",
            "subPhase": "Concept Development",
            "progress": 11
        }
    
    return {
        "number": 0,
        "name": "Not Started",
        "subPhase": "-",
        "progress": 0
    }

def scan_requirements(project_root):
    """Scan requirements directory"""
    # Check new structure first, fall back to old structure
    req_dir = project_root / "Project_Specific" / "01_Project" / "01.02_requirements"
    if not req_dir.exists():
        req_dir = project_root / "01_Requirements"
    
    if not req_dir.exists():
        return {
            "total": 0,
            "approved": 0,
            "inProgress": 0,
            "pending": 0,
            "list": []
        }
    
    req_files = list(req_dir.glob("REQ-*.md"))
    
    total = len(req_files)
    approved = 0
    in_progress = 0
    pending = 0
    
    req_list = []
    for req_file in req_files:
        try:
            with open(req_file, 'r', encoding='utf-8') as f:
                content = f.read()
                req_id = req_file.stem
                
                if 'Status: Approved' in content or 'status: Approved' in content:
                    approved += 1
                    status = "approved"
                elif 'Status: In Progress' in content or 'status: In Progress' in content:
                    in_progress += 1
                    status = "in-progress"
                else:
                    pending += 1
                    status = "pending"
                
                # Extract title
                title_match = re.search(r'Title:\s*(.+)', content)
                title = title_match.group(1).strip() if title_match else req_id
                
                req_list.append({
                    "id": req_id,
                    "title": title[:50],  # Truncate long titles
                    "status": status
                })
        except Exception as e:
            pending += 1
            req_list.append({
                "id": req_file.stem,
                "title": "Error reading",
                "status": "pending"
            })
    
    return {
        "total": total,
        "approved": approved,
        "inProgress": in_progress,
        "pending": pending,
        "list": req_list[:10]  # Latest 10
    }

def scan_design_status(project_root):
    """Scan design status"""
    # Check new structure first, fall back to old structure
    design_dir = project_root / "Project_Specific" / "01_Project" / "01.03_design"
    if not design_dir.exists():
        design_dir = project_root / "02_Design"
    
    # Check for concept sketches (01.01_concepts/sketches or 00_Concepts/sketches)
    concepts_dir = project_root / "Project_Specific" / "01_Project" / "01.01_concepts"
    if not concepts_dir.exists():
        concepts_dir = project_root / "00_Concepts"
    concept_sketches_status = "pending"
    if (concepts_dir / "sketches").exists():
        sketch_files = list((concepts_dir / "sketches").glob("*.png"))
        if sketch_files and len(sketch_files) >= 6:  # Should have 6 technical views
            concept_sketches_status = "complete"
        elif sketch_files:
            concept_sketches_status = "in-progress"
    
    skeletons_status = "pending"
    skeletons_subdir = design_dir / "01.03.03_skeletons" if "01.03_design" in str(design_dir) else design_dir / "skeletons"
    if skeletons_subdir.exists():
        skeleton_files = list(skeletons_subdir.glob("*.step"))
        if skeleton_files:
            skeletons_status = "complete"
        elif list(skeletons_subdir.glob("*.py")):
            skeletons_status = "in-progress"
    
    manufacturing_status = "pending"
    parts_dir = design_dir / "01.03.01_parts" if "01.03_design" in str(design_dir) else design_dir / "parts"
    if parts_dir.exists():
        part_step_files = list(parts_dir.glob("*.step"))
        if part_step_files:
            manufacturing_status = "complete"
        else:
            # Check for manufacturing-ready Python scripts (Sub-Phase 3.2)
            part_scripts = [f for f in parts_dir.glob("*_A001.py") if f.stem not in ["export_all_parts_step", "generate_all_drawings", "generate_BOM", "validate_all_step_files"]]
            if part_scripts and len(part_scripts) >= 5:  # At least 5 manufacturing-ready parts
                manufacturing_status = "in-progress"  # Scripts ready, STEP export pending
    
    assemblies_status = "pending"
    assemblies_dir = design_dir / "01.03.02_assemblies" if "01.03_design" in str(design_dir) else design_dir / "assemblies"
    if assemblies_dir.exists():
        assembly_step_files = list(assemblies_dir.glob("*.step"))
        if assembly_step_files:
            assemblies_status = "complete"
        else:
            # Check for assembly Python scripts
            assembly_scripts = list(assemblies_dir.glob("*.py"))
            if assembly_scripts:
                assemblies_status = "in-progress"
    elif (project_root / "Project_Specific" / "01_Project" / "01.03_design" / "create_assembly_stl.py").exists() or (project_root / "02_Design" / "create_assembly_stl.py").exists():
        assemblies_status = "in-progress"
    
    drawings_status = "pending"
    drawings_dir = design_dir / "manufacturing" / "drawings"
    if drawings_dir.exists():
        drawing_files = list(drawings_dir.glob("*.pdf")) + list(drawings_dir.glob("*.FCStd"))
        if drawing_files:
            drawings_status = "complete"
    
    dfm_status = "pending"
    # Check framework templates first, then project-specific
    dfm_review = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "DFM_review_process.md"
    dfm_checklist = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "DFM_checklist.md"
    if not dfm_review.exists():
        dfm_review = design_dir / "manufacturing" / "DFM_review_process.md"
    if not dfm_checklist.exists():
        dfm_checklist = design_dir / "manufacturing" / "DFM_checklist.md"
    if dfm_review.exists():
        dfm_status = "complete"
    elif dfm_checklist.exists():
        dfm_status = "in-progress"
    
    dfa_status = "pending"
    dfa_review = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "DFA_review_process.md"
    dfa_checklist = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "DFA_checklist.md"
    if not dfa_review.exists():
        dfa_review = design_dir / "manufacturing" / "DFA_review_process.md"
    if not dfa_checklist.exists():
        dfa_checklist = design_dir / "manufacturing" / "DFA_checklist.md"
    if dfa_review.exists():
        dfa_status = "complete"
    elif dfa_checklist.exists():
        dfa_status = "in-progress"
    
    # Check for validation tools
    # Check framework templates first, then project-specific
    manufacturing_dir = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing"
    if not manufacturing_dir.exists():
        manufacturing_dir = design_dir / "manufacturing"
    step_validator = (manufacturing_dir / "validate_step_files.py").exists()
    interference_checker = (manufacturing_dir / "check_assembly_interference.py").exists()
    tolerance_calculator = (manufacturing_dir / "tolerance_stackup_calculator.py").exists()
    fit_validator = (manufacturing_dir / "validate_assembly_fit.py").exists()
    gdt_annotations = (manufacturing_dir / "gdt_drawing_annotations.py").exists()
    
    # Check for validation reports
    step_validation_report = list(manufacturing_dir.glob("step_validation_report.md"))
    interference_report = list((design_dir / "assemblies").glob("*interference*.md")) if (design_dir / "assemblies").exists() else []
    tolerance_report = list(manufacturing_dir.glob("*tolerance*.md"))
    
    validation_tools_available = step_validator and interference_checker and tolerance_calculator and fit_validator
    validation_complete = len(step_validation_report) > 0 or len(interference_report) > 0 or len(tolerance_report) > 0
    
    step_validation_status = "complete" if validation_complete and step_validator else "in-progress" if step_validator else "pending"
    assembly_validation_status = "complete" if (len(interference_report) > 0 or len(tolerance_report) > 0) and interference_checker else "in-progress" if interference_checker else "pending"
    
    return {
        "conceptSketches": concept_sketches_status,
        "skeletons": skeletons_status,
        "manufacturing": manufacturing_status,
        "assemblies": assemblies_status,
        "drawings": drawings_status,
        "dfm": dfm_status,
        "dfa": dfa_status,
        "stepValidation": step_validation_status,
        "assemblyValidation": assembly_validation_status,
        "gdtDrawings": "complete" if gdt_annotations else "pending"
    }

def scan_production_status(project_root):
    """Scan production status"""
    prod_dir = project_root / "02_Design" / "production"
    
    # Check for production version in release log
    version = "Not Assigned"
    release_log = prod_dir / "release_log.md"
    if not release_log.exists():
        # Try framework templates location
        release_log = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "production" / "release_log.md"
    if release_log.exists():
        try:
            with open(release_log, 'r', encoding='utf-8') as f:
                content = f.read()
                # Extract version
                match = re.search(r'PROD-v(\d+\.\d+)', content)
                if match:
                    version = f"PROD-v{match.group(1)}"
        except:
            pass
    
    pre_review_status = "pending"
    release_gate_checklist = prod_dir / "release_gate_checklist.md"
    if not release_gate_checklist.exists():
        release_gate_checklist = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "production" / "release_gate_checklist.md"
    if release_gate_checklist.exists():
        try:
            with open(release_gate_checklist, 'r', encoding='utf-8') as f:
                content = f.read()
                if "Status:" in content and "Completed" in content:
                    pre_review_status = "complete"
                elif "Status:" in content and "In Progress" in content:
                    pre_review_status = "in-progress"
        except:
            pre_review_status = "in-progress" if release_gate_checklist.exists() else "pending"
    
    release_gate_status = "pending"
    if release_gate_checklist.exists():
        release_gate_status = "in-progress"
        try:
            with open(release_gate_checklist, 'r', encoding='utf-8') as f:
                content = f.read()
                if "Approved" in content or "Completed" in content:
                    release_gate_status = "complete"
        except:
            pass
    
    release_package_status = "pending"
    release_doc_template = prod_dir / "release_documentation_template.md"
    if not release_doc_template.exists():
        release_doc_template = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "production" / "release_documentation_template.md"
    if release_doc_template.exists():
        release_package_status = "in-progress"
        if version != "Not Assigned":
            release_package_status = "complete"
    
    return {
        "preReview": pre_review_status,
        "releaseGate": release_gate_status,
        "releasePackage": release_package_status,
        "version": version
    }

def scan_change_management(project_root):
    """Scan change management status"""
    eco_log = project_root / "02_Design" / "production" / "ECO_log.md"
    eco_requests_dir = project_root / "02_Design" / "production" / "ECO_requests"
    
    open_ecos = 0
    pending_approval = 0
    approved = 0
    eco_list = []
    
    # Count ECOs from requests directory
    if eco_requests_dir.exists():
        eco_files = list(eco_requests_dir.glob("ECO-*.md"))
        open_ecos = len(eco_files)
    
    # Parse ECO log if it exists
    if eco_log.exists():
        try:
            with open(eco_log, 'r', encoding='utf-8') as f:
                content = f.read()
                # Count by status
                pending_approval = content.count("Pending") + content.count("Under Review")
                approved = content.count("Approved") + content.count("Closed")
                
                # Extract ECO entries (simplified)
                lines = content.split('\n')
                for line in lines:
                    if 'ECO-' in line and '|' in line:
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 4:
                            eco_list.append({
                                "number": parts[1] if len(parts) > 1 else "ECO-XXX",
                                "description": parts[2] if len(parts) > 2 else "",
                                "status": parts[4] if len(parts) > 4 else "Pending"
                            })
        except:
            pass
    
    return {
        "openECOs": open_ecos,
        "pendingApproval": pending_approval,
        "approved": approved,
        "list": eco_list[:5]  # Latest 5
    }

def scan_compliance(project_root):
    """Scan compliance status"""
    # Check new structure first, fall back to old structure
    compliance_matrix = project_root / "Project_Specific" / "01_Project" / "01.02_requirements" / "compliance_matrix.md"
    if not compliance_matrix.exists():
        compliance_matrix = project_root / "00_Framework" / "00.03_templates" / "00.03.02_requirements" / "compliance_matrix_template.md"
    if not compliance_matrix.exists():
        compliance_matrix = project_root / "01_Requirements" / "compliance_matrix_template.md"
    
    compliance_test = project_root / "Project_Specific" / "01_Project" / "01.05_verification" / "compliance" / "compliance_test_plan.md"
    if not compliance_test.exists():
        compliance_test = project_root / "04_Verification" / "compliance" / "compliance_test_plan.md"
    
    certification = project_root / "Project_Specific" / "01_Project" / "01.05_verification" / "compliance" / "certification_documentation.md"
    if not certification.exists():
        certification = project_root / "04_Verification" / "compliance" / "certification_documentation.md"
    
    matrix_status = "complete" if compliance_matrix.exists() else "pending"
    testing_status = "complete" if compliance_test.exists() else "pending"
    cert_status = "complete" if certification.exists() else "pending"
    
    return {
        "matrix": matrix_status,
        "testing": testing_status,
        "certification": cert_status
    }

def scan_manufacturing_feedback(project_root):
    """Scan manufacturing feedback loop status"""
    # Check new structure first, fall back to old structure
    manufacturing_dir = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "manufacturing"
    if not manufacturing_dir.exists():
        manufacturing_dir = project_root / "02_Design" / "manufacturing"
    
    production_dir = project_root / "00_Framework" / "00.03_templates" / "00.03.04_manufacturing" / "production"
    if not production_dir.exists():
        production_dir = project_root / "02_Design" / "production"
    
    # Check for feedback tools
    issue_tracker = (manufacturing_dir / "manufacturing_issue_tracker.py").exists()
    feedback_db = (manufacturing_dir / "manufacturing_feedback_db.py").exists()
    supplier_templates = (production_dir / "supplier_communication_templates.md").exists()
    supplier_package_gen = (production_dir / "generate_supplier_package.py").exists()
    design_iteration = (manufacturing_dir / "design_iteration_workflow.md").exists()
    
    # Check for feedback data (project-specific)
    issues_file = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "manufacturing_issues.json"
    if not issues_file.exists():
        issues_file = manufacturing_dir / "manufacturing_issues.json"
    
    feedback_file = project_root / "Project_Specific" / "01_Project" / "01.03_design" / "manufacturing_feedback.json"
    if not feedback_file.exists():
        feedback_file = manufacturing_dir / "manufacturing_feedback.json"
    
    tools_available = issue_tracker and feedback_db and supplier_templates and supplier_package_gen
    data_exists = issues_file.exists() or feedback_file.exists()
    
    feedback_status = "complete" if tools_available and data_exists else "in-progress" if tools_available else "pending"
    
    return {
        "tools": "complete" if tools_available else "pending",
        "data": "complete" if data_exists else "pending",
        "status": feedback_status
    }

def scan_recent_activity(project_root):
    """Scan recent activity from session log"""
    # Check new structure first, fall back to old structure
    log_file = project_root / "Project_Specific" / "01_Project" / "01.06_logs" / "session_log.md"
    if not log_file.exists():
        log_file = project_root / "logs" / "session_log.md"
    activities = []
    
    if log_file.exists():
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                # Parse markdown table format
                for line in lines:
                    if '|' in line and '@' in line and not line.strip().startswith('|--'):
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 4 and parts[1] and parts[2] and parts[3]:
                            # Skip header row
                            if 'Date' in parts[1] or 'Role' in parts[1]:
                                continue
                            activities.append({
                                "date": parts[1] if len(parts) > 1 else "Unknown",
                                "role": parts[2] if len(parts) > 2 else "Unknown",
                                "action": parts[3] if len(parts) > 3 else "Activity",
                                "outcome": parts[4] if len(parts) > 4 else ""
                            })
        except Exception as e:
            pass
    
    # Return last 5 activities, most recent first
    return activities[-5:][::-1] if activities else []

def scan_timeline_data(project_root):
    """Scan timeline data from session logs and file system"""
    timeline_events = []
    project_initiated = None
    
    # Try to parse session log first (primary source)
    log_file = project_root / "Project_Specific" / "01_Project" / "01.06_logs" / "session_log.md"
    if not log_file.exists():
        log_file = project_root / "logs" / "session_log.md"
    if log_file.exists():
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if '|' in line and not line.strip().startswith('|--'):
                        parts = [p.strip() for p in line.split('|')]
                        # Skip header row
                        if len(parts) >= 4 and ('Date' in parts[1] or 'Role' in parts[1] or not parts[1]):
                            continue
                        if len(parts) >= 4 and parts[1] and parts[2] and parts[3]:
                            date_str = parts[1] if len(parts) > 1 else ""
                            role_str = parts[2] if len(parts) > 2 else ""
                            task_str = parts[3] if len(parts) > 3 else ""
                            outcome_str = parts[4] if len(parts) > 4 else ""
                            
                            # Extract persona from role (look for @PersonaName pattern)
                            persona = None
                            persona_match = re.search(r'@(\w+)', role_str)
                            if persona_match:
                                persona = f"@{persona_match.group(1)}"
                            elif role_str:
                                # Map common role names to personas
                                role_lower = role_str.lower()
                                if 'innovator' in role_lower or 'brainstorm' in role_lower:
                                    persona = "@Innovator"
                                elif 'senior' in role_lower or 'requirements' in role_lower:
                                    persona = "@SeniorEng"
                                elif 'design' in role_lower:
                                    persona = "@DesignEng"
                                elif 'builder' in role_lower or 'implement' in role_lower:
                                    persona = "@Builder"
                                elif 'skeptic' in role_lower or 'verification' in role_lower or 'test' in role_lower:
                                    persona = "@Skeptic"
                            
                            # Parse files from outcome column
                            files_list = []
                            if outcome_str:
                                # Extract file names (common patterns: file.ext, path/file.ext)
                                file_pattern = r'([\w\-_/]+\.(?:py|md|step|stl|json|html|css|js|png|jpg|pdf|FCStd))'
                                files_found = re.findall(file_pattern, outcome_str)
                                files_list = [f for f in files_found if not f.startswith('http')]
                            
                            # Parse date - try multiple formats
                            timestamp = None
                            try:
                                # Try YYYY-MM-DD format
                                if re.match(r'\d{4}-\d{2}-\d{2}', date_str):
                                    timestamp = date_str
                                # Try to parse with datetime
                                elif date_str:
                                    # Try common formats
                                    for fmt in ['%Y-%m-%d', '%Y/%m/%d', '%m/%d/%Y', '%d-%m-%Y']:
                                        try:
                                            dt = datetime.strptime(date_str, fmt)
                                            timestamp = dt.strftime('%Y-%m-%d')
                                            break
                                        except:
                                            continue
                            except:
                                pass
                            
                            if timestamp or date_str:
                                timeline_events.append({
                                    "timestamp": timestamp or date_str,
                                    "persona": persona or "Unknown",
                                    "command": task_str[:100],  # Truncate long descriptions
                                    "filesCreated": len(files_list),
                                    "filesList": files_list[:10]  # Limit to 10 files per event
                                })
        except Exception as e:
            pass
    
    # Fallback: Scan file system for creation dates if no session log
    if not timeline_events:
        try:
            # Get all project files (excluding common non-project files)
            exclude_dirs = {'.git', '__pycache__', '.vscode', 'node_modules', '.idea'}
            exclude_exts = {'.pyc', '.pyo', '.pyd', '.log'}
            
            file_events = {}
            for file_path in project_root.rglob('*'):
                if file_path.is_file():
                    # Skip excluded directories
                    if any(part in exclude_dirs for part in file_path.parts):
                        continue
                    # Skip excluded extensions
                    if file_path.suffix.lower() in exclude_exts:
                        continue
                    
                    try:
                        # Get file creation time (or modification time as fallback)
                        stat = file_path.stat()
                        # Windows: st_ctime is creation time, Unix: st_mtime is modification time
                        creation_time = datetime.fromtimestamp(stat.st_ctime)
                        date_key = creation_time.strftime('%Y-%m-%d')
                        
                        if date_key not in file_events:
                            file_events[date_key] = {
                                "timestamp": date_key,
                                "persona": "System",
                                "command": f"Files created/modified",
                                "filesCreated": 0,
                                "filesList": []
                            }
                        
                        file_events[date_key]["filesCreated"] += 1
                        if len(file_events[date_key]["filesList"]) < 10:
                            # Store relative path
                            rel_path = file_path.relative_to(project_root)
                            file_events[date_key]["filesList"].append(str(rel_path))
                    except:
                        continue
            
            # Convert to list and sort by date
            timeline_events = sorted(file_events.values(), key=lambda x: x["timestamp"])
        except Exception as e:
            pass
    
    # Determine project initiation date
    if timeline_events:
        # Use earliest event date
        project_initiated = min(event["timestamp"] for event in timeline_events)
    else:
        # Fallback: try to find earliest file in project
        try:
            earliest_date = None
            for file_path in project_root.rglob('*'):
                if file_path.is_file() and file_path.name not in ['.gitignore', '.cursorrules']:
                    try:
                        stat = file_path.stat()
                        creation_time = datetime.fromtimestamp(stat.st_ctime)
                        if earliest_date is None or creation_time < earliest_date:
                            earliest_date = creation_time
                    except:
                        continue
            if earliest_date:
                project_initiated = earliest_date.strftime('%Y-%m-%d')
        except:
            pass
    
    # If still no date, use current date as fallback
    if not project_initiated:
        project_initiated = datetime.now().strftime('%Y-%m-%d')
    
    # Sort events by timestamp (most recent first for display)
    timeline_events.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return {
        "projectInitiated": project_initiated,
        "events": timeline_events
    }

if __name__ == "__main__":
    print("Scanning project files...")
    dashboard_data = scan_project()
    
    # Write to JSON file for dashboard to read
    output_file = Path(__file__).parent / "dashboard_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, indent=2, ensure_ascii=False)
    
    print("[OK] Dashboard data generated successfully!")
    print(f"Data written to: {output_file}")
    metadata = dashboard_data.get('metadata', {})
    print(f"Last updated: {metadata.get('lastUpdated', 'Unknown')}")
    print(f"\nSummary:")
    current_phase = dashboard_data.get('currentPhase', {})
    print(f"   Current Phase: {current_phase.get('name', 'Unknown')} ({current_phase.get('progress', 0)}%)")
    print(f"   Overall Progress: {metadata.get('overallProgress', 0)}%")
    requirements = dashboard_data.get('requirements', {})
    print(f"   Requirements: {requirements.get('total', 0)} total ({requirements.get('approved', 0)} approved)")
    change_mgmt = dashboard_data.get('changeManagement', {})
    print(f"   Open ECOs: {change_mgmt.get('openECOs', 0)}")

