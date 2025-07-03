# HRV Data Analysis

This project provides tools for reading, cleaning, and analyzing Heart Rate Variability (HRV) data from a text file. It includes basic statistics, visualization (Poincaré plot, histogram), and RMSSD computation.

## Features
- Read HRV data from a text file
- Clean data using a median filter
- Compute RR interval statistics (pNN50, RMSSD, etc.)
- Visualize data with plots

## Requirements
- Python 3.x
- numpy
- matplotlib
- pandas
- scipy

## Usage
1. Place your HRV data in a text file (one value per line).
2. Adjust the filename in `HRV_dummy_data_test.py` if needed.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the script: `python HRV_dummy_data_test.py`

## Output
- Console output with HRV statistics
- Plots for data visualization
