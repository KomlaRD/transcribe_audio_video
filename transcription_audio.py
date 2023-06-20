#!/usr/bin/env python3

# Import libraries
import whisper  # Speech-to-text
import torch 
import os # Working with directory
import json # Working with JSON

# -------------------------------------------------
# Function to read instruction file root directory
#--------------------------------------------------
def readInstructionFile():
    """
    Read instruction file
    """
    with open('ins.json', 'r') as ins:
        data = json.load(ins)
    return data

# Read instructions from file
data = readInstructionFile() 
    
# Get root path 
root_path = data["root_path"] 

# List to provide path(s) of videos to be transcribed
audio_paths = [os.path.join(root_path, f) for f in os.listdir(root_path)
               if f.endswith('.mp3')]

# Loop over list of video path
for i, audio_path in enumerate(audio_paths):
    
    # Extract file name from video path
    filename = os.path.basename(audio_path)
    
    # Remove file extension
    filename = os.path.splitext(filename)[0]
    # Check device
    torch.cuda.is_available()
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Load whisper model and transcribe
    model = whisper.load_model("base.en", device=DEVICE)
    print("Transcribing audio...")
    
    # Transcribe audio from Audios directory
    result = model.transcribe(f"{root_path}/{filename}.mp3") 
    print(json.dumps(result["text"], indent=2, ensure_ascii=False)) 
        