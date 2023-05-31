import cv2, os 
from config import *

if not os.path.isdir(output_path): os.mkdir(output_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

class QuickCut:
    def __init__(self, tmp, time='', fps=30) -> None:
        self.has_save = False
        self.L = tmp['L']
        self.R = tmp['R']
        self.x0 = self.L[0]
        self.y0 = self.L[1]
        self.x1 = self.R[0]
        self.y1 = self.R[1]
        self.w = int(self.x1-self.x0)
        self.h = int(self.y1-self.y0)
        self.time = int(time)
        self.name = f'quickcut_{self.x0}_{self.y0}_{self.time}'
        self.savename = f'{output_path}{self.name}.mp4'
        self.VW = cv2.VideoWriter(self.savename, fourcc, fps, (self.w, self.h))
    def __str__(self) -> str:
        return f'{self.name} L=({self.x0},{self.y0}) R=({self.x1},{self.y1})'
    def draw(self, now_frame):
        if not self.has_save:
            f = now_frame.copy()
            cv2.rectangle(f, self.L, self.R, (0, 0, 255), 2)
            return f
        else:
            return now_frame
    def write(self, copy_frame):
        if not self.has_save:
            f2 = copy_frame.copy()[self.y0:self.y1, self.x0:self.x1]
            # f2 = cv2.resize(frame.copy(), (0,0), fx=(1/img_scale), fy=(1/img_scale))
            self.VW.write(f2)
    def save(self):
        if not self.has_save:
            print(f'QuickCut has saved to {self.savename} !')
            self.VW.release()
            self.has_save = True
    def check_pos(self, p):
        if not self.has_save:
            if self.x0 <= p[0] and p[0] <= self.x1:
                if self.y0 <= p[1] and p[1] <= self.y1:
                    self.save()
                    return True
        return False

def mouse_handler(event, x, y, flags, data):
    if data['new_QuickCut'] == 1:
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"    New QuickCut LBUTTONDOWN: (x={x}, y={y})")
            data['tmp']['L'] = (x,y)
        if event == cv2.EVENT_RBUTTONDOWN:
            print(f"    New QuickCut RBUTTONDOWN: (x={x}, y={y})")
            data['tmp']['R'] = (x,y)
    elif data['new_QuickCut'] == -1:
        if event == cv2.EVENT_LBUTTONDOWN:
            data['now'] = (x,y)
            print(f"    Save QuickCut LBUTTONDOWN: (x={x}, y={y})")

def main():
    data = {'new_QuickCut': 0, 'QuickCut': [], 'tmp':{'L':None, 'R':None}, 'now':None}
    cv2.namedWindow("Image", 0)
    cap = cv2.VideoCapture(vpath)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f'Video FPS = {fps}')
    ret, frame = cap.read()
    f2 = cv2.resize(frame, (0,0), fx=img_scale, fy=img_scale)
    h2, w2, dim2 = f2.shape
    cv2.resizeWindow("Image", w2, h2)
    cv2.setMouseCallback("Image", mouse_handler, data)
    play = 1
    while cap.isOpened():
        if play:
            ret, frame = cap.read()
            if not ret:
                print(f'Video end.')
                break
            now_frame = cv2.resize(frame, (0,0), fx=img_scale, fy=img_scale)
            copy_frame = now_frame.copy()
            for qc_ in data['QuickCut']:
                now_frame = qc_.draw(now_frame)
                qc_.write(copy_frame)
        cv2.imshow('Image', now_frame)
        key = cv2.waitKey(int(1000/fps))
        if key == 27 or key == ord('q'):
            'Esc: 27 Enter: 13 Up: 82 Down: 84 Left: 81 Right: 83 Space: 32 Backspace: 8'
            print('break')
            break
        elif key == 32:
            if play: play = 0
            else: play = 1
            print('Play' if play else 'Pause')
        elif key == ord('n'):
            print(f'New QuickCut')
            data['new_QuickCut'] = 1
            while True:
                key2 = cv2.waitKey()
                if key2 == 13 or key2 == ord('n'):
                    if not data['tmp']['L']:
                        print(' You must to set L !')
                    elif not data['tmp']['R']:
                        print(' You must to set R !')
                    elif data['tmp']['L'][0] >= data['tmp']['R'][0] or data['tmp']['L'][1] >= data['tmp']['R'][1]:
                        print(' L is over R, please try it again.')
                        data['tmp']['L'] = None
                        data['tmp']['R'] = None
                    else:
                        qc = QuickCut(data['tmp'], time=cap.get(0), fps=fps)
                        data['QuickCut'].append(qc)
                        print(f'{qc}')
                        break
                elif key2 == 27:    break
            data['new_QuickCut'] = 0
            data['tmp'] = {'L':None, 'R':None}
        elif key == ord('s'):
            print(f'Save QuickCut')
            data['new_QuickCut'] = -1
            while True:
                key2 = cv2.waitKey()
                if key2 == 13 or key2 == ord('s'):
                    if not data['now']:
                        print(' You must to set a point !')
                    else:
                        for qc_ in data['QuickCut']:
                            if qc_.check_pos(data['now']): break
                        data['now'] = None
                        break
                elif key2 == 27:    break


    for qc_ in data['QuickCut']:
        qc_.save()
            
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()