# Project Dashboard - User Guide

**Purpose:** Interactive dashboard showing real-time project status from @SeniorEng's perspective

**Location:** `PROJECT_DASHBOARD.html`

---

## Quick Start

1. **Generate Dashboard Data:**
   - Run `python generate_dashboard_data.py` to create `dashboard_data.json`
   - This must be done first!

2. **Start a Local Web Server:**
   - **IMPORTANT:** The dashboard cannot load data when opened directly from the file system
   - **Easy Method:** Double-click `start_dashboard_server.bat` (Windows) or run `start_dashboard_server.ps1` (PowerShell)
   - **Manual Method:** Open PowerShell/Terminal in the project root directory and run: `python -m http.server 8000`
   - Keep this terminal window open while viewing the dashboard

3. **Open the Dashboard:**
   - Open your web browser
   - Navigate to: `http://localhost:8000/PROJECT_DASHBOARD.html`
   - The dashboard will automatically load data from `dashboard_data.json`

4. **Refresh the Dashboard:**
   - Click the **"🔄 Refresh Dashboard"** button to update
   - Or wait for auto-refresh (every 60 seconds)

5. **Update Dashboard Data:**
   - Run `python generate_dashboard_data.py` again to update `dashboard_data.json`
   - Click "Refresh Dashboard" in the browser to see updates

---

## What the Dashboard Shows

### Current Phase
- Current workflow phase (1-9)
- Sub-phase name
- Overall progress percentage

### Requirements Status
- Total requirements count
- Approved, In Progress, Pending counts
- List of recent requirements with status

### Design Status
- 3D Skeletons (pending/in-progress/complete)
- Manufacturing-Ready Files
- Assemblies
- Technical Drawings
- DFM Review
- DFA Review

### Production Readiness
- Pre-Production Review status
- Release Gate Checklist status
- Release Documentation status
- Production Version (PROD-v1.0, etc.)

### Change Management
- Open ECOs count
- Pending Approval count
- Approved ECOs count
- Recent ECO list

### Compliance Status
- Compliance Matrix
- Compliance Testing
- Certification

### Recent Activity
- Latest activities from session log
- Shows role, action, and timestamp

---

## How It Works

1. **Data Generation:**
   - `generate_dashboard_data.py` scans project files
   - Determines current phase based on file existence
   - Counts requirements, checks design status, etc.
   - Generates `dashboard_data.json`

2. **Dashboard Display:**
   - `PROJECT_DASHBOARD.html` reads `dashboard_data.json`
   - Displays data in interactive cards
   - Auto-refreshes every 60 seconds
   - Manual refresh button available

---

## When to Update Dashboard

**@SeniorEng should run `generate_dashboard_data.py` when:**
- New requirements are created
- Design phase progresses (skeletons → manufacturing-ready)
- Production release occurs
- ECOs are created or updated
- Any significant project milestone is reached

**Or simply run it periodically:**
- Before important meetings
- At end of each work session
- When checking project status

---

## Troubleshooting

### Dashboard shows "Error loading dashboard data" or "Could not load dashboard data"
- **Problem:** Browser security blocks loading local JSON files when opening HTML directly
- **Solution 1 (Recommended):** Use a local web server:
  ```powershell
  python -m http.server 8000
  ```
  Then open: `http://localhost:8000/PROJECT_DASHBOARD.html`
- **Solution 2:** Use VS Code "Live Server" extension:
  - Install "Live Server" extension
  - Right-click `PROJECT_DASHBOARD.html`
  - Select "Open with Live Server"
- **Solution 3:** Ensure `dashboard_data.json` exists:
  - Run `python generate_dashboard_data.py` first

### Dashboard shows "Could not load dashboard data" even with server
- **Solution:** Check that `dashboard_data.json` exists in the same directory as `PROJECT_DASHBOARD.html`
- **Solution:** Run `python generate_dashboard_data.py` to regenerate the file
- **Solution:** Check browser console (F12) for specific error messages

### Dashboard shows outdated information
- **Solution:** Click "Refresh Dashboard" button or run `generate_dashboard_data.py` again

### Dashboard doesn't auto-refresh
- **Solution:** Check browser console for errors. Ensure `dashboard_data.json` exists and is accessible
- **Solution:** Make sure the web server is still running

---

## File Structure

```
Project Root/
├── PROJECT_DASHBOARD.html          # Interactive dashboard (open in browser)
├── generate_dashboard_data.py       # Script to scan project and generate data
├── dashboard_data.json              # Generated data file (read by dashboard)
├── start_dashboard_server.bat       # Windows batch file to start server
├── start_dashboard_server.ps1       # PowerShell script to start server
└── DASHBOARD_README.md             # This file
```

---

## Integration with @SeniorEng

The dashboard is automatically maintained by @SeniorEng as part of their Project Awareness responsibilities. The dashboard reflects @SeniorEng's view of the project status.

**See:** `cursorrules_modules/01_personas/senior_eng.md` - "Project Awareness & Dashboard" section

---

**Last Updated:** 2024-12-22

