import cv2
import os

# Folder containing the images
folder_path = "images"

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Sort the files to ensure they are processed in order
files.sort()

# Loop through each file in the folder
for file in files:
    # Check if the file is an image (assuming all files in the folder are images)
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        # Read the image
        image = cv2.imread(os.path.join(folder_path, file))
        
        # Display the image
        cv2.imshow("Image", image)
        
        # Wait for a key press to display the next image
        # Press any key to display the next image
        cv2.waitKey(0)

# Release resources
cv2.destroyAllWindows()
