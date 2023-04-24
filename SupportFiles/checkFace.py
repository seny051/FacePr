import face_recognition
import cv2
import numpy as np
from os import walk,getcwd
from SupportFiles import responce
from SupportFiles import arduino

def check():
    video_capture = cv2.VideoCapture(0)
    known_face_encodings = []
    known_face_names = []
    for root, dirs, files in walk(getcwd()+'\\base'):  
        for filename in files:
            known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(getcwd()+'\\base\\'+filename))[0])
            known_face_names.append(responce.namePerson(int(filename.split('.')[0])))
    if len(known_face_names)!=0 and len(known_face_encodings)!=0:
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        time=0
        board = arduino.connectArd()
        open=False
        while True:

            ret, frame = video_capture.read()
            if process_this_frame:
                small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

                rgb_small_frame = small_frame[:, :, ::-1]

                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]
                    face_names.append(name)
                    if len(face_names)!=0 and face_names[0]!='Unknown':
                        if open==True and time>=0:
                            time=100
                        if open==False and time==0:
                            for l in range(0,90,5):
                                arduino.rot(board,9,l)
                            open=True
                            time+=100
            if time>0:
                time-=1
            if open==True and time ==0:
                    print(time, open)
                    for l in range(90, 0, -5):
                        arduino.rot(board, 9, l)
                    open=False
            process_this_frame = not process_this_frame

            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame,name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            cv2.imshow('Video', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                ser.close()
                break

        video_capture.release()
        cv2.destroyAllWindows()
    else:
        return 'База данный пуста'
