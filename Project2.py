import matplotlib.pyplot as plt
import numpy as np
import time


def calculate_microphone_intensities(sp, mp):
    
    distances = [np.linalg.norm(np.array(sp) - np.array(mic)) for mic in mp]
    # Inverse square law for intensity (closer microphones have higher intensity)
    intensities = [1 / (d**2 + 1e-6) for d in distances]  # Avoid division by zero
    normalized_intensities = intensities / np.sum(intensities)  # Normalize
    return normalized_intensities


def determine_camera_angle(intensities, mp):
   
    sound_source = np.dot(intensities, mp)
    angle = np.degrees(np.arctan2(sound_source[1], sound_source[0]))
    magnitude = np.linalg.norm(sound_source)
    return angle, magnitude


def visualize_camera_direction(room_size, sp, mp, intensities):
   
    angle, magnitude = determine_camera_angle(intensities, mp)
    width, height = room_size

    plt.figure(figsize=(8, 8))

    # Plot microphone positions
    for i, mic in enumerate(mp):
        plt.scatter(mic[0], mic[1], color='blue', label=f'Mic {i+1} (Intensity: {intensities[i]:.2f})')
        plt.text(mic[0], mic[1] + 0.2, f'Mic {i+1}', fontsize=10, ha='center')

    # Plot sound source
    plt.scatter(sp[0], sp[1], color='purple', label='Sound Source')
    plt.text(sp[0], sp[1] + 0.2, 'Source', fontsize=10, ha='center')

    # Plot camera direction
    x, y = magnitude * np.cos(np.radians(angle)), magnitude * np.sin(np.radians(angle))
    plt.arrow(0, 0, x, y, head_width=0.5, head_length=0.5, fc='green', ec='green', label='Camera Direction')

    # Set plot limits and labels
    plt.xlim(-width / 2, width / 2)
    plt.ylim(-height / 2, height / 2)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Camera Direction Based on Sound Source and Microphone Inputs")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


def feedback_loop(room_size, mp, initial_sp, iterations=10, delay=1):
   
    current_sp = initial_sp  # Start with the initial position
    
    for i in range(iterations):
        print(f"Iteration {i+1}:")
        
        # Calculate microphone intensities
        intensities = calculate_microphone_intensities(current_sp, mp)
        
        # Determine camera direction
        angle, magnitude = determine_camera_angle(intensities, mp)
        print(f"Camera Direction: Angle = {angle:.2f}°, Magnitude = {magnitude:.2f}")
        
        # Visualize the current state
        visualize_camera_direction(room_size, current_sp, mp, intensities)
        
        # Simulate sound source movement (e.g., move right by 1 unit)
        current_sp = (current_sp[0] + 1, current_sp[1])  # Change this to customize movement
        
        time.sleep(delay)  # Wait for the next update


def main():
    # Room dimensions
    room_width = float(input("Enter the room width: "))
    room_height = float(input("Enter the room height: "))
    room_size = (room_width, room_height)

    # Initial source position
    source_x = float(input("Enter the initial sound source X position: "))
    source_y = float(input("Enter the initial sound source Y position: "))
    initial_sp = (source_x, source_y)

    # Microphone positions (corners of the room)
    mp = [
        (-room_width / 2, room_height / 2),  # Front-left
        (room_width / 2, room_height / 2),  # Front-right
        (-room_width / 2, -room_height / 2),  # Back-left
        (room_width / 2, -room_height / 2)  # Back-right
    ]

    # Simulate feedback loop
    iterations = int(input("Enter the number of iterations for the feedback loop: "))
    delay = float(input("Enter the delay (in seconds) between iterations: "))
    feedback_loop(room_size, mp, initial_sp, iterations, delay)


if __name__ == "__main__":
    main()
