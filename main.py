import tkinter as tk
from tkinter import messagebox  # Import messagebox for user feedback
import random
import time
import csv
from itertools import product

# Global variables
MAX_TRIALS_PER_CONFIG = 10
trial_counter = 0
trial_data = []
current_trial = {}

circle_sizes = [10, 20, 30, 40]
circle_distances = [100, 200, 300, 400]  # Distance from the center
circle_directions = ['left', 'right']  # Circle's direction relative to the center
trial_configurations = list(product(circle_sizes, circle_distances, circle_directions))
random.shuffle(trial_configurations)  # Shuffle the configurations

# Function to check if the click was inside the circle
def is_inside_circle(circle_center, circle_radius, click_point):
    distance = ((click_point[0] - circle_center[0])**2 + (click_point[1] - circle_center[1])**2)**0.5
    return distance <= circle_radius

# Function to handle mouse click
def handle_click(event):
    global current_trial, trial_counter
    click_position = (event.x, event.y)
    
    # Calculate distance between click position and circle center
    distance = ((click_position[0] - current_trial['circle_center'][0])**2 + (click_position[1] - current_trial['circle_center'][1])**2)**0.5
    current_trial['distance'] = distance  # Store the distance in current_trial
    
    if is_inside_circle(current_trial['circle_center'], current_trial['circle_radius'], click_position):
        # Click was inside the circle
        current_trial['time_taken'] = time.time() - current_trial['start_time']
        current_trial['success'] = True
        trial_data.append(current_trial)
        canvas.delete("all")  # Clear the canvas
        messagebox.showinfo("Success", "Well done! Click OK for the next trial.")  # Feedback for successful click
        if trial_counter < len(trial_configurations) * MAX_TRIALS_PER_CONFIG:
            start_trial()
        else:
            end_experiment()
    else:
        # Click was outside the circle, record the error and let the user try again
        current_trial['errors'] += 1
        messagebox.showwarning("Missed", "Oops! You missed. Try again.")  # Feedback for missed click

# Function to start a trial
def start_trial():
    global current_trial, trial_counter, trial_configurations
    canvas.delete("all")  # Clear the canvas
    
    config_index = trial_counter // MAX_TRIALS_PER_CONFIG
    circle_radius, distance_from_center, direction = trial_configurations[config_index]
    
    circle_x = canvas.winfo_width() / 2 + (distance_from_center if direction == 'right' else -distance_from_center)
    circle_y = canvas.winfo_height() / 2

    # Draw the circle
    canvas.create_oval(circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius, fill='blue')

    # Initialize the current trial's data
    current_trial = {
        'circle_radius': circle_radius,
        'circle_center': (circle_x, circle_y),
        'start_time': time.time(),
        'errors': 0,
        'success': False,
        'direction': direction
    }

    trial_counter += 1

# Function to save trial data
def save_data():
    # Define the filename
    filename = "fitts_law_experiment_data.csv"
    # Define the fieldnames
    fieldnames = ['trial', 'circle_radius', 'circle_center_x', 'circle_center_y', 'time_taken', 'distance', 'errors', 'direction']
    # Write data to the CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i, data in enumerate(trial_data):
            writer.writerow({'trial': i+1, 'circle_radius': data['circle_radius'], 'circle_center_x': data['circle_center'][0], 'circle_center_y': data['circle_center'][1], 'time_taken': data['time_taken'], 'distance': data['distance'], 'errors': data['errors'], 'direction': data['direction']})
    print(f"Data saved to {filename}")

# Function to end the experiment
def end_experiment():
    canvas.delete("all")  # Clear the canvas
    save_data()  # Save the data to a file
    show_results()  # Function to display results or provide export option

# Function to show results and end the experiment
def show_results():
    results_window = tk.Tk()
    results_window.title("Experiment Completed")

    results_text = "The experiment is complete. Thank you for your participation!"
    results_label = tk.Label(results_window, text=results_text)
    results_label.pack()

    close_button = tk.Button(results_window, text="Close", command=results_window.destroy)
    close_button.pack()

    results_window.mainloop()

# Function to show the welcome screen
def show_welcome_screen():
    welcome_screen = tk.Tk()
    welcome_screen.title("Welcome to the Fitts' Law Experiment")

    consent_text = """Informed Consent Statement: [Your Consent Text Here]"""
    consent_label = tk.Label(welcome_screen, text=consent_text, wraplength=400)
    consent_label.pack()

    def on_agree():
        # Log or record the consent here
        with open("consent_log.txt", "a") as file:
            file.write(f"Consent given at {time.asctime(time.localtime())}\n")
        welcome_screen.destroy()
        start_experiment()  # Function to initialize the main experiment window

    agree_button = tk.Button(welcome_screen, text="I Agree", command=on_agree)
    agree_button.pack()

    welcome_screen.mainloop()

# Function to start the main experiment
def start_experiment():
    global root, canvas
    root = tk.Tk()
    root.title("Fitts' Law Experiment")

    canvas = tk.Canvas(root, width=800, height=600, bg='white')
    canvas.pack()
    canvas.bind("<Button-1>", handle_click)

    start_button = tk.Button(root, text="Start Experiment", command=start_trial)
    start_button.pack()

    # Add an Abort button to terminate the experiment early
    abort_button = tk.Button(root, text="Abort Experiment", command=end_experiment)
    abort_button.pack()

    root.mainloop()

# Start the application
show_welcome_screen()
