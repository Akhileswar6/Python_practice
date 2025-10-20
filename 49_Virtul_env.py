# A virtual environment is an isolated Python environment that allows you to manage dependencies for each project separately. It prevents conflicts between projects and avoids affecting the system-wide Python installation.

# How to Create a Virtual Environment in Python
# We use the virtualenv module to create isolated environments. It creates a folder with all necessary executables for the project.

# Step 1: Installing virtualenv
"""$ pip install virtualenv"""

# Step 2: Check Installation
"""$ virtualenv --version"""

# Step 3: Create a Virtual Environment
"""$ virtualenv my_env"""


# Activating a Virtual Environment in Python

# 1. On Windows
"""cd <envname> Scripts\activate"""

# 2. On Linux/macOS
"""$ source virtualenv_name/bin/activate"""


# Installing Dependencies in Virtual Environment

# For example, to install Django 1.9:
"""(virtualenv_name)$ pip install Django==1.9"""


# Deactivate Python Virtual Environment
"""(virtualenv_name)$ deactivate"""

