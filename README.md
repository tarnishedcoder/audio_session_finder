# audio_session_finder

Audio Session Matcher

A user-friendly desktop application built with Python and Tkinter for managing and matching audio files to their corresponding Digital Audio Workstation (DAW) session files. Ideal for audio engineers, producers, and hobbyists looking to streamline file organization and enhance workflow.

Features
Drag & Drop Support: Easily add audio files to the application for processing.
File Metadata Display: View selected audio files and their last modified dates in an organized table.
DAW Session Matching: Automatically find DAW session files (e.g., .ptx, .als, .flp) that are timestamped within 24 hours of the selected audio files.
Custom Search: Choose a directory to scan for matching DAW session files.
Clear Results: Reset selected files and results with a single click.
Interactive UI: Built with Tkinter for a clean and intuitive graphical interface.
Supported File Types
Audio Files: .mp3, .wav, .m4a
DAW Session Files:
Pro Tools: .ptx, .ptf
Logic Pro: .logic
Ableton Live: .als
FL Studio: .flp
How It Works
Add audio files by dragging and dropping them into the interface or selecting them via a file dialog.
Use the Find Matching Sessions button to search for DAW session files in a specified directory.
View matched results, including the session file name, corresponding DAW, and modification date, in the results table.
Clear selections and results to start a new search as needed.
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/your-username/audio-session-matcher.git  
cd audio-session-matcher  
Install dependencies:
bash
Copy code
pip install mutagen  
Run the application:
bash
Copy code
python audio_session_matcher.py  
Future Improvements
Add support for more DAW formats.
Implement a fuzzy matching algorithm for better accuracy.
Enable exporting matched results to a CSV file.
