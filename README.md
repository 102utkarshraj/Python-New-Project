# 🌍 Real-Time Air Quality Analysis Dashboard 🏙️

Welcome to the **Real-Time Air Quality Analysis** project! This repository contains Python-based data analysis and visualization scripts to uncover insights from air pollution data collected from various Indian cities.

---

## 📦 Project Overview

This project focuses on exploring, cleaning, and visualizing real-time **Air Quality Index (AQI)** data. It helps in identifying pollution patterns, comparing city-wise stats, and mapping geospatial pollution intensity — all with the power of **Python**, **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 🎯 Objectives of the Analysis

### 1️⃣ Preview & Understand the Dataset  
🔍 Display the first few rows, structure, and summary statistics.  
🧹 Identify missing values and data types to assess data quality.

### 2️⃣ Data Cleaning  
🧽 Handle missing values by dropping rows with null pollutant readings.  
🗺️ Create binned geographic variables (`lat_bin`, `lon_bin`) for geospatial visualization.

### 3️⃣ Univariate Analysis  
📈 Plot **KDE (Kernel Density Estimate)** of average pollutant levels.  
📊 Generate a **histogram** to understand AQI distribution.

### 4️⃣ City-wise Pollution Comparison  
📦 Use **box plots** to compare maximum pollution levels across top cities.  
🚩 Highlight cities with extreme outliers and variability.

### 5️⃣ Geospatial Distribution  
🌐 Bin locations by latitude and longitude.  
🔥 Use **heatmaps** to visualize pollution intensity across regions.

### 6️⃣ Pollutant Type Breakdown  
🥧 Create a **pie chart** showing the share of different pollutant types (`pollutant_id`).

### 7️⃣ Pollution Level Relationship  
🧮 Use **scatter plots** and **regression lines** to analyze the relationship between min and max pollutant levels.

### 8️⃣ Sensor-Level Granularity  
🎻 Create **violin plots** to explore the distribution of pollutant readings by city.

### 9️⃣ Visual Correlation of Geo Data  
📍 Analyze the impact of **latitude and longitude** using bar charts and heatmaps.

### 🔟 Highlight High-Density Regions  
📊 Detect geographic zones with consistently high pollution using binning & aggregation.

---

## 💾 Dataset

📄 **Source**: [data.gov.in](https://data.gov.in)  
🧪 **Format**: CSV  
📍 **Fields**: City, Pollutant Type, Pollutant Max/Min/Avg, Latitude, Longitude, Timestamp, etc.

---

## 📌 Dependencies

