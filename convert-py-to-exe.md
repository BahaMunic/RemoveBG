# Steps to Convert a Python File to an EXE File

## 1. Install PyInstaller
- Open Command Prompt.
- Execute the command:
  pip install pyinstaller

## 2. Navigate to the Project Folder
- Use the cd command to navigate to the folder containing your Python file. For example:
  cd C:\path\to\your\project

## 3. Create the EXE File
- To create a simple EXE file, use:
  pyinstaller your_script.py
- To create an EXE file with a graphical interface, use:
  pyinstaller --windowed --onefile your_script.py

## 4. Find the EXE File
- After completion, look in the dist folder for the resulting EXE file.

## 5. Test the EXE File
- Open the dist folder and click on the EXE file to ensure it works correctly.

# Steps to Convert a Python File to an EXE File Using Auto Py to Exe

## 1. Install Auto Py to Exe
- Open Command Prompt.
- Execute the command:
  pip install auto-py-to-exe

## 2. Run Auto Py to Exe
- Type in the Command Prompt:
  auto-py-to-exe

## 3. Set Up the Project
- In the Auto Py to Exe interface:
  - Select the Python File: Click the "Browse" button to choose your .py file.
  - Select the Execution Type: 
    - Choose "One File" to convert the program into a single EXE file.
    - Make sure to select "Windowed" if you want to run the application without a console window.

## 4. Select an Icon (Optional)
- If you want to set an icon, you can do so through the "Icon" option.

## 5. Add Additional Files (Optional)
- If you have files to include, you can add them in the "Additional Files" section.

## 6. Configure Settings
- Check the remaining settings, and you can leave them at the default values if you are a beginner.

## 7. Create the EXE File
- After finishing the settings, click the "Convert .py to .exe" button.
- Wait for the conversion to complete.

## 8. Find the EXE File
- After completion, the EXE file will be created in the specified output folder.

## 9. Test the EXE File
- Open the folder containing the EXE file and click on it to ensure it works correctly.
