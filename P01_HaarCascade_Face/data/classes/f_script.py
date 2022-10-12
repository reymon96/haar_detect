class ALGORITM_HAAR():

	def import_haar(cv2, route):
		return (cv2.CascadeClassifier(route));
	#END

	def detect_face(cv2, haar, frame):
		
		rects	= haar.detectMultiScale(
			frame, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20)
			);

		if (len(rects) > 0):

			rects[:, 2:] += rects[:, :2];

			for x1, y1, x2, y2 in rects:
				cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 1);
			#END

			return(True);

		else:
			
			return (False);

		#END
		
	#END

	def detect_eyes(cv2, haar, frame):
		
		rects	= haar.detectMultiScale(
			frame, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20,20)
			);

		var = [];

		if (len(rects) > 1):

			rects[:, 2:] += rects[:, :2];

			for x1, y1, x2, y2 in rects:
				cv2.rectangle(frame, (x1, y1), (x2, y2), (255,255,0), 1);
				var.append(x1);
				var.append(y1);
				var.append(x2);
				var.append(y2);
			#END

			return var;

		else:
			
			return 0, 0;

		#END

	#END

#END		