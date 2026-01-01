# How to Use the Project Dashboard

A simple step-by-step guide to view and use your project dashboard.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Generate Dashboard Data
Open PowerShell or Terminal in the project folder and run:
```powershell
python generate_dashboard_data.py
```
This creates the `dashboard_data.json` file that the dashboard needs.

### Step 2: Start the Web Server
**Option A - Easy Way (Windows):**
- Double-click `start_dashboard_server.bat`
- A terminal window will open showing the server is running

**Option B - PowerShell:**
- Right-click in the project folder
- Select "Open in Terminal" or "Open PowerShell here"
- Run: `python -m http.server 8000`

**Option C - Manual Command:**
```powershell
python -m http.server 8000
```

**⚠️ Important:** Keep the terminal window open while viewing the dashboard!

### Step 3: Open the Dashboard
1. Open your web browser (Chrome, Firefox, Edge, etc.)
2. Go to: `http://localhost:8000/PROJECT_DASHBOARD.html`
3. The dashboard will load automatically!

---

## 📊 What You'll See

The dashboard shows:

- **📍 Current Phase** - Which phase of the V-Model you're in (1-9)
- **📋 Requirements** - Total count, approved, in-progress, pending
- **🎨 Design Status** - Skeletons, manufacturing files, drawings, DFM/DFA
- **🏭 Production Readiness** - Release gate status, version number
- **📝 Change Management** - Open ECOs, pending approvals
- **✅ Compliance** - Compliance matrix, testing, certification
- **📝 Recent Activity** - Latest project activities

---

## 🔄 Refreshing the Dashboard

### Update the Data
When you make changes to the project, update the dashboard data:
```powershell
python generate_dashboard_data.py
```

### Refresh in Browser
- Click the **"🔄 Refresh Dashboard"** button (top right)
- Or wait for auto-refresh (happens every 60 seconds)

---

## ❓ Common Questions

### Q: Why do I need a web server?
**A:** Browsers block loading local JSON files for security. A web server solves this.

### Q: Can I just double-click the HTML file?
**A:** No, it won't load the data. You must use a web server (see Step 2 above).

### Q: What port does it use?
**A:** Port 8000 by default. If that's busy, use a different port:
```powershell
python -m http.server 8080
```
Then open: `http://localhost:8080/PROJECT_DASHBOARD.html`

### Q: The dashboard shows "Error loading dashboard data"
**A:** Make sure:
1. You ran `python generate_dashboard_data.py` first
2. The web server is running
3. You're accessing via `http://localhost:8000/` (not `file://`)

### Q: How often should I update the dashboard?
**A:** Run `generate_dashboard_data.py`:
- After creating new requirements
- After design milestones
- After production releases
- Before important meetings
- At the end of work sessions

---

## 🛠️ Troubleshooting

### Problem: "Failed to load dashboard data"
**Solution:**
1. Check that `dashboard_data.json` exists in the project folder
2. If not, run: `python generate_dashboard_data.py`
3. Make sure the web server is still running
4. Refresh the browser page

### Problem: "This site can't be reached" (localhost error)
**Solution:**
1. Make sure the web server is running (check the terminal window)
2. Verify you're using the correct URL: `http://localhost:8000/PROJECT_DASHBOARD.html`
3. Try a different port if 8000 is busy

### Problem: Dashboard shows old information
**Solution:**
1. Run `python generate_dashboard_data.py` to update the data
2. Click the "Refresh Dashboard" button in the browser
3. Or wait for auto-refresh (60 seconds)

### Problem: Port 8000 is already in use
**Solution:**
Use a different port:
```powershell
python -m http.server 8080
```
Then open: `http://localhost:8080/PROJECT_DASHBOARD.html`

---

## 💡 Tips

1. **Bookmark the URL:** Save `http://localhost:8000/PROJECT_DASHBOARD.html` as a bookmark for quick access

2. **Keep Server Running:** Don't close the terminal window while viewing the dashboard

3. **Auto-Refresh:** The dashboard refreshes every 60 seconds automatically, but you can click the refresh button anytime

4. **VS Code Users:** Install the "Live Server" extension for even easier access:
   - Install "Live Server" extension
   - Right-click `PROJECT_DASHBOARD.html`
   - Select "Open with Live Server"

5. **Multiple Projects:** If you have multiple projects, use different ports:
   - Project 1: `python -m http.server 8000`
   - Project 2: `python -m http.server 8001`
   - Project 3: `python -m http.server 8002`

---

## 📁 Files Involved

- `PROJECT_DASHBOARD.html` - The dashboard interface (open in browser)
- `generate_dashboard_data.py` - Script to generate dashboard data
- `dashboard_data.json` - Generated data file (created by the script)
- `start_dashboard_server.bat` - Windows helper to start server
- `start_dashboard_server.ps1` - PowerShell helper to start server
- `HOW_TO_USE_DASHBOARD.md` - This file

---

## 🎯 Summary

1. **Generate data:** `python generate_dashboard_data.py`
2. **Start server:** Double-click `start_dashboard_server.bat` or run `python -m http.server 8000`
3. **Open browser:** Go to `http://localhost:8000/PROJECT_DASHBOARD.html`
4. **Refresh when needed:** Run the generate script again and click refresh

That's it! You're ready to use the dashboard! 🎉

---

**Need more help?** See `DASHBOARD_README.md` for detailed technical information.

**Last Updated:** 2024-12-22

