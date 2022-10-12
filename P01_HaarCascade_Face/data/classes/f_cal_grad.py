class GRAD_CALC():

	def draw_line(cv2, coord, frame):

		orientation = 'Derecha';

		m1_1 = coord[0] + int((coord[2] - coord[0]) / 2);
		m1_2 = coord[1] + int((coord[3] - coord[1]) / 2);
		m2_1 = coord[4] + int((coord[6] - coord[4]) / 2);
		m2_2 = coord[5] + int((coord[7] - coord[5]) / 2);

		cv2.line(frame, (m1_1, m1_2), (m2_1, m2_2), (255, 100, 0), 1);

		med = int(abs(m1_1 - m2_1) /2);

		if (m1_1 < m2_1):
			
			med += m1_1;
			
			if (m1_2 < m2_2):
				orientation = 'izquierda';
			#END

		else:
			
			med += m2_1

			if (m2_2 < m1_2):
				orientation = 'izquierda';
			#END

		#END

		cv2.line(frame, (med, 0), (med, len(frame[0])), (55, 0, 255), 1);

		if (m1_2 > m2_2):
			cv2.line(frame, (0, m1_2), (len(frame), m1_2), (55, 0, 255), 1);
		else:
			cv2.line(frame, (0, m2_2), (len(frame), m2_2), (55, 0, 255), 1);
		#END

		return (m1_2, m2_2, orientation);

	#END

	def cal_grad(eye1, eye2, orient):
		
		val  = abs(eye2 - eye1);

		grad = 0;

		while (val > 0):
			
			val  -= 2.4827;
			grad += 1;

		#END

		if (grad == 0):
			return(grad, 'centrado');
		else:
			return(grad, orient);
		#END

	#END

#END