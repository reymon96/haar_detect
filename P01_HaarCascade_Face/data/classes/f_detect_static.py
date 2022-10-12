import os;
import data.classes.f_script 	as fS;
import data.classes.f_cal_grad 	as cG;

class DETECT_STATIC():

	def detect_os(cv2, dir_, frontal_face, profile_face, eye_tree):
		
		files = os.listdir(dir_);
		print('Imagenes encontradas: ', len(files), 'archivos.\n');

		for file in files:

			capture			= cv2.VideoCapture('data/img/' + file);
			rects, frame 	= capture.read();

			try:

				if 	 (fS.ALGORITM_HAAR.detect_face(cv2, frontal_face, frame)):
					
					coord = fS.ALGORITM_HAAR.detect_eyes(cv2, eye_tree, frame);

					if (len(coord) == 8):
						
						print('imagen', file, 'acetada.');

						eye1, eye2, orient 	= cG.GRAD_CALC.draw_line(cv2, coord, frame);
						grad, orient 		= cG.GRAD_CALC.cal_grad(eye1, eye2, orient);

						cv2.imwrite(
							'data/result/algoritm/Grados:' + 
							str(grad) + '_' + orient + '_' + file, frame);

					else:
						print('Incapaz de calcular grados por ojos insuficientes.');
					#END

				elif (fS.ALGORITM_HAAR.detect_face(cv2, profile_face, frame)):

					coord = fS.ALGORITM_HAAR.detect_eyes(cv2, eye_tree, frame);
					
					if (len(coord) == 8):
						
						print('imagen', file, 'acetada.');
						
						eye1, eye2, orient 	= cG.GRAD_CALC.draw_line(cv2, coord, frame);
						grad, orient 		= cG.GRAD_CALC.cal_grad(eye1, eye2, orient);

						cv2.imwrite(
							'data/result/algoritm/Grados:' + 
							str(grad) + '_' + orient + '_' + file, frame);

					else:
						print('Incapaz de calcular grados por ojos insuficientes.');
					#END

				else:
					
					coord = fS.ALGORITM_HAAR.detect_eyes(cv2, eye_tree, frame);

					if (len(coord) == 8):

						print('imagen', file, 'acetada.');
						
						eye1, eye2, orient 	= cG.GRAD_CALC.draw_line(cv2, coord, frame);
						grad, orient 		= cG.GRAD_CALC.cal_grad(eye1, eye2, orient);

						cv2.imwrite(
							'data/result/algoritm/Grados:' + 
							str(grad) + '_' + orient + '_' + file, frame);
					else:
						print('No se encontraron características suficientes en el Archivo', file);
					#END

				#END
				
			
			except Exception as e:
				
				print('Error en el analisis de', file, '\n', e);

			#END

		#END

	#END

#END		