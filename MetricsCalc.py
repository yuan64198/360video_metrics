import numpy
import cv2

from WSPsnrCalc import WSPsnrCalc
from SPsnrNnCalc import SPsnrNnCalc
from PsnrCalc import PsnrCalc


def MetricsCalc( log_name, path, expe_clips, cont_video, T, mode = 0, next_frame = 0):
	
	if mode == 0:
		f = open(log_name,"w")
		f.write("      frame No.,           PSNR,      S-PSNR-NN,        WS-PSNR\n")
		f.close()
	else:
		print("Continue mode. Start from "+str(next_frame))


	frame_no = 0
	psnr_list = []
	s_psnr_list = []
	ws_psnr_list = []
	flag = False
	cont = cv2.VideoCapture(cont_video)
	print("Start Evaluating PSNR...")
	
	for vf in expe_clips:
		expe = cv2.VideoCapture(path+vf)
		while(True):
			ret, imgE = expe.read()
			if(imgE is None):
				print("next clip...")
				break
			ret, imgC = cont.read()
			if(imgC is None):
				print("Error occured!")
				return
			if( (frame_no%T) != 0 or frame_no < next_frame):
				frame_no += 1
				continue
			psnr = PsnrCalc(imgC, imgE)
			s_psnr_nn = SPsnrNnCalc(imgC, imgE)
			ws_psnr = WSPsnrCalc(imgC, imgE)
			print("----------------------------")
			print("Frame No.")
			print(frame_no)
			print("PSNR:")
			print(psnr)
			print("S-PSNR-NN:")
			print(s_psnr_nn)
			print("WS-PSNR:")
			print(ws_psnr)
			f = open(log_name, "a")
			f.write(str(frame_no).ljust(15)+','+str(psnr).rjust(15)+','+str(s_psnr_nn).rjust(15)+','+str(ws_psnr).rjust(15)+'\n')
			psnr_list.append(psnr)
			s_psnr_list.append(s_psnr_nn)
			ws_psnr_list.append(ws_psnr)
			frame_no += 1
	
	f = open(log_name, "a")
	f.write("###############,"+str(np.mean(psnr_list)).rjust(15)+','+str(np.mean(s_psnr_list)).rjust(15)+','+str(np.mean(ws_psnr_list).rjust(15)+'\n'))
	f.close()
	print("Evaluation finished!")		
