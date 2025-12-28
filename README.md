Overview

The workflow is:

Use an RTL-SDR to observe a fixed frequency (or frequency range)

Record signal power levels over time into a CSV file

Process the CSV data

Generate graphs and a heatmap representation of radio intensity across the sky

This project is intended for experimentation, learning, and hobbyist radio astronomy.

Requirements
Hardware

RTL-SDR (RTL2832U-based dongle)

Appropriate antenna for the frequency of interest

Computer (Linux recommended, Windows/macOS may work with driver changes)

Software

RTL-SDR drivers installed

Python 3.x

Required Python libraries (example):

numpy

pandas

matplotlib

Setup

Install RTL-SDR drivers
Ensure the correct drivers are installed for your operating system.

Plug in your RTL-SDR
Verify that the device is detected (e.g., rtl_test on Linux).

Configure scripts
Set the desired frequency, gain, sample rate, and observation duration in the observation script.

How To Use

Make sure you have the correct drivers for your SDR

Plug in your RTL-SDR

Run the observation script to collect power data

Confirm that a CSV file has been created

Run the heatmap script to generate graphs and the sky heatmap

Output

CSV file containing timestamps, frequency information, and power levels

Graphs showing signal power over time

Heatmap visualizing radio intensity across the observed sky region

Notes

Results depend heavily on antenna quality, local interference, and observation time.

For best results, observe away from strong RF noise sources.

This project can be extended to include azimuth/elevation tracking, multiple frequencies, or automated sky scans.

Inspiration

This project was inspired by the radio and electronics experiments featured on the Saveitforparts YouTube channel.
