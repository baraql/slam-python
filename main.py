from slam import process
from display import Display
from pointmap import PointMap
# from createCap import createCap

import cv2
import open3d as o3d

import os

pmap = PointMap()
display = Display()

def main():
	# cap = cv2.VideoCapture("videos/test_video3.mp4")
	# cap = createCap("../vis_nav_player/data/images")
	# cap = createCap("../vis_nav_player/data/images")

	pcd = o3d.geometry.PointCloud()
	visualizer = o3d.visualization.Visualizer()
	visualizer.create_window(window_name="3D plot", width=960, height=540)

	# while cap.isOpened():
	# 	ret, frame = cap.read()
	folder_path = "images"
	files = os.listdir(folder_path)

	# Pad filenames with leading zeroes
	files_padded = [f"{int(file.split('.')[0]):03d}.{file.split('.')[1]}" for file in files]

	# Sort the padded filenames
	files_sorted = sorted(files_padded)

	for file in files_sorted:
		# Check if the file is an image (assuming all files in the folder are images)
		if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
			# Read the image
			image = cv2.imread(os.path.join(folder_path, file))
			
			# Check if the image was successfully read
			if image is not None:
				try:
					frame = cv2.resize(image, (960, 540))
					img, tripoints, kpts, matches = process(frame)
					
					xyz = pmap.collect_points(tripoints)

					if kpts is not None or matches is not None:
						display.display_points2d(frame, kpts, matches)
					else:
						pass
					display.display_vid(frame)

					if xyz is not None:
						display.display_points3d(xyz, pcd, visualizer)
					else:
						pass
					if cv2.waitKey(1) == 27:
						break
				except Error as e:
					print(e)

	cv2.destroyAllWindows()
	# cap.release()

if __name__ == '__main__':
	main()
