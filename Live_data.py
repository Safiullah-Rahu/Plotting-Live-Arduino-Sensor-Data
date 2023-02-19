# Import libs
import streamlit as st
import numpy as np
import time
import serial

   
if st.sidebar.button("Show Arduino Live Sensor Data"):
    ser = serial.Serial(port='COM4', baudrate=9600) # write the port at which arduino is connected
    # Initialize an empty numpy array to store data
    data = np.empty((0,2), int)
    chart_data = []
    chart = st.line_chart(chart_data)
    i = 0
    dict = {}
    while True:
        line = ser.readline()
        #chart_data.append(float(data))
        row = np.array([[i, float(line)]])
        data = np.concatenate((row, data), axis=0)
        chart.add_rows(data)
        i += 1
        time.sleep(0.5)
        
