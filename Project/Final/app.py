import os
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class RomAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ROM-Scan Analyzer System v1.0")
        self.root.geometry("850x500")
        self.root.minsize(800, 400)
        
      
        self.supported_extensions = {'.nes', '.sfc', '.smc', '.gba', '.bin', '.rom'}
        
        self._build_ui()

    def _build_ui(self):
        
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill=tk.X)
        
        self.path_entry = ttk.Entry(top_frame, font=("Segoe UI", 10))
        self.path_entry.insert(0, "Specify directory path for game collection scanning...")
        self.path_entry.bind("<FocusIn>", lambda e: self.path_entry.delete(0, tk.END) if "Specify directory" in self.path_entry.get() else None)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        ttk.Button(top_frame, text="Browse Folder", command=self._browse_folder).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Execute Scan", command=self._start_scan_thread).pack(side=tk.LEFT, padx=5)

        
        control_frame = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        control_frame.pack(fill=tk.X)
        
        self.status_label = ttk.Label(control_frame, text="Library State: Idle (Awaiting User Input)", foreground="#4a5568")
        self.status_label.pack(side=tk.LEFT)

      
        table_frame = ttk.Frame(self.root, padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("name", "platform", "size")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("name", text="Identified File Name")
        self.tree.heading("platform", text="Emulated Console Platform")
        self.tree.heading("size", text="Size (MB)")
        
        self.tree.column("name", width=300, anchor=tk.W)
        self.tree.column("platform", width=150, anchor=tk.W)
        self.tree.column("size", width=120, anchor=tk.E)
        
        # Add a scrollbar for navigating up to 10,000 file entries smoothly
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _browse_folder(self):
        selected_dir = filedialog.askdirectory()
        if selected_dir:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, selected_dir)

    def _start_scan_thread(self):
        target_dir = self.path_entry.get().strip()
        if not target_dir or not os.path.isdir(target_dir):
            messagebox.showwarning("Execution Fault", "The target destination path parameter is invalid.")
            return
            
        self.status_label.config(text="Library State: Parsing Directories...")
        # Running the engine inside a background thread keeps the GUI completely fluid
        threading.Thread(target=self._execute_scan, args=(target_dir,), daemon=True).start()

    def _execute_scan(self, target_dir):
        # Clear existing table data rows smoothly
        self.root.after(0, lambda: self.tree.delete(*self.tree.get_children()))
        
        file_counter = 0
        discovered_entries = []
        
        try:
            # EnumerateFiles pattern protects system heap bounds against memory spikes
            for root, _, files in os.walk(target_dir):
                for file in files:
                    file_counter += 1
                    if file_counter > 100:
                        raise BufferError("System safe boundary exceeded: directory tree contains over 100 entities.")
                    
                    ext = os.path.splitext(file)[1].lower()
                    if ext in self.supported_extensions:
                        full_path = os.path.join(root, file)
                        parent_folder = os.path.basename(root).lower()
                        
                        platform = self._resolve_platform(parent_folder)
                        file_size_mb = os.path.getsize(full_path) / (1024 * 1024)
                        
                        discovered_entries.append((file, platform, f"{file_size_mb:.2f} MB"))

            # Push results safely back onto the main loop thread UI elements
            self.root.after(0, self._update_ui_results, discovered_entries, f"Library State: Verified {len(discovered_entries)} game entries successfully.")

        except BufferError as err:
            self.root.after(0, lambda: messagebox.showerror("Memory Buffer Overrun Safety Fault", str(err)))
            self.root.after(0, lambda: self.status_label.config(text="Library State: Scan Fault Encountered."))
        except Exception as ex:
            self.root.after(0, lambda: messagebox.showerror("Unexpected Runtime Exception", f"Process halted: {str(ex)}"))

    def _resolve_platform(self, parent_folder):
        """Resolves the console platform from the parent directory name."""
        if parent_folder == "fc" or parent_folder == "nes": return "Nintendo NES"
        if parent_folder == "snes": return "Super Nintendo"
        if parent_folder == "gba": return "Game Boy Advance"
        return "Unknown / Unverified"

    def _update_ui_results(self, entries, status_text):
        for item in entries:
            self.tree.insert("", tk.END, values=item)
        self.status_label.config(text=status_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = RomAnalyzerApp(root)
    root.mainloop()
