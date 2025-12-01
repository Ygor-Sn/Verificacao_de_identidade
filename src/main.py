import cv2
import keyboard
import time
import tkinter as tk
from PIL import ImageTk, Image
from recontoshi import recon, send_info_grafic
from vars import alt_array_dis_por, alt_recon_time

txt_context = ["Mantenha o rosto centralizado",
               ("Arial", 28), "SystemButtonFace", "SystemButtonText"]

# controle
pause_until = 0

window = tk.Tk()
window.title("Projeto Verificação de Identidade por Reconhecimento Facial Identificação")
window.geometry('700x550')

label = tk.Label(window)
label.pack()

text = tk.Label(window, text="Mantenha o rosto centralizado",
                font=("Arial", 28))
text.pack()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def main():
    global pause_until, txt_context

    now = time.time()

    if now < pause_until:
        window.after(10, main)
        return

    ok, frame = cam.read()
    if not ok:
        window.after(10, main)
        return

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if keyboard.is_pressed('r'):
        print('registtrando')
        txt_context = recon(frame_rgb, 2, txt_context, resultado_recon)
    if keyboard.is_pressed('g'):

        recon_time, array_dis_por = send_info_grafic()
        with open('./src/vars.py', 'w') as test:
            test.write(f'''
import numpy as np
alt_array_dis_por={recon_time + alt_recon_time}
alt_recon_time={array_dis_por + alt_array_dis_por}
''')
            print('gravado')

    img_tk = ImageTk.PhotoImage(Image.fromarray(frame_rgb))
    label.image = img_tk
    label.config(image=img_tk)

    text.config(text=txt_context[0],
                font=txt_context[1],
                bg=txt_context[2],
                fg=txt_context[3])

    if now % 5 < 0.02:
        txt_context = recon(frame_rgb, 1, txt_context, resultado_recon)

    window.after(10, main)


def resultado_recon(frame, resultado, xyzh, por_eclidiana, color):
    global pause_until

    pause_until = time.time() + 3

    top, right, bottom, left = xyzh

    w = right - left
    h = bottom - top

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    cv2.rectangle(frame, (left, top), (left + w, top + h), color, 3)
    cv2.putText(frame, f"Distancia eclidiana:{por_eclidiana:.1f}%", (
        left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    img_tk = ImageTk.PhotoImage(Image.fromarray(frame))
    label.image = img_tk
    label.config(image=img_tk)


main()
window.mainloop()
