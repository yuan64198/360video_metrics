import cv2
import numpy
import os
import threading

from MetricsCalc import MetricsCalc

def main():


	#"panel_tr_u01_30.csv"
	panel_cr_u01 = [n for n in os.listdir("./video/panel/user01/CR/") if n[0]=='p' and n[-4:]=='.mp4']
	panel_cr_u01 = sorted(panel_cr_u01, key=lambda item: int( item.split('_')[2]))

	#"panel_tr_u01_30.csv"
	panel_tr_u01 = [n for n in os.listdir("./video/panel/user01/TR/") if n[0]=='p' and n[-4:]=='.mp4']
	panel_tr_u01 = sorted(panel_tr_u01, key=lambda item: int( item.partition('.')[0][13:]))
	
	#"game_cr_u01_30.csv"	
	game_cr_u01 = [n for n in os.listdir("./video/game/user01/CR/") if n[0]=='g' and n[-4:]=='.mp4']
	game_cr_u01 = sorted(game_cr_u01, key=lambda item: int( item.split('_')[2]))
	
	#"game_tr_u01_30.csv"
	game_tr_u01 = [n for n in os.listdir("./video/game/user01/TR/") if n[0]=='g' and n[-4:]=='.mp4']
	game_tr_u01 = sorted(game_tr_u01, key=lambda item: int( item.partition('.')[0][12:]))

	t1 = threading.Thread(target = MetricsCalc, args = ( "game_cr_u01_3.csv", "./video/game/user01/CR/", game_cr_u01, "./video/game/game_equir.mp4", 1))	
	t2 = threading.Thread(target = MetricsCalc, args = ( "game_cr_u01_5.csv", "./video/game/user01/CR/", game_cr_u01, "./video/game/game_equir.mp4", 1))

	t1.start()
	t2.start()
	t1.join()
	t2.join()
if __name__ == "__main__":
	main()

