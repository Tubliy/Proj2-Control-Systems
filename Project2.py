import matplotlib.pyplot as plt
import numpy as np


def calculate_microphone_intensities(sp, mp):
    """
    Calculate microphone intensities based on the source position.
    Args:
        source_position: (x, y) coordinates of the sound source.
        mic_positions: List of (x, y) coordinates of microphone positions.
    Returns:
        List of intensities for each microphone.
    """
    distances = [np.linalg.norm(np.array(sp) - np.array(mic)) for mic in mp]
    # Inverse square law for intensity (closer microphones have higher intensity)
    intensities = [1 / (d**2 + 1e-6) for d in distances]  # Avoid division by zero
    normalized_intensities = intensities / np.sum(intensities)  # Normalize
    return normalized_intensities


def determine_camera_angle(intensities, mp):
    """
    Determine the camera angle based on microphone intensities.
    Args:
        intensities: List of microphone intensities.
        mic_positions: List of (x, y) coordinates of microphone positions.
    Returns:
        (angle, magnitude): Angle in degrees and magnitude for camera direction.
    """
    sound_source = np.dot(intensities, mp)
    angle = np.degrees(np.arctan2(sound_source[1], sound_source[0]))
    magnitude = np.linalg.norm(sound_source)
    return angle, magnitude


def visualize_camera_direction(room_size, sp, mp, intensities):
    """
    Visualize the room, sound source, microphones, and camera direction.
    Args:
        room_size: Tuple of (width, height) of the room.
        source_position: (x, y) coordinates of the sound source.
        mic_positions: List of (x, y) coordinates of microphone positions.
        intensities: List of microphone intensities.
    """
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


def main():
    # Room dimensions
    room_width = float(input("Enter the room width: "))
    room_height = float(input("Enter the room height: "))
    room_size = (room_width, room_height)

    # Source position
    source_x = float(input("Enter the sound source X position: "))
    source_y = float(input("Enter the sound source Y position: "))
    sp = (source_x, source_y)

    # Microphone positions (corners of the room)
    mp = [
        (-room_width / 2, room_height / 2),  # Front-left
        (room_width / 2, room_height / 2),  # Front-right
        (-room_width / 2, -room_height / 2),  # Back-left
        (room_width / 2, -room_height / 2)  # Back-right
    ]

    # Calculate intensities based on source position
    intensities = calculate_microphone_intensities(sp, mp)

    # Visualize the room, microphones, source, and camera direction
    visualize_camera_direction(room_size, sp, mp, intensities)


if __name__ == "__main__":
    main()
