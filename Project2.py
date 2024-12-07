import matplotlib.pyplot as plt
import numpy as np
import time


def estimate_source_position(mp, intensities):
    # Weighted centroid formula: Position = Σ(intensity * mic_position) / Σ(intensity)
    weighted_positions = np.array([intensity * np.array(mic) for intensity, mic in zip(intensities, mp)])
    source_position = np.sum(weighted_positions, axis=0) / np.sum(intensities)
    return source_position


def calculate_microphone_intensities(mp, sp_estimate):
    # Use the inverse square law to estimate intensities
    distances = [np.linalg.norm(np.array(sp_estimate) - np.array(mic)) for mic in mp]
    intensities = [1 / (d**2 + 1e-6) for d in distances]  # Avoid division by zero
    normalized_intensities = intensities / np.sum(intensities)  # Normalize
    return normalized_intensities


def visualize_camera_direction(room_size, mp, intensities, sp_estimate, true_sp):

    width, height = room_size
    camera_position = (0, 0)  # Camera is at the center of the room

    # Calculate camera pointing direction
    dx, dy = sp_estimate[0] - camera_position[0], sp_estimate[1] - camera_position[1]
    angle = np.degrees(np.arctan2(dy, dx))  # Angle in degrees for camera orientation

    plt.figure(figsize=(8, 8))

    # Plot microphone positions
    for i, mic in enumerate(mp):
        plt.scatter(mic[0], mic[1], color='blue', label=f'Mic {i+1}' if i == 0 else None)
        plt.text(mic[0], mic[1] + 0.2, f'Mic {i+1} (Intensity: {intensities[i]:.2f})', fontsize=10, ha='center')

    # Plot estimated source position
    plt.scatter(sp_estimate[0], sp_estimate[1], color='purple', label='Estimated Source')
    plt.text(sp_estimate[0], sp_estimate[1] + 0.2, 'Estimated', fontsize=10, ha='center')

    # Plot true source position
    plt.scatter(true_sp[0], true_sp[1], color='orange', label='True Source')
    plt.text(true_sp[0], true_sp[1] + 0.2, 'True', fontsize=10, ha='center')

    # Plot camera position
    plt.scatter(camera_position[0], camera_position[1], color='red', label='Camera')
    plt.arrow(
        camera_position[0], camera_position[1], 
        2 * np.cos(np.radians(angle)), 2 * np.sin(np.radians(angle)),  # Camera direction
        head_width=0.5, head_length=0.5, fc='green', ec='green', label='Camera Direction'
    )

    # Set plot limits and labels
    plt.xlim(-width / 2, width / 2)
    plt.ylim(-height / 2, height / 2)
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
    plt.title("Camera Direction Based on Estimated Sound Source and Microphone Inputs")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


def feedback_loop(room_size, mp, true_sp, iterations=10, delay=1):
    
    sp_estimate = (0, 0)  # Start with an initial guess for the source position

    for i in range(iterations):
        print(f"Iteration {i+1}:")

        # Simulate microphone intensities based on true source position
        intensities = calculate_microphone_intensities(mp, true_sp)

        # Estimate source position based on the intensities
        sp_estimate = estimate_source_position(mp, intensities)

        # Print estimated and true source positions
        print(f"Estimated Source Position: X = {sp_estimate[0]:.2f}, Y = {sp_estimate[1]:.2f}")
        print(f"True Source Position: X = {true_sp[0]:.2f}, Y = {true_sp[1]:.2f}")

        # Visualize the current state
        visualize_camera_direction(room_size, mp, intensities, sp_estimate, true_sp)

        # Simulate movement of the true source (e.g., move right by 1 unit)
        true_sp = (true_sp[0] + 1, true_sp[1])  # Update true source position

        time.sleep(delay)  # Wait for the next update


def main():
    # Room dimensions
    room_width = float(input("Enter the room width: "))
    room_height = float(input("Enter the room height: "))
    room_size = (room_width, room_height)

    # Initial true source position
    source_x = float(input("Enter the initial sound source X position: "))
    source_y = float(input("Enter the initial sound source Y position: "))
    true_sp = (source_x, source_y)

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
    feedback_loop(room_size, mp, true_sp, iterations, delay)


if __name__ == "__main__":
    main()
