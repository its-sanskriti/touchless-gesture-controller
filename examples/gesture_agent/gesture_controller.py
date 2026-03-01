import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Finger tip landmark indexes
tip_ids = [4, 8, 12, 16, 20]

# Command text shown on screen
current_command = ""

print("Touchless Gesture Controller Running...")

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert BGR → RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

            lm_list = []
            for id, lm in enumerate(hand.landmark):
                h, w, _ = frame.shape
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            fingers = []

            # Thumb (horizontal check)
            if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0]-1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other four fingers (vertical check)
            for i in range(1, 5):
                if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i]-2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = sum(fingers)

            # Gesture → Command mapping
            if total_fingers == 5:
                current_command = "PAUSE"

            elif total_fingers == 1:
                current_command = "ACCEPT"

            elif total_fingers == 2:
                current_command = "NEXT"

    # Display command on screen
    cv2.putText(
        frame,
        f"Command: {current_command}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        3
    )

    cv2.imshow("Touchless Gesture Controller", frame)

    # Exit using ESC or Q
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        print("Exiting Gesture Controller...")
        break

cap.release()
cv2.destroyAllWindows()