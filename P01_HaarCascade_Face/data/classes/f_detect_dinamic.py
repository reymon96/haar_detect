import time;
import data.classes.f_script 	as fS;
import data.classes.f_cal_grad 	as cG;

class DETECT_DINAMIC():

	def detect_video(cv2, frontal_face, profile_face, eye_tree):
		
		capture			= cv2.VideoCapture(0);

		while (True):
			
			rects, frame 	= capture.read();

			try:
				
				if 	 (fS.ALGORITM_HAAR.detect_face(cv2, frontal_face, frame)):

					coord = fS.ALGORITM_HAAR.detect_eyes(cv2, eye_tree, frame);

					if (len(coord) == 8):

						eye1, eye2, orient 	= cG.GRAD_CALC.draw_line(cv2, coord, frame);
						grad, orient 		= cG.GRAD_CALC.cal_grad(eye1, eye2, orient);

						timer = str(time.strftime("%H:%M:%S"));
						cv2.imwrite(
							'data/result/NNC/Grados_' + 
							str(grad) + '_' + orient + '_' + timer + '.jpg', frame);
					#END

				elif (fS.ALGORITM_HAAR.detect_face(cv2, profile_face, frame)):
					
					coord = fS.ALGORITM_HAAR.detect_eyes(cv2, eye_tree, frame);

					if (len(coord) == 8):

						eye1, eye2, orient 	= cG.GRAD_CALC.draw_line(cv2, coord, frame);
						grad, orient 		= cG.GRAD_CALC.cal_grad(eye1, eye2, orient);

						timer = str(time.strftime("%H:%M:%S"));
						cv2.imwrite(
							'data/result/NNC/Grados_' + 
							str(grad) + '_' + orient + '_' + timer + '.jpg', frame);
					#END

				#END

			except Exception as e:
				
				print('Error en el analisis', e);

			#END

			cv2.imshow('Captura', frame);

			if (cv2.waitKey(10) == 27):
				cv2.destroyAllWindows();
				break;
			#END

		#END

	#END

#END