import random
import cv2
import HandTrackingModule as htm
import time
import os

def checkWinner(player, comp):
    if player == comp:
        return None  # Draw
    elif player == 'rock' and comp == 'scissor':
        return 0  # Player wins
    elif player == 'paper' and comp == 'rock':
        return 0  # Player wins
    elif player == 'scissor' and comp == 'paper':
        return 0  # Player wins
    else:
        return 1  # Computer wins

def main():
    waitTime = 4
    moves = ['rock', 'paper', 'scissor']
    scores = [0, 0]  # [player, comp]
    comp, player = None, None
    wCam, hCam = 1280, 720

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.handDetector(detectionCon=0.8, maxHands=1)

    pTime = 0
    prevTime = time.time()
    newTime = time.time()

    game_started = False
    game_paused = False

    # Path to the directory containing the images
    images_path = r'C:\Users\SUNANDAN PC\OneDrive\Desktop\Projects\RockPaperScissor-OpenCV-main\RockPaperScissor-OpenCV-main\Fingers'

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        if not game_started:
            cv2.putText(img, 'Press "s" to start the game', (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.putText(img, 'Press "p" to pause the game', (400, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        elif game_paused:
            cv2.putText(img, 'Game paused. Press "p" to resume', (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.line(img, (wCam // 2, 0), (wCam // 2, hCam), (0, 255, 0), 5)
            cv2.rectangle(img, (780, 160), (1180, 560), (0, 0, 255), 2)
            cv2.putText(img, f'Player: {scores[0]}', (wCam - 300, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 250, 0), 3)
            cv2.putText(img, f'Computer: {scores[1]}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 250, 0), 3)

            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)

            if waitTime - int(newTime) + int(prevTime) < 0:
                cv2.putText(img, '0', (960, 120), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255), 3)
            else:
                cv2.putText(img, f'{waitTime - int(newTime) + int(prevTime)}', (960, 120), cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255), 3)

            if len(lmList) != 0 and newTime - prevTime >= waitTime:
                x, y = lmList[0][1:]
                if 780 < x < 1180 and 160 < y < 560:
                    fingers = detector.fingersUp()
                    totalFingers = fingers.count(1)

                    if totalFingers == 0:
                        player = 'rock'
                    elif totalFingers == 2:
                        player = 'scissor'
                    elif totalFingers == 5:
                        player = 'paper'
                    else:
                        player = None  # Invalid gesture

                    if player is not None:
                        comp = moves[random.randint(0, 2)]

                        if comp is not None:
                            winner = checkWinner(player, comp)
                            if winner is not None:
                                scores[winner] += 1

                        prevTime = time.time()

            if comp:
                # Load and display the computer's move image
                comp_img_path = os.path.join(images_path, f'{comp}.jpg')
                comp_img = cv2.imread(comp_img_path)
                if comp_img is not None:
                    img[160:560, 120:520] = comp_img
                else:
                    print(f"Failed to load image: {comp_img_path}")

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (1050, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        newTime = time.time()
        cv2.imshow('Image', img)

        key = cv2.waitKey(1)
        if key == ord('s') and not game_started:  # Start game
            game_started = True
        elif key == ord('p') and game_started:  # Pause game
            game_paused = not game_paused
        elif key == ord('q'):  # Quit game
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
