import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from datetime import datetime
import mutagen
from pathlib import Path
import re


class AudioSessionMatcher:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Session Matcher")
        self.root.geometry("800x600")

        # Store selected files and matched sessions
        self.selected_files = []
        self.matched_sessions = {}

        self.setup_ui()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Drop zone frame
        self.drop_frame = ttk.LabelFrame(
            main_frame, text="Drop Audio Files Here", padding="20"
        )
        self.drop_frame.grid(
            row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10
        )

        drop_label = ttk.Label(
            self.drop_frame, text="Drag and drop files or click to select"
        )
        drop_label.grid(row=0, column=0, pady=20)

       
        self.drop_frame.bind("<Button-1>", self.select_files)

        files_frame = ttk.LabelFrame(main_frame, text="Selected Files", padding="10")
        files_frame.grid(
            row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10
        )

    
        self.files_tree = ttk.Treeview(
            files_frame, columns=("Path", "Date"), show="headings"
        )
        self.files_tree.heading("Path", text="File")
        self.files_tree.heading("Date", text="Date Modified")
        self.files_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar for files list
        files_scroll = ttk.Scrollbar(
            files_frame, orient=tk.VERTICAL, command=self.files_tree.yview
        )
        files_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.files_tree.configure(yscrollcommand=files_scroll.set)

        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=2, column=0, columnspan=2, pady=10)

        ttk.Button(
            buttons_frame, text="Clear Selection", command=self.clear_selection
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            buttons_frame, text="Find Matching Sessions", command=self.find_matches
        ).grid(row=0, column=1, padx=5)

        # Results frame
        results_frame = ttk.LabelFrame(
            main_frame, text="Matched Sessions", padding="10"
        )
        results_frame.grid(
            row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10
        )

        # Treeview for results
        self.results_tree = ttk.Treeview(
            results_frame, columns=("Audio", "Session", "Date"), show="headings"
        )
        self.results_tree.heading("Audio", text="Audio File")
        self.results_tree.heading("Session", text="Session File")
        self.results_tree.heading("Date", text="Date")
        self.results_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar for results
        results_scroll = ttk.Scrollbar(
            results_frame, orient=tk.VERTICAL, command=self.results_tree.yview
        )
        results_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.results_tree.configure(yscrollcommand=results_scroll.set)

        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        files_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(0, weight=1)

    def select_files(self, event=None):
        files = filedialog.askopenfilenames(
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.m4a"),
            ]
        )
        self.add_files(files)

    def add_files(self, files):
        for file in files:
            if file not in self.selected_files:
                self.selected_files.append(file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(file))
                self.files_tree.insert(
                    "",
                    tk.END,
                    values=(file, modified_time.strftime("%Y-%m-%d %H:%M:%S")),
                )

    def clear_selection(self):
        self.selected_files.clear()
        self.files_tree.delete(*self.files_tree.get_children())
        self.results_tree.delete(*self.results_tree.get_children())

    def find_matches(self):
        if not self.selected_files:
            messagebox.showwarning(
                "No Files Selected", "Please select audio files first."
            )
            return

        # Clear previous results
        self.results_tree.delete(*self.results_tree.get_children())

        # Define DAW session file extensions
        daw_extensions = {
            "ptx": "Pro Tools",
            "ptf": "Pro Tools",
            "logic": "Logic",
            "als": "Ableton",
            "flp": "FL Studio",
        }

        # Ask user for directory to search
        search_dir = filedialog.askdirectory(
            title="Select Directory to Search for Session Files"
        )
        if not search_dir:
            return

        for audio_file in self.selected_files:
            audio_time = datetime.fromtimestamp(os.path.getmtime(audio_file))

            # Walk through directory
            for root, dirs, files in os.walk(search_dir):
                for file in files:
                    ext = file.lower().split(".")[-1]
                    if ext in daw_extensions:
                        session_path = os.path.join(root, file)
                        session_time = datetime.fromtimestamp(
                            os.path.getmtime(session_path)
                        )

                        # Check if files were modified within 24 hours of each other
                        time_diff = abs((audio_time - session_time).total_seconds())
                        if time_diff <= 86400:  # 24 hours in seconds
                            self.results_tree.insert(
                                "",
                                tk.END,
                                values=(
                                    os.path.basename(audio_file),
                                    f"{os.path.basename(session_path)} ({daw_extensions[ext]})",
                                    session_time.strftime("%Y-%m-%d %H:%M:%S"),
                                ),
                            )

        if not self.results_tree.get_children():
            messagebox.showinfo(
                "No Matches",
                "No matching session files found within 24 hours of the audio files.",
            )


def main():
    root = tk.Tk()
    app = AudioSessionMatcher(root)
    root.mainloop()


if __name__ == "__main__":
    main()
