# Planning

## Step 1: Data Input
- Read HRV data from a user-provided text file
- Handle missing or malformed data gracefully

## Step 2: Data Cleaning
- Apply a median filter to remove outliers
- Ensure data is in the correct numeric format

## Step 3: Analysis
- Compute RR interval differences
- Calculate HRV metrics (pNN50, RMSSD)
- Prepare data for visualization

## Step 4: Visualization
- Plot Poincaré scatter plot of RR intervals
- Plot histogram of RR interval differences
- Optionally, plot running RMSSD

## Step 5: Output
- Print summary statistics (number of entries, total time, pNN50, RMSSD)
- Save cleaned data if needed
