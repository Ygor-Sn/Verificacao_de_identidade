import face_recognition,os,cv2,time
folder_face = r'faces/'
files_in_folder = len(os.listdir(folder_face))
array_time_check = []
array_por_ecli = []


def recon(frame, context, txt_context,resultado_recon):
    global files_in_folder
    if files_in_folder == 0 and context == 1:

        txt_context[0] = 'erro: Sem rostos para indentificar! Salve um rosto antes!'
        txt_context[1] = ("Arial", 15)
        txt_context[2] = 'red'
        txt_context[3] = 'white'

        return txt_context

    img_to_recon = face_recognition.face_locations(frame)
    
    if len(img_to_recon) > 0:
        match context:
            case 1:
                return check(frame, img_to_recon, txt_context,resultado_recon)
            case 2:
                return rec_face(frame, files_in_folder,txt_context)
            case _:
                print('erro falta de contexto')
                txt_context[0] = 'erro: falta de contexto!'
                txt_context[1] = ("Arial", 28)
                txt_context[2] = 'red'
                txt_context[3] = 'white'
                return txt_context
    else:
        print('nenhum Rosto detectado, aguardando...')
        txt_context[0] = 'Nenhum rosto detectado, procurando...'
        txt_context[1] = ("Arial", 20)
        txt_context[2] = 'SystemButtonFace'
        txt_context[3] = 'SystemButtonText'
        return txt_context


def check(frame, img_to_recon,txt_context,resultado_recon):
    global array_time_check, array_por_ecli
    time_check = time.time()

    found = False
    recon_encod = face_recognition.face_encodings(frame, img_to_recon)[0]

    for i in range(0, files_in_folder):
        get_file_face = f'{folder_face}face_{i}.jpeg'
        img_load = face_recognition.load_image_file(get_file_face)
        img_encod = face_recognition.face_encodings(img_load)[0]
        resultado = face_recognition.compare_faces([img_encod], recon_encod)
        dis_eclidiana = face_recognition.face_distance([img_encod], recon_encod)[0]
        por_eclidiana = (1 - dis_eclidiana) * 100

        if resultado[0] == True:
            print('Rosto Indentificado!')
            found = True
            txt_context[0] = 'Rosto Indentificado!'
            txt_context[1] = ("Arial", 20)
            txt_context[2] = 'green'
            txt_context[3] = 'white'
            resultado_recon(frame,1,img_to_recon[0], por_eclidiana,color=(0,255,0))
            array_por_ecli.append(por_eclidiana)
            array_time_check.append(time.time() - time_check)
            return txt_context

    if found == False:
        print('Rosto Nâo Indentificado!')
        txt_context[0] = 'Rosto Não Indentificado!'
        txt_context[1] = ("Arial", 20)
        txt_context[2] = 'red'
        txt_context[3] = 'white'
        resultado_recon(frame,1,img_to_recon[0], por_eclidiana,color=(0,0,255))
        array_por_ecli.append(por_eclidiana)
        array_time_check.append(time.time() - time_check)
        return txt_context
    




def rec_face(img_to_rec, id_to_rec, txt_context):
    global files_in_folder
    path = f'{folder_face}face_{id_to_rec}.jpeg'
    convert = cv2.cvtColor(img_to_rec, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, convert)
    print(f'Rosto salvo em: {path}')
    txt_context[0] = 'Rosto salvo!'
    txt_context[1] = ("Arial", 20)
    txt_context[2] = 'green'
    txt_context[3] = 'white'
    files_in_folder = len(os.listdir(folder_face))
    return txt_context

def send_info_grafic():
    global array_time_check, array_por_ecli
    return array_por_ecli,array_time_check