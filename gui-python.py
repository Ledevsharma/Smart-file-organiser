import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit
from PyQt6.QtCore import Qt
from organizer import organize_directory  # Importing your core engine!

class OrganizerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window setup
        self.setWindowTitle('Smart File Organizer')
        self.resize(550, 450)
        self.setStyleSheet("background-color: #121212; color: #ffffff;") # Dark mode background

        layout = QVBoxLayout()

        # 1. Title
        self.title_label = QLabel("🧠 Smart File Organizer")
        self.title_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #39ff14; padding: 10px;") # Neon green
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.title_label)

        # 2. Selected Folder Display
        self.folder_label = QLabel("Status: Waiting for folder selection...")
        self.folder_label.setStyleSheet("color: #aaaaaa; font-size: 14px; font-style: italic;")
        self.folder_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.folder_label)

        # 3. Browse Button
        self.btn_browse = QPushButton("📁 Select Folder to Organize")
        self.btn_browse.setStyleSheet("""
            QPushButton {
                background-color: #2a2a2a; 
                padding: 12px; 
                font-size: 16px; 
                border-radius: 5px;
                border: 1px solid #39ff14;
            }
            QPushButton:hover { background-color: #333333; }
        """)
        self.btn_browse.clicked.connect(self.browse_folder)
        layout.addWidget(self.btn_browse)

        # 4. Run Button
        self.btn_run = QPushButton("🚀 Run Smart Organizer")
        self.btn_run.setStyleSheet("""
            QPushButton {
                background-color: #39ff14; 
                color: #000000; 
                padding: 12px; 
                font-size: 16px; 
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:disabled { background-color: #2a2a2a; color: #555555; }
        """)
        self.btn_run.clicked.connect(self.run_organizer)
        self.btn_run.setEnabled(False) # Disabled until a folder is picked
        layout.addWidget(self.btn_run)

        # 5. Console Output Log
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet("""
            background-color: #0a0a0a; 
            color: #39ff14; 
            font-family: Consolas, monospace; 
            border: 1px solid #333333;
            padding: 5px;
        """)
        self.log_output.append("System initialized. Awaiting user input...\n")
        layout.addWidget(self.log_output)

        self.setLayout(layout)
        self.target_folder = ""

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory to Clean")
        if folder:
            self.target_folder = folder
            self.folder_label.setText(f"Target: {self.target_folder}")
            self.btn_run.setEnabled(True)
            self.log_output.append(f"[INFO] Target directory set to: {self.target_folder}")

    def run_organizer(self):
        self.log_output.append("\n[PROCESSING] Starting organization protocol...")
        self.btn_run.setEnabled(False) # Prevent clicking twice
        self.repaint() # Force UI to update before running the heavy task
        
        try:
            # Call the logic from organizer.py
            organize_directory(self.target_folder)
            
            self.log_output.append("[SUCCESS] Organization Complete!")
            self.log_output.append("Check your folder to see the categorized files.")
        except Exception as e:
            self.log_output.append(f"[ERROR] {str(e)}")
        
        self.btn_run.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OrganizerGUI()
    ex.show()
    sys.exit(app.exec())