# V-Model Framework Copier v2.0

A simple GUI application to copy reusable framework files from an existing V-Model project to start a new project.

## 📋 What It Does

The template copier identifies and copies all reusable framework files while excluding project-specific content:

- ✅ Core rules and personas (`cursorrules_modules/`)
- ✅ Common parts library (`02_Design/common_parts/`)
- ✅ Production templates (`02_Design/production/`)
- ✅ Manufacturing framework templates (`02_Design/manufacturing/`)
- ✅ Requirements templates (`01_Requirements/`)
- ✅ Dashboard files and scripts
- ✅ Documentation and guides

**Excludes:**
- ❌ Project-specific concepts, requirements, parts, assemblies
- ❌ Virtual environments (`cad_env/`)
- ❌ Project-specific logs and data

## 🚀 Quick Start

### Option 1: Double-Click Launcher (Windows)

1. **Double-click** `launch_vmodel_framework_copier.bat` (or `launch_vmodel_framework_copier.ps1`)

### Option 2: Command Line

```bash
python vmodel_framework_copier.py
```

## 📖 How to Use

1. **Launch the application** using one of the methods above

2. **Select Source Project:**
   - Click "Browse..." next to "Source Path"
   - Navigate to your existing V-Model project directory
   - Select the project root folder (the one containing `.cursorrules`)

3. **Select Destination:**
   - Click "Browse..." next to "Destination Path"
   - Navigate to where you want to create the new project
   - Select or create the destination folder

4. **Configure Options:**
   - ✅ **Create empty directory structure** - Creates empty folders for concepts, requirements, design, etc.
   - ✅ **Create README.md** - Creates a README with post-copy setup instructions

5. **Preview Files (Optional):**
   - Click "Preview Files" to see what will be copied before copying

6. **Copy Files:**
   - Click "Copy Template Files"
   - Wait for the copy operation to complete
   - Review the success message

## 📁 What Gets Copied

See `PROJECT_TEMPLATE_FILES.md` for a complete list of files and folders that will be copied.

### Summary:
- **~70 files** including:
  - Core framework files (`.cursorrules`, dashboard files, etc.)
  - Complete `cursorrules_modules/` directory
  - Complete `common_parts/` library
  - Production templates
  - Manufacturing framework templates
  - Requirements templates

- **~15 empty directories** created (if option enabled)

## 🔧 Post-Copy Setup

After copying, you'll need to:

1. **Create Virtual Environment:**
   ```powershell
   python -m venv cad_env
   .\cad_env\Scripts\Activate.ps1
   pip install build123d cadquery cq-warehouse
   ```

2. **Update Project Information:**
   - Edit `generate_dashboard_data.py`
   - Update project name, concept, and description

3. **Initialize Dashboard:**
   ```bash
   python generate_dashboard_data.py
   ```

4. **Start Your Project:**
   - Begin with Phase 1 (Concept) using `@Innovator`
   - Follow the V-Model workflow

## 💾 Configuration

The application saves your last used source and destination paths in:
- Windows: `C:\Users\<YourUsername>\.vmodel_framework_copier.json`

This makes it easier to copy multiple projects from the same source.

## 🐛 Troubleshooting

### "No files found to copy"
- Ensure you selected the correct source directory (should contain `.cursorrules`)
- Check that the source project has the expected structure

### "Directory not empty"
- The destination directory contains files
- Choose a different destination or empty the directory first

### "Permission denied"
- Ensure you have write permissions to the destination directory
- On Windows, try running as administrator if needed

### GUI doesn't appear
- Ensure Python and tkinter are installed
- Test with: `python -c "import tkinter; print('tkinter OK')"`
- On Linux, you may need: `sudo apt-get install python3-tk`

## 📝 Files Created

- `vmodel_framework_copier.py` - Main application (v2.0)
- `PROJECT_TEMPLATE_FILES.md` - Complete list of files to copy
- `launch_vmodel_framework_copier.bat` - Windows batch launcher
- `launch_vmodel_framework_copier.ps1` - PowerShell launcher
- `TEMPLATE_COPIER_README.md` - This file

## 🎯 Features

- ✅ **GUI Interface** - Easy-to-use graphical interface
- ✅ **File Preview** - See what will be copied before copying
- ✅ **Smart Filtering** - Automatically excludes project-specific files
- ✅ **Empty Directory Creation** - Sets up project structure
- ✅ **Progress Indication** - Visual feedback during copy
- ✅ **Error Handling** - Clear error messages
- ✅ **Path Memory** - Remembers last used paths
- ✅ **README Generation** - Creates setup instructions

## 📚 Related Documentation

- `PROJECT_TEMPLATE_FILES.md` - Detailed file list
- `V_MODEL_COMPLETE_GUIDE.html` - Complete workflow guide
- `cursorrules_modules/README.md` - Persona and workflow documentation

---

**Happy Project Starting! 🚀**

