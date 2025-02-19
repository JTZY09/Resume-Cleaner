import os
import shutil
import requests
import json
import pdfplumber

import os

# Get the absolute path of the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the folder path
resume_folder = os.path.join(script_dir, "Resume")
pass_folder = os.path.join(script_dir, "Pass")
fail_folder = os.path.join(script_dir, "Fail")



url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
api_key = "AIzaSyDEUHc-RdyLF7tltoG1jUEbPmao-fWvSus" 

    