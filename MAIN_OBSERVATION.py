"""Author : Johan Sheby
    Date : 26/12/2025
    Description : A python program that pulls signal strength from a 
    RTL_SDR  and plots it to create
    a radio telescope."""

import os
import sys
import ctypes
import csv
import numpy as np
import time
from datetime import datetime, timezone
from ctypes.util import find_library

# Add RTL-SDR DLL directory to path
dll_path = r"C:\dev\rtl-sdr-64bit-20251221\rtl-sdr-64bit-20251221"
if os.path.exists(dll_path):
    os.add_dll_directory(dll_path)
    sys.path.insert(0, dll_path)
    os.environ['PATH'] = dll_path + os.pathsep + os.environ.get('PATH', '')

from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = (94.3)*(1000000)   # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

# Ask user if they want to save to file
save_to_file = input("Do you want to record data to a spreadsheet file? (yes/no): ").strip().lower() == 'yes'

csv_file = None
csv_writer = None
if save_to_file:
    csv_file = open("signal_data.csv", "w", newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["UTC Time", "Signal Power (dB)"])
    print("Recording to signal_data.csv...")

try:
    reading_count = 0
    # === ADJUST MEASUREMENT INTERVAL HERE (in seconds) ===
    measurement_interval = 0  # Set to 0 for continuous, or any positive number for delay between readings
    # =====================================================
    
    last_reading_time = time.time()
    
    while True:
        current_time = time.time()
        time_since_last_reading = current_time - last_reading_time
        
        # Only read, display, and record at the specified interval
        if measurement_interval == 0 or time_since_last_reading >= measurement_interval:
            # Read samples
            samples = sdr.read_samples(512)
            
            # Calculate power level
            power = np.abs(samples) ** 2
            power_db = 10 * np.log10(power + 1e-10)
            avg_power_db = np.mean(power_db)
            
            # Get UTC time
            utc_time = datetime.now(timezone.utc).isoformat()
            
            # Print power level
            print(f"[{utc_time}] Signal Power: {avg_power_db:.2f} dB")
            
            # Save to file if enabled
            if save_to_file and csv_writer:
                csv_writer.writerow([utc_time, f"{avg_power_db:.2f}"])
                csv_file.flush()
            
            reading_count += 1
            last_reading_time = current_time
        else:
            # Small sleep to prevent CPU spinning when interval > 0
            time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\n\nStopping measurement...")
    if save_to_file and csv_file:
        csv_file.close()
        print(f"Data saved to signal_data.csv ({reading_count} readings)")
finally:
    sdr.close()