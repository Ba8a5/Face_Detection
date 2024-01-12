import datetime
import csv
import cv2
import time

# Load a good classifier pre-trained found on Git-hub
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open Webcam
cap = cv2.VideoCapture(0)

# Open CSV in writing mode
with open('faces_detected.csv', mode='a', newline='') as file:
	writer = csv.writer(file, delimiter=';')
	last_nb_faces = 0
	last_detection_time = time.time()
	#1st line
	writer.writerow(['Date', 'Heure', 'Nombre de visages détectés'])

	while True:
		# Read image from webcam
		ret, frame = cap.read()

		# Convert to grayscale for better detection of skin color
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect face(s), recommended with this package (found this advice online)
		faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

		# Number of faces
		nb_faces = len(faces)

		# Date and time
		now = datetime.datetime.now()
		date = now.date().strftime("%Y-%m-%d")
		hms = now.time().strftime("%H:%M:%S")

		if nb_faces != last_nb_faces or time.time() - last_detection_time >= 10:
			last_detection_time = time.time()
			last_nb_faces = nb_faces
		# Writing to CSV
			writer.writerow([date, hms, nb_faces])
			for (x, y, w, h) in faces:
		# Put frames around faces
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# Show frames
		cv2.imshow('Faces detected', frame)


		# Quit
		if cv2.waitKey(1) & 0xFF == ord('x'):
			break

# Close Webcam and destroy frames
cap.release()
cv2.destroyAllWindows()
