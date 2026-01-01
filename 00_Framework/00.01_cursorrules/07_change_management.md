# Change Management & Notification System

**Purpose:** Ensure all design changes are documented, communicated, and coordinated between personas efficiently.

---

## Change Notification Protocol

### When to Create Change Notification

**MANDATORY:** Create change notification when:
- Design dimensions change
- Component positions change
- Interface specifications change
- Material selection changes
- Manufacturing process changes
- Any change that affects other personas' work

### Change Notification Format

**Location:** `changes/change_[ID].md`

**Template:**
```markdown
# Change Notification: [Change ID]

**Date:** YYYY-MM-DD  
**Initiator:** @PersonaName  
**Change ID:** CHG-001  
**Priority:** High/Medium/Low  
**Status:** Pending/In Progress/Complete

## Change Summary
[Brief description of change]

## Component Affected
[Component name and part number]

## Change Details
[Detailed description of what changed]

## Impact Analysis
- **Affected Personas:** [List personas affected]
- **Affected Components:** [List components affected]
- **Impact Description:** [How this change affects other work]

## Required Actions
- [ ] @PersonaName: [Action required]
- [ ] @PersonaName: [Action required]

## Notification Status
- [ ] @DesignEng notified
- [ ] @ElectroMechEng notified
- [ ] @SeniorEng notified
- [ ] @Skeptic notified

## Resolution
[How change was resolved, decisions made, etc.]
```

---

## Team Discussion Protocol

### When to Initiate Team Discussion

**Initiate team discussion when:**
- Complex coordination needed between multiple personas
- Change affects multiple subsystems
- Conflict resolution requires input from multiple personas
- Design decision needs team consensus
- Interface definition requires coordination

### Team Discussion Format

**Location:** `coordination/discussions/discussion_[ID].md`

**Template:**
```markdown
# Team Discussion: [Discussion ID]

**Date:** YYYY-MM-DD  
**Initiator:** @PersonaName  
**Discussion ID:** DISC-001  
**Topic:** [Discussion topic]  
**Status:** Open/Resolved

## Participants
- @DesignEng
- @ElectroMechEng
- @SeniorEng
- [Other relevant personas]

## Discussion Topic
[What needs to be discussed]

## Discussion Points
### @PersonaName:
[Input from persona]

### @PersonaName:
[Input from persona]

## Decisions Made
1. [Decision 1]
2. [Decision 2]

## Action Items
- [ ] @PersonaName: [Action item]
- [ ] @PersonaName: [Action item]

## Resolution
[Final resolution and next steps]
```

---

## Change Propagation Workflow

### Step 1: Change Initiation
1. Persona identifies need for change
2. Creates change notification document
3. Performs impact analysis
4. Identifies affected personas

### Step 2: Notification
1. Update change log: `changes/change_log.md`
2. Notify all affected personas
3. Tag personas in change notification
4. Set notification status

### Step 3: Review & Acknowledgment
1. Affected personas review change
2. Acknowledge receipt of notification
3. Assess impact on their work
4. Provide feedback if needed

### Step 4: Implementation
1. Initiator implements change
2. Update affected components
3. Update geometric state ledger if needed
4. Update interface control documents if needed

### Step 5: Validation
1. Verify change implemented correctly
2. Verify all affected work updated
3. Update change notification status to "Complete"
4. Document in change log

---

## Efficient Communication Mechanism

### Notification Channels

1. **Change Notification Documents:** For formal change tracking
2. **Coordination Log:** For coordination events
3. **Team Discussion Documents:** For complex coordination
4. **Challenge Documents:** For design challenges

### Communication Rules

1. **Immediate Notification:** For critical changes (High priority)
   - Create notification immediately
   - Tag all affected personas
   - Update coordination log

2. **Batch Notification:** For non-critical changes (Medium/Low priority)
   - Can batch multiple changes
   - Daily update to coordination log
   - Weekly summary if needed

3. **Documentation:** All communication must be documented
   - No verbal-only coordination
   - All decisions documented
   - All acknowledgments recorded

---

## Change Log

**Location:** `changes/change_log.md`

**Format:**
| Date | Change ID | Initiator | Component | Change Description | Affected Personas | Status | Resolution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YYYY-MM-DD | CHG-001 | @DesignEng | Enclosure | Height increased by 5mm | @ElectroMechEng | Complete | Accepted, PCB clearance verified |

---

## Change Impact Analysis

### Impact Categories

1. **Geometric Impact:** Changes to dimensions, positions, clearances
2. **Interface Impact:** Changes to interfaces between components
3. **Material Impact:** Changes to material selection
4. **Process Impact:** Changes to manufacturing process
5. **Assembly Impact:** Changes to assembly sequence or requirements

### Impact Analysis Process

1. **Identify Direct Impact:** What directly changes?
2. **Identify Cascading Impact:** What else is affected?
3. **Identify Personas Affected:** Who needs to know?
4. **Assess Risk:** What's the risk if change not communicated?
5. **Define Required Actions:** What must each persona do?

---

## Change Approval Process

### Approval Levels

1. **Self-Approval:** For minor changes with no impact on others
2. **Persona Coordination:** For changes affecting other personas (coordinate directly)
3. **User Approval:** For major changes or conflicts

### Approval Workflow

1. Initiator creates change notification
2. Performs impact analysis
3. If no impact on others: Self-approve and implement
4. If impact on others: Notify affected personas
5. If conflict: Escalate to user
6. Document approval and implementation

---

## Integration with Workflow

- **Throughout Design Phase:** Change notifications for design changes
- **Sub-phase 3.1:** Skeleton modification notifications
- **Sub-phase 3.2:** Part design change notifications
- **Sub-phase 3.3:** Assembly modification notifications
- **Coordination Events:** Team discussions for complex coordination

---

## Best Practices

1. **Be Proactive:** Notify early, not after implementation
2. **Be Complete:** Include all relevant details in notification
3. **Be Responsive:** Acknowledge and respond to notifications promptly
4. **Be Documented:** Document all changes and communications
5. **Be Coordinated:** Use team discussions for complex coordination

---

## Checklist

Before implementing change:
- [ ] Change notification created
- [ ] Impact analysis complete
- [ ] Affected personas identified
- [ ] All personas notified
- [ ] Approvals obtained (if needed)
- [ ] Change log updated

After implementing change:
- [ ] Change implemented
- [ ] All affected work updated
- [ ] Geometric state ledger updated (if needed)
- [ ] Interface documents updated (if needed)
- [ ] Change notification status updated
- [ ] Change log updated

