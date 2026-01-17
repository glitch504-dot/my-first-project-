# ping_gui.py - A GUI app to ping an IP address
import tkinter as tk
from tkinter import ttk
import subprocess
import platform
import threading

def ping_ip():
    """Ping the IP address and show the result."""
    ip = ip_entry.get().strip()

    if not ip:
        result_label.config(text="Please enter an IP address", foreground="orange")
        return

    # Disable button and show "Pinging..."
    ping_button.config(state="disabled")
    result_label.config(text="Pinging...", foreground="blue")
    window.update()

    # Run ping in a thread so GUI doesn't freeze
    def do_ping():
        flag = "-n" if platform.system().lower() == "windows" else "-c"
        try:
            result = subprocess.run(
                ["ping", flag, "2", ip],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                result_label.config(text="Ping Successful!", foreground="green")
            else:
                result_label.config(text="Ping Unsuccessful!", foreground="red")
        except subprocess.TimeoutExpired:
            result_label.config(text="Ping Timed Out!", foreground="red")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}", foreground="red")
        finally:
            ping_button.config(state="normal")

    threading.Thread(target=do_ping, daemon=True).start()

# Create the main window
window = tk.Tk()
window.title("Ping Tool")
window.geometry("350x180")
window.resizable(False, False)

# Create a frame for padding
frame = ttk.Frame(window, padding="20")
frame.pack(fill="both", expand=True)

# Label for instruction
instruction_label = ttk.Label(frame, text="Enter IP Address:")
instruction_label.pack(pady=(0, 5))

# Entry field for IP address
ip_entry = ttk.Entry(frame, width=30, font=("Arial", 12))
ip_entry.pack(pady=(0, 10))
ip_entry.insert(0, "1.1.1.1")  # Default value

# Ping button
ping_button = ttk.Button(frame, text="Ping", command=ping_ip)
ping_button.pack(pady=(0, 15))

# Result label
result_label = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Allow pressing Enter to ping
ip_entry.bind("<Return>", lambda e: ping_ip())

# Start the GUI
window.mainloop()
