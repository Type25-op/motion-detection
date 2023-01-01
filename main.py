import mediapipe
import cv2
import time
def alert(i):
    print(f"{i} : Fuck")
    return

def log(x:list):
    with open("output.txt","w") as file:
        file.writelines(x)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    cap = cv2.VideoCapture(0)
    mpHands = mediapipe.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mediapipe.solutions.drawing_utils
    ptime = time.time()
    no_of_fucks = 0
    cooldown = time.time()
    while True:
        success , img = cap.read()
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)
        if result.multi_hand_landmarks:

            for handLms in result.multi_hand_landmarks:
                mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
                out = []
                for id,lm in enumerate(handLms.landmark):
                    h,w,c = img.shape
                    cx, cy = int(lm.x*w),int(lm.y*h)
                    out.append(f"{id:3}: {(cx)} {(cy)} \n")
                    if id == 12:
                        cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)
                        if cx - (handLms.landmark[8].x * w) >60 and cx - (handLms.landmark[16].x * w) > 60:
                            if time.time() - cooldown >3:
                                alert(no_of_fucks+1)
                                no_of_fucks+=1
                                cooldown = time.time()
                            # else:print("time short")
                log(out)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv2.putText(img,str(int(fps)) ,(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3 )
        cv2.imshow("Image", img)
        cv2.waitKey(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # alert(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
