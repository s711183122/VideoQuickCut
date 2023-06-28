# VideoQuickCut
一個快速剪輯影片中所需範圍的小程式(不包含音訊)   
A small program to quickly cut a desired range in a video (audio not included)  
  
執行 run
-------------
請更改 config.py 中的各項設定，並執行 main.py 開始程式。  
Please change the settings in 'config.py' and execute 'main.py' to start the program.  
  
鍵盤操作功能 Keyboard operation function  
-------------  
使用 'Space' 播放/暫停 影片。  
Use 'SPACE' to play/pause the video.   
  
使用 'o' 讓影片快轉 5 秒，使用 'l' 讓影片快轉 10 秒。  
Use 'o' to advance video for 5 sec, use 'l' to advance video for 10 sec.  
  
使用 'i' 讓影片倒回 5 秒，使用 'k' 讓影片倒回 10 秒。  
Use 'i' to backwind video for 5 sec, use 'k' to backwind video for 10 sec.  
  
使用 '.' 來更改影片播放速度。  
Use '.' to change video play speed. 
  
使用 'ESC' 或是 'q' 關閉程式。  
Use 'ESC' or 'q' to exit the program.  
  
使用 'n' or 'm' 進入 '新增範圍模式'，滑鼠左鍵設定左上點，滑鼠右鍵設定右下點，最後使用 'n' or 'm' 或 'ENTER' 新增範圍。
Use 'n' or 'm' to enter 'Add Range Mode', left mouse button to set the upper left point, right mouse button to set the lower right point, and finally use 'n' or 'm' or 'ENTER' to add a new range.  
  
使用 's' 進入 '儲存/輸出模式'，滑鼠左鍵點選任意範圍內部，最後使用 's' 或 'ENTER' 輸出影片。    
Use 's' to enter 'Save/Export Mode', left mouse click to select any range, and finally use 's' or 'ENTER' to export the video.   
  
影片結束後將會自動輸出所有範圍影片。   
All range videos will be output automatically after the movie ends.  
  
requirement
-------------  
python >= 3.9.14  
opencv-python >= 4.6.0
  
