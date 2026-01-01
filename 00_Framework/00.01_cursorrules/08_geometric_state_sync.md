# Geometric State Synchronization Protocol

**Purpose:** Ensure geometric state ledger remains consistent when multiple personas update it. Prevent conflicts, lost data, and inconsistencies.

**CRITICAL:** Geometric state sync is a priority. All updates must be synchronized properly.

---

## Sync Priority

**Geometric state synchronization is CRITICAL and takes priority over other tasks.**

1. **Before any design work:** Check current geometric state
2. **Before updating:** Verify no conflicts with other personas' updates
3. **After updating:** Immediately sync with master ledger
4. **Before assembly:** Verify all geometric states are synchronized

---

## Geometric State Update Protocol

### Single Persona Update (No Conflict Risk)

**When:** Only one persona is updating geometric state

**Process:**
1. Read current state ledger: `02_Design/geometric_state/state_ledger.md`
2. Update ledger with new component positions
3. Save updated ledger
4. Document update in change log: `02_Design/geometric_state/update_log.md`

### Multi-Persona Update (Conflict Risk)

**When:** Multiple personas need to update geometric state

**Process:**
1. **Check for Active Updates:**
   - Check update log for recent updates
   - Check coordination log for ongoing updates
   - Verify no other persona is currently updating

2. **Lock Mechanism (Sequential Updates):**
   - If @DesignEng updating: @ElectroMechEng waits
   - If @ElectroMechEng updating: @DesignEng waits
   - Document lock in coordination log

3. **Update Sequence:**
   - Persona 1 updates ledger
   - Persona 1 notifies Persona 2
   - Persona 2 reads updated ledger
   - Persona 2 updates ledger (if needed)
   - Both verify consistency

4. **Conflict Detection:**
   - Compare updates from both personas
   - Identify conflicts (same component, different positions)
   - Flag conflicts for resolution

---

## Conflict Detection & Resolution

### Conflict Types

1. **Position Conflict:** Same component has different positions from different personas
2. **Dimension Conflict:** Same component has different dimensions
3. **Missing Component:** Component in one persona's update but not in ledger
4. **Orphaned Component:** Component in ledger but not in persona's update

### Conflict Detection Process

1. **Automated Check:**
   - Run conflict detection script: `02_Design/geometric_state/detect_conflicts.py`
   - Compare current ledger with new updates
   - Flag all conflicts

2. **Manual Review:**
   - Review flagged conflicts
   - Determine if conflict is real or false positive
   - Document conflict in: `02_Design/geometric_state/conflicts/conflict_[ID].md`

### Conflict Resolution Process

**Step 1: Conflict Identification**
- Document conflict in conflict file
- Include:
  - Component name
  - Conflicting values
  - Persona 1 value and source
  - Persona 2 value and source

**Step 2: Persona Coordination**
- @DesignEng and @ElectroMechEng review conflict
- Attempt direct resolution
- Document resolution attempt

**Step 3: Escalation (if needed)**
- If direct resolution fails, escalate to user
- Present conflict with both personas' positions
- User makes final decision

**Step 4: Resolution Implementation**
- Update ledger with resolved values
- Remove conflict from active conflicts
- Document resolution in conflict file

---

## Merge Process for Multi-Persona Updates

### Merge Strategy

1. **Component-Based Merge:**
   - Merge by component
   - If component only in one update: Add to ledger
   - If component in both updates: Resolve conflict

2. **Priority-Based Merge:**
   - @DesignEng has priority for mechanical components
   - @ElectroMechEng has priority for electrical components
   - Shared components: Resolve conflict

3. **Timestamp-Based Merge:**
   - Most recent update takes precedence (if no conflict)
   - Conflicts always require resolution

### Merge Process

1. **Read Both Updates:**
   - Read @DesignEng's update
   - Read @ElectroMechEng's update
   - Read current ledger

2. **Identify Components:**
   - List all components from all sources
   - Identify unique components
   - Identify shared components

3. **Merge Components:**
   - For unique components: Add to ledger
   - For shared components: Check for conflicts
   - Resolve conflicts if found

4. **Validate Merge:**
   - Verify all components included
   - Verify no duplicates
   - Verify positions are valid
   - Verify coordinate system consistency

5. **Save Merged Ledger:**
   - Save updated ledger
   - Document merge in update log
   - Notify all personas of merge

---

## Geometric State Validation

### Validation Checkpoints

1. **After Each Update:** Validate update before saving
2. **Before Assembly:** Validate all components synchronized
3. **After Merge:** Validate merge successful
4. **Periodic:** Regular validation checks

### Validation Criteria

- **Completeness:** All components from all personas included
- **Consistency:** No conflicting positions
- **Accuracy:** Positions match actual design
- **Coordinate System:** All positions use same GCS
- **Orientation:** All orientations valid

### Validation Process

1. **Run Validation Script:**
   - `02_Design/geometric_state/validate_state.py`
   - Checks all validation criteria
   - Reports any issues

2. **Manual Review:**
   - Review validation report
   - Fix any issues found
   - Re-run validation

3. **Document Validation:**
   - Document validation results
   - Update validation log: `02_Design/geometric_state/validation_log.md`

---

## Update Log

**Location:** `02_Design/geometric_state/update_log.md`

**Format:**
| Date | Time | Persona | Component | Update Type | Status | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YYYY-MM-DD | HH:MM | @DesignEng | Enclosure | Position Update | Complete | Updated position [10, 20, 5] |

**Update Types:**
- Position Update: Component position changed
- Dimension Update: Component dimensions changed
- Add Component: New component added
- Remove Component: Component removed
- Merge: Multi-persona merge performed

---

## Sync Checklist

Before updating geometric state:
- [ ] Check current ledger state
- [ ] Check for active updates from other personas
- [ ] Verify coordinate system consistency
- [ ] Prepare update with all required information

After updating geometric state:
- [ ] Save updated ledger
- [ ] Document update in update log
- [ ] Notify other personas (if multi-persona)
- [ ] Validate update
- [ ] Check for conflicts

Before assembly:
- [ ] Verify all personas' updates synchronized
- [ ] Run conflict detection
- [ ] Resolve any conflicts
- [ ] Validate complete state
- [ ] Verify all components included

---

## Best Practices

1. **Update Frequently:** Update ledger after each design change
2. **Sync Immediately:** Sync updates as soon as possible
3. **Document Everything:** Document all updates and merges
4. **Validate Regularly:** Run validation checks regularly
5. **Resolve Conflicts Promptly:** Don't let conflicts accumulate
6. **Communicate:** Notify other personas of updates

---

## Integration with Workflow

- **Sub-phase 3.0:** Initialize geometric state
- **Sub-phase 3.1:** Update with skeleton positions
- **Sub-phase 3.2:** Update with part positions
- **Sub-phase 3.3:** Validate assembly state
- **Throughout:** Continuous sync and validation

---

## Tools

- **Conflict Detection:** `02_Design/geometric_state/detect_conflicts.py`
- **State Validation:** `02_Design/geometric_state/validate_state.py`
- **Merge Tool:** `02_Design/geometric_state/merge_updates.py` (if needed)

---

## Critical Rules

1. **NEVER update ledger without checking for conflicts first**
2. **ALWAYS document updates in update log**
3. **ALWAYS validate after merge**
4. **ALWAYS notify other personas of updates**
5. **ALWAYS resolve conflicts before proceeding**

