import cv2
import face_recognition
from PIL import Image
from SupportFiles import responce

def register(ID,Firstname,Surname,Position):
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            ret, frame = cap.read()
            cv2.imwrite(f'base\{ID}.jpg', frame)
            image = face_recognition.load_image_file(f"base\{ID}.jpg")
            face_locations = face_recognition.face_locations(image)
            for face_location in face_locations:
                top, right, bottom, left = face_location
                face_image = image[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                pil_image.save(f'base\{ID}.jpg')
                responce.reg(ID,Firstname,Surname,Position)
            break
    cap.release()
    cv2.destroyAllWindows()

