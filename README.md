A best practice among Python developers is to avoid installing packages into a global interpreter environment. You instead use a project-specific virtual environment that contains a copy of a global interpreter. Once you activate that environment, any packages you then install are isolated from other environments. Such isolation reduces many complications that can arise from conflicting package versions. To create a virtual environment and install the required packages, enter the following commands as appropriate for your operating system:

**Note:** For additional information about virtual environments, see [Environments](https://code.visualstudio.com/docs/python/environments#_creating-environments).

1. Create a virtual environment using the _Create Environment_ command\
   \
   From within VS Code, you can create non-global environments, using Venv or Anaconda, by opening the Command Palette (Ctrl+Shift+P), start typing the Python: Create Environment command to search, and then select the command. You can also trigger the Python: Create Environment command through the Getting Started with Python page.
   \
   The command presents a list of environment types, Venv or Conda. For this example, select **Venv**.
   \
   ![Select an Environment type screenshot](https://code.visualstudio.com/assets/docs/python/environments/create_environment_dropdown.png)
   \
   The command then presents a list of interpreters that can be used for your project.
   \
   ![Virtual environment interpreter selection](https://code.visualstudio.com/assets/docs/python/environments/interpreters-list.png)
   \
   After selecting the desired interpreter, a notification will show the progress of the environment creation and the environment folder will appear in your workspace.
   \
   ![Create environment status notification](https://code.visualstudio.com/assets/docs/python/environments/create_environment_prompt_status.png)
   \
   The command will also install necessary packages outlined in a requirements/dependencies file, such as requirements.txt, pyproject.toml, or environment.yml, located in the project folder.
   \
   Note: If you want to create an environment manually, or run into error in the environment creation process, visit the Environments page.

1. Ensure your new environment is selected by using the Python: Select Interpreter command from the Command Palette.
   \
   ![Select an Interpreter](https://code.visualstudio.com/assets/docs/python/tutorial/interpreter-venv.png)
   \
1. Install the packages (eg)

```python
# Don't use with Anaconda distributions because they include matplotlib already.

# macOS
python3 -m pip install matplotlib

# Windows (may require elevation)
py -m pip install matplotlib

# Linux (Debian)
apt-get install python3-tk
python3 -m pip install matplotlib
```

### **WARNING**: Don't use with Anaconda distributions because they include matplotlib already.

## macOS

python3 -m pip install matplotlib

## Windows (may require elevation)

py -m pip install matplotlib

## Linux (Debian)

apt-get install python3-tk
python3 -m pip install matplotlib
