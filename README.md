# HCI

# Fitts' Law Experiment Application

### Developed by:
- **Biruk Anley** – biruk.anley@mnsu.edu  
- **Melan Shifa** – melan.shifa@mnsu.edu  
- **Eyouel Aregahegn** – eyouel.aregahegn@mnsu.edu  
- **Tebibu Kebede** – tebibu.kebede@mnsu.edu  
- **Ahmed Umer** – ahmed.umer@mnsu.edu  

---

## 📘 Overview
The **Fitts’ Law Experiment Application** is a Human-Computer Interaction (HCI) research tool designed to study and measure the efficiency of users when pointing and clicking on targets at various sizes and distances on a screen.

Based on **Fitts’ Law**, which predicts the time required to move to and select a target area, this application records user performance across randomized trials and generates experiment data for analysis of **speed**, **accuracy**, and **error rates**.

This project was developed as part of the **CS470 – Human-Computer Interaction** course at **Minnesota State University, Mankato**.

---

## 🎯 Objective
The goal of this experiment is to empirically evaluate Fitts' Law by examining how target **size** and **distance** affect user performance.  
Participants are asked to click on blue circles displayed at random positions on the screen.  
Performance metrics such as **movement time**, **distance**, and **error count** are recorded for statistical analysis.

---

## ⚙️ Features
- **Interactive GUI** built using Tkinter for real-time user interaction.
- **Automated trial generation** with randomized target sizes, distances, and positions.
- **Data collection and logging** of each trial’s results to a CSV file for later analysis.
- **User feedback system** with success and miss prompts.
- **Informed consent screen** to ensure participants agree to terms before starting.
- **Automated cursor repositioning** using PyAutoGUI for controlled experiments.
- **Configurable parameters** (e.g., number of trials, circle sizes, distances).
- **Data persistence** — appends results from multiple participants into one file.

---

## 🧮 Data Collected
For every trial, the following data points are recorded:

| Field | Description |
|-------|-------------|
| `trial` | Trial number |
| `circle_radius` | Radius of the target circle (px) |
| `circle_center_x`, `circle_center_y` | Target center coordinates |
| `time_taken` | Time (in seconds) taken to successfully click the target |
| `distance` | Distance between click and target center |
| `errors` | Number of misses before success |
| `direction` | Direction of movement (left/right/random) |
| `success` | Boolean indicating success or miss |
| `start_time` | Timestamp of the trial start |

All results are stored in a CSV file located on the user’s desktop as:
