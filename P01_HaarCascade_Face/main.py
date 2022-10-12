import cv2;
import data.classes.f_script 			as haar_cascade;
import data.classes.f_detect_static 	as dS;
import data.classes.f_detect_dinamic 	as dD;

class VOID_MAIN():

	def __main__():

		#Archivo especializado en rostros frontales;
		frontal_face 	= haar_cascade.ALGORITM_HAAR.import_haar(
			cv2, 'data/xml/haarcascade_frontalface_alt.xml');
		#Archivo especializado en rostros de perfíl;
		profile_face 	= haar_cascade.ALGORITM_HAAR.import_haar(
			cv2, 'data/xml/haarcascade_profileface.xml');
		#Archivo especializado en ojos;
		eye_tree 		= haar_cascade.ALGORITM_HAAR.import_haar(
			cv2, 'data/xml/haarcascade_eye_tree_eyeglasses.xml');

		print('Programa de detección de rostros Haar Cascade:\n\n', 
			'	Seleccione de las siguientes opciones la que desee:\n\n', 
			'	Opción 1: Detección de rostros en imágenes estáticas.\n',
			'	Opción 2: Detección y seguimiento de rostros en videocam.\n',
			'	Opción 3: Salir.\n\n');

		while (True):
			
			var = input('\nOpción Deseada: ');
			
			if 	 (var == '1'):
				#Detección de rostros en imágenes estáticas;
				
				print('Iniciando Detección:\n');
				dS.DETECT_STATIC.detect_os(cv2, input('Ingrese directorio: '),
					frontal_face,
					profile_face,
					eye_tree);

			elif (var == '2'):
				#Detección y seguimiento de rostros en videocam;
				
				print('Iniciando Seguimiento:\n');
				dD.DETECT_DINAMIC.detect_video(cv2, 
					frontal_face, 
					profile_face, 
					eye_tree);

			elif (var == '3'):
				#Fín del ciclo;
				
				print('Bye!\n');
				break;

			else:
				print('Opción Invalida.\n');
			#END

		#END

	#END

	__main__();

#END