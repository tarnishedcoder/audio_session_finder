# Audio Session Matcher 🎵

A user-friendly desktop application built with Python and Tkinter for managing and matching audio files to their corresponding Digital Audio Workstation (DAW) session files. Ideal for audio engineers, producers, and hobbyists looking to streamline file organization and enhance workflow.

## ✨ Features

- **Drag & Drop Support**: Easily add audio files to the application for processing
- **File Metadata Display**: View selected audio files and their last modified dates in an organized table
- **DAW Session Matching**: Automatically find DAW session files (e.g., .ptx, .als, .flp) that are timestamped within 24 hours of the selected audio files
- **Custom Search**: Choose a directory to scan for matching DAW session files
- **Clear Results**: Reset selected files and results with a single click
- **Interactive UI**: Built with Tkinter for a clean and intuitive graphical interface

## 📁 Supported File Types

### Audio Files
- `.mp3`
- `.wav`
- `.m4a`

### DAW Session Files
- **Pro Tools**: `.ptx`, `.ptf`
- **Logic Pro**: `.logic`
- **Ableton Live**: `.als`
- **FL Studio**: `.flp`

## 🔍 How It Works

1. Add audio files by dragging and dropping them into the interface or selecting them via a file dialog
2. Use the "Find Matching Sessions" button to search for DAW session files in a specified directory
3. View matched results, including the session file name, corresponding DAW, and modification date, in the results table
4. Clear selections and results to start a new search as needed

## 🚀 Installation

### Clone this repository:
```bash
git clone https://github.com/tarnishedcoder/audio-session-matcher.git
cd audio-session-matcher
```

### Install dependencies:
```bash
pip install mutagen
```

### Run the application:
```bash
python audio_session_matcher.py
```

## 🔮 Future Improvements

- [ ] Add support for more DAW formats
- [ ] Implement a fuzzy matching algorithm for better accuracy
- [ ] Enable exporting matched results to a CSV file
- [ ] Add batch processing capabilities
- [ ] Implement custom time window for matching

## 🤝 Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork this repository
2. Create a new branch for your feature/bug fix:
```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m "Description of your changes"
```
4. Push to your branch:
```bash
git push origin feature-name
```
5. Open a pull request

### Contribution Guidelines
- Write clean, documented code
- Test your changes thoroughly
- Update documentation as needed
- Follow existing code style and conventions
- Include descriptive commit messages

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📫 Support

If you encounter any issues or have questions:
hit me up xdd


---

Made with ❤️ by melik
