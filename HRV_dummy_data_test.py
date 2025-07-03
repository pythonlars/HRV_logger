import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import medfilt
from scipy import stats
from datetime import datetime

rr_data = np.loadtxt('HRV_dummy_data.txt')
start_time = datetime.now()
meshering_time = input("Please enter meshering time : ")
rmssd_list = []

def clean_data(rr_data):
  cleaned_data = np.empty(len(rr_data))
  
  for i, rr in enumerate(rr_data):
    rr = float(rr*1000)
    if 300<rr<2000:
      cleaned_data[i] = rr
  return cleaned_data

def calculate_metrics(cleaned_data, start_time):
    global rmssd_list, meshering_time
    cleaned_data = np.insert(cleaned_data, 0, start_time)
    diff = np.diff(cleaned_data)
    time_in_seconds = 0
    rr_chunk = []
    for d in diff:
      time_in_seconds += d
      rr_chunk.append(d)
      if time_in_seconds >= int(meshering_time) * 60:
        rmssd = np.sqrt(np.mean(np.array(rr_chunk)**2))
        rmssd_list.append(rmssd)
        time_in_seconds = 0
        rr_chunk = []
    mean_rr = np.mean(cleaned_data)
    hr_bpm = 60000/mean_rr
    