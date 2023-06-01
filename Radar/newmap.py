import pygame
import math
import time
import sys

# Initialize the Pygame library
pygame.init()

# Set the size of the game window
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Set the title of the game window
pygame.display.set_caption("Radar")

# Define the colors used in the program
background_color = (0, 0, 0)      # Black
line_color = (0, 255, 0)          # Green
dot_color = (255, 0, 0)           # Red
text_color = (255, 255, 255)      # White
button_color = (0, 0, 0)          # Black

# Define the properties of the radar
radar_radius = 400
center_x = width // 2
center_y = height

# Set up the font for text display
font = pygame.font.Font(None, 15)

# Define the file path where the radar data is stored
file_path = "C:/Users/Philip/Desktop/data.txt"

# Function to update the radar values from the file
def update_values():
    with open(file_path, "r") as file:
        # Read lines from the file and remove any leading or trailing whitespace
        lines = [line.strip() for line in file if line.strip()]

    # Declare global variables that will be used to store the radar values
    global current_distance, current_line_index, detected_objects

    # Check if there are more lines to read from the file
    if current_line_index < len(lines):
        line = lines[current_line_index]
        # Extract the numeric part from the line (digits only)
        numeric_part = ''.join(c for c in line if c.isdigit())
        # Convert the numeric part to an integer, or set it to 0 if no digits were found
        current_distance = int(numeric_part) if numeric_part else 0
        # Ensure that the current distance does not exceed the radar radius
        current_distance = min(current_distance, radar_radius)
        # Move to the next line in the file
        current_line_index = (current_line_index + 1) % len(lines)
        # Pause the program for a short time to simulate real-time updates
        time.sleep(0.1)

        # Check if an object already exists at the current angle
        existing_object = None
        for obj in detected_objects:
            if obj[0] == current_angle:
                existing_object = obj
                break

        # If an object already exists at the current angle, update its distance
        if existing_object:
            existing_object[1] = current_distance
        # Otherwise, add a new object to the detected_objects list
        else:
            detected_objects.append([current_angle, current_distance])

# Function to draw the radar display on the screen
def draw_radar():
    # Fill the entire screen with the background color (black)
    screen.fill(background_color)
    # Draw the outer circle of the radar
    pygame.draw.circle(screen, line_color, (center_x, center_y), radar_radius, 1)

    # Divide the radar into multiple concentric circles to represent different distances
    num_lines = 10
    distance_interval = radar_radius // num_lines
    for i in range(1, num_lines + 1):
        distance = i * distance_interval
        line_radius = int(radar_radius * distance / radar_radius)
        # Draw each circle with increasing radius
        pygame.draw.circle(screen, line_color, (center_x, center_y), line_radius, 1)
        # Display the distance labels at the corresponding circles
        draw_text(str(distance) + "cm", center_x + line_radius, center_y - 15)

    # Calculate the coordinates of the line indicating the current angle
    line_x = center_x + radar_radius * math.cos(math.radians(current_angle))
    line_y = center_y - radar_radius * math.sin(math.radians(current_angle))
    # Draw the line from the center to the current angle
    pygame.draw.line(screen, line_color, (center_x, center_y), (line_x, line_y), 2)

    # Draw dots on the radar to represent detected objects
    dot_radius = 5
    for obj in detected_objects:
        obj_angle, obj_distance = obj
        # Check if the object angle is within the desired range (0 to 180 degrees)
        if 0 <= obj_angle <= 180:
            # Calculate the coordinates of the dot based on the object angle and distance
            dot_angle = math.radians(obj_angle)
            dot_x = center_x + obj_distance / radar_radius * radar_radius * math.cos(dot_angle)
            dot_y = center_y - obj_distance / radar_radius * radar_radius * math.sin(dot_angle)
            # Draw a circle at the calculated coordinates
            pygame.draw.circle(screen, dot_color, (int(dot_x), int(dot_y)), dot_radius)

    # Display text on the screen to show the current angle and distance
    draw_text("Angle: " + str(current_angle) + "°", 20, 20)
    if current_distance:
        draw_text("Distance: " + str(current_distance) + "cm", 20, 40)

# Function to render and display text on the screen
def draw_text(text, x, y, color=text_color):
    # Render the text using the specified font, with antialiasing and the specified color
    text_surface = font.render(text, True, color)
    # Blit (draw) the rendered text onto the screen at the specified position (x, y)
    screen.blit(text_surface, (x, y))

# Function to draw the close button on the screen
def draw_close_button():
    button_width, button_height = 20, 20
    button_x, button_y = 10, height - button_height - 10
    # Draw a rectangle for the button using the button color
    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))
    # Display the "Close" label at the center of the button
    draw_text("Close", button_x + button_width // 2, button_y + button_height // 2, text_color)

# Function to check if the button is clicked
def is_button_clicked(pos):
    button_width, button_height = 60, 20
    button_x, button_y = 10, height - button_height - 10
    # Check if the click position is within the button's boundaries
    return button_x < pos[0] < button_x + button_width and button_y < pos[1] < button_y + button_height

# Initialize variables and clock
detected_objects = []       # List to store the detected objects
current_angle = 0          # Variable to store the current angle
current_distance = 0       # Variable to store the current distance
current_line_index = 0     # Variable to keep track of the current line in the file
direction = 1              # Variable to control the direction of angle rotation

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        # Check if the left mouse button was clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if the click position is within the close button boundaries
                if is_button_clicked(event.pos):
                    running = False
                    pygame.quit()
                    sys.exit()

    # Update the radar values from the file
    update_values()

    # Update the current angle and direction
    current_angle += direction
    if current_angle <= 0 or current_angle >= 180:
        direction *= -1

    # Draw the radar display and close button on the screen
    draw_radar()
    draw_close_button()
    
    # Update the display and limit the frame rate to 60 FPS
    pygame.display.flip()
    clock.tick(60)
