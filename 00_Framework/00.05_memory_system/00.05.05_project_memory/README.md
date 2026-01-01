# Project Memory System

**Purpose:** Comprehensive memory system to track project state, decisions, coordination, changes, interfaces, geometric state, and validation throughout the project lifecycle.

---

## Memory Sections

### 1. Project State Memory
**Location:** `project_memory/project_state.json`  
**Purpose:** Track current phase, completed work, pending tasks, blockers, next actions  
**Files:** `project_state.json`

### 2. Decision Memory
**Location:** `project_memory/decisions/decision_log.md`  
**Purpose:** Record critical decisions and rationale  
**Files:** `decision_log.md`, individual decision documents

### 3. Coordination Memory
**Location:** `coordination/coordination_log.md`  
**Purpose:** Track persona interactions, handoffs, agreements, conflicts  
**Files:** `coordination_log.md`, challenge documents, input documents, discussion documents, escalation documents

### 4. Change History Memory
**Location:** `changes/change_log.md`  
**Purpose:** Track design changes and impacts  
**Files:** `change_log.md`, individual change notification documents

### 5. Interface Memory
**Location:** `interfaces/interface_registry.md`  
**Purpose:** Single source of truth for interfaces  
**Files:** `interface_registry.md`, ICD documents, interface change requests, interface notifications

### 6. Geometric State Memory
**Location:** `02_Design/geometric_state/state_ledger.md`  
**Purpose:** Persistent geometric state tracking  
**Files:** `state_ledger.md`, `update_log.md`, `validation_log.md`, `gcs_definition.md`, `interference_checks.md`

### 7. Validation Memory
**Location:** `validation/validation_log.md`  
**Purpose:** Track validation checkpoints and results  
**Files:** `validation_log.md`, individual validation documents

---

## Master Memory File

**Location:** `project_memory/master_memory.json`

**Purpose:** Central registry of all memory sections with metadata:
- Memory section name and description
- File locations
- File lists with timestamps
- File counts
- Last update timestamps

---

## Dashboard Integration

The master memory file is integrated with the project dashboard to display:
- Memory section names
- Number of files in each section
- Timestamps of last file updates
- File names for each section
- Statistics and summaries

---

## Usage

### Updating Memory

1. **Update Memory Section:** Update the relevant memory file
2. **Update Master Memory:** Run update script to sync master memory
3. **Dashboard Refresh:** Dashboard automatically reflects updates

### Querying Memory

1. **Check Master Memory:** Review `master_memory.json` for overview
2. **Check Specific Section:** Review relevant memory file
3. **Check Dashboard:** View memory status in project dashboard

---

## Maintenance

### Regular Updates

- Update memory files after each significant event
- Sync master memory regularly
- Refresh dashboard to reflect updates

### Validation

- Verify all memory sections are up to date
- Check for missing files or updates
- Validate file counts and timestamps

---

## See Also

- `cursorrules_modules/05_coordination.md` - Coordination protocol
- `cursorrules_modules/07_change_management.md` - Change management
- `cursorrules_modules/08_geometric_state_sync.md` - Geometric state sync
- `interfaces/interface_control_system.md` - Interface control system

