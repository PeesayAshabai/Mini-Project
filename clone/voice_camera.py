import cv2
import speech_recognition as sr
import pygame

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say 'capture' to take a photo...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

def play_click_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\ADMIN\Desktop\clone\click_sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        play_click_sound()  # Play click sound
        cv2.imwrite("captured_photo.jpg", frame)  # Save the captured image
    cam.release()
    cv2.destroyAllWindows()

def main():
    while True:
        command = listen_for_command()
        if command and "capture" in command:
            capture_image()
            print("Photo captured.")
        elif command:
            print("Command not recognized. Please say 'capture' to take a photo.")

if __name__ == "__main__":
    main()
