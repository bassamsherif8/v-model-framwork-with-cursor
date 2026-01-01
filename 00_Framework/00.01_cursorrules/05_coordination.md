# Persona Coordination Protocol

**Purpose:** Define how personas coordinate, hand off work, resolve conflicts, and maintain design consistency.

---

## Core Principles

1. **Design Ownership:** @DesignEng owns all mechanical design decisions
2. **Challenge Rights:** @ElectroMechEng can challenge designs with technical justification
3. **User Authority:** All conflicts escalate to user/project manager for final decision
4. **Documentation:** All coordination events, challenges, and resolutions must be documented

---

## Handshake Mechanism

### When @ElectroMechEng Needs to Challenge @DesignEng's Design

**Step 1: Challenge Request**
- @ElectroMechEng identifies issue with @DesignEng's design
- Creates challenge document: `coordination/challenges/challenge_[ID].md`
- Includes:
  - Challenge ID, date, challenger (@ElectroMechEng)
  - Design component being challenged
  - Technical justification (why the challenge is needed)
  - Proposed alternative or modification
  - Impact analysis (what changes if challenge is accepted)
  - Priority (High/Medium/Low)
- **Memory Update (MANDATORY):**
  - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with challenge event
  - Include: Event ID, date, initiator, recipient, event type "Challenge", description, status
  - **BLOCKING:** Cannot proceed to Step 2 if coordination log not updated

**Step 2: @DesignEng Review**
- @DesignEng reviews challenge document
- Responds within challenge document:
  - Accepts challenge (with modifications if needed)
  - Rejects challenge (with technical justification)
  - Requests clarification
- Updates design if challenge accepted
- **Memory Update (MANDATORY):**
  - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with review response
  - Update status: "Accepted", "Rejected", or "Clarification Requested"
  - If challenge accepted, update `change_log.md` with design change
  - **BLOCKING:** Cannot proceed to Step 3 if coordination log not updated

**Step 3: Conflict Resolution**
- If @DesignEng rejects and @ElectroMechEng maintains challenge → **ESCALATE TO USER**
- User/project manager makes final decision
- Decision documented in challenge document
- All affected personas notified of decision
- **Memory Update (MANDATORY):**
  - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with resolution
  - If escalated, update status: "Escalated" and create escalation document
  - Update `decision_log.md` with final decision and rationale
  - **BLOCKING:** Cannot proceed to Step 4 if coordination log and decision log not updated

**Step 4: Implementation**
- If challenge accepted: @DesignEng implements changes
- If challenge rejected: @ElectroMechEng adapts electro-mechanical design
- If escalated: User decision is final, both personas implement accordingly

---

## Coordination Events

### Standard Coordination Events

1. **Design Handoff:** @DesignEng → @ElectroMechEng
   - @DesignEng completes mechanical skeleton/design
   - Notifies @ElectroMechEng via coordination log
   - @ElectroMechEng reviews and provides input
   - **Memory Update (MANDATORY):**
     - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with handoff event
     - Include: Event ID, date, initiator (@DesignEng), recipient (@ElectroMechEng), event type "Handoff", description, status "Complete"
     - **BLOCKING:** Cannot proceed with handoff if coordination log not updated

2. **Electro-Mechanical Input:** @ElectroMechEng → @DesignEng
   - @ElectroMechEng identifies PCB mounting requirements
   - Provides input document: `coordination/inputs/input_[ID].md`
   - @DesignEng incorporates input into design
   - **Memory Update (MANDATORY):**
     - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with input event
     - Include: Event ID, date, initiator (@ElectroMechEng), recipient (@DesignEng), event type "Input", description, status
     - Update `interface_registry.md` if interfaces change
     - **BLOCKING:** Cannot proceed with design incorporation if coordination log not updated

3. **Change Notification:** Any persona → Affected personas
   - Persona makes design change
   - Creates change notification: `changes/change_[ID].md`
   - Notifies all affected personas
   - All personas review and update their work if needed
   - **Memory Update (MANDATORY):**
     - Update `00_Framework/00.05_memory_system/00.05.02_changes/change_log.md` with change details
     - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with change notification event
     - Include: Event ID, date, initiator, recipients, event type "Change", description, status
     - **BLOCKING:** Cannot proceed with change implementation if change log and coordination log not updated

4. **Team Discussion:** Multiple personas
   - When complex coordination needed
   - Create discussion document: `coordination/discussions/discussion_[ID].md`
   - All relevant personas contribute
   - Document decisions and action items
   - **Memory Update (MANDATORY):**
     - Update `00_Framework/00.05_memory_system/00.05.01_coordination/coordination_log.md` with discussion event
     - Include: Event ID, date, participants, event type "Discussion", description, decisions made, action items, status
     - Update `decision_log.md` with decisions made during discussion
     - **BLOCKING:** Cannot proceed with implementation if coordination log and decision log not updated

---

## Coordination Log

**Location:** `coordination/coordination_log.md`

**Format:**
| Date | Event ID | Initiator | Recipient | Event Type | Description | Status | Resolution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| YYYY-MM-DD | EVT-001 | @DesignEng | @ElectroMechEng | Handoff | Mechanical skeleton complete | Complete | - |
| YYYY-MM-DD | EVT-002 | @ElectroMechEng | @DesignEng | Challenge | PCB clearance insufficient | Escalated | User decision pending |

**Event Types:**
- Handoff: Work transferred from one persona to another
- Challenge: Design challenge raised
- Input: Technical input provided
- Change: Design change notification
- Discussion: Team discussion/meeting
- Resolution: Conflict resolved

---

## Conflict Resolution Process

### Level 1: Direct Resolution
- Personas attempt to resolve directly
- Document resolution in coordination log
- Update designs accordingly

### Level 2: Escalation to User
- If direct resolution fails
- Create escalation document: `coordination/escalations/escalation_[ID].md`
- Include:
  - Conflict summary
  - @DesignEng position and justification
  - @ElectroMechEng position and justification
  - Impact analysis
  - Recommended resolution (if applicable)
- User makes final decision
- Document decision and implement

---

## Communication Protocols

### Notification Requirements

1. **Immediate Notification:** For critical changes or conflicts
   - Create notification document
   - Update coordination log
   - Tag affected personas in notification

2. **Regular Updates:** For ongoing coordination
   - Update coordination log daily
   - Document all interactions
   - Track pending items

3. **Change Propagation:** When design changes
   - Identify all affected personas
   - Create change notification
   - Wait for acknowledgment before proceeding
   - Update all relevant documents

### Documentation Requirements

- **All coordination events must be documented**
- **All challenges must be tracked**
- **All conflicts must be escalated if unresolved**
- **All decisions must be recorded**

---

## Memory Update Requirements (MANDATORY)

**ALL coordination events MUST update the coordination log. This is non-negotiable.**

### Memory Update Checklist for Each Coordination Event:
- [ ] Coordination log updated with event details (Event ID, date, initiator, recipient, type, description, status)
- [ ] Decision log updated if decisions made (for discussions, escalations, resolutions)
- [ ] Change log updated if design changes occur (for change notifications, accepted challenges)
- [ ] Interface registry updated if interfaces change (for input events, design changes)
- [ ] Project state updated if phase transitions occur (for handoffs)

### Memory Update Enforcement:
- **BLOCKING:** No coordination event can proceed to next step if coordination log not updated
- **BLOCKING:** No handoff can complete if coordination log not updated
- **BLOCKING:** No challenge can resolve if coordination log and decision log not updated
- **BLOCKING:** No change can implement if change log and coordination log not updated

## Coordination Checklist

Before proceeding to next phase, verify:
- [ ] All coordination events documented in coordination log
- [ ] All challenges resolved or escalated (coordination log updated)
- [ ] All affected personas notified of changes (coordination log updated)
- [ ] All handoffs completed (coordination log updated)
- [ ] Coordination log up to date with all events
- [ ] Decision log updated for all decisions made
- [ ] Change log updated for all design changes
- [ ] No pending conflicts

---

## Examples

### Example 1: Challenge Process
```
@ElectroMechEng: "I need to challenge the enclosure height. The PCB with tall capacitors requires 5mm more clearance."

1. Creates challenge document
2. @DesignEng reviews: "I can increase height by 5mm, but this affects overall dimensions. Accept with modification to maintain aspect ratio."
3. Both agree, @DesignEng implements change
4. Documented in coordination log
```

### Example 2: Escalation
```
@ElectroMechEng: "PCB mounting holes need to be 2mm larger for thermal expansion."
@DesignEng: "This conflicts with structural requirements. I cannot accommodate."

1. Both document positions
2. Escalate to user
3. User decides: "Use thermal pads instead of larger holes"
4. Both implement user decision
```

---

## Integration with Workflow

- **Sub-phase 3.1:** Skeleton creation coordination
- **Sub-phase 3.2:** Design refinement coordination
- **Sub-phase 3.3:** Assembly coordination
- **Throughout:** Change notification and conflict resolution

See `cursorrules_modules/02_workflow.md` for workflow integration details.

