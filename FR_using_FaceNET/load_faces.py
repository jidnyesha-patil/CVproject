import mtcnn
import cv2
import numpy as np
import os

doc1 = {"Name":[] , "Count":[]}
path = 'C:\\Users\\rushi\\Documents\\CV_project\\Intro_DB\\'
name_list = os.listdir(path)
for name in name_list:
    doc1["Name"].append(name)
    new_path = path + name + '\\'
    n = os.listdir(new_path)
    doc1["Count"].append(len(n))
    
def face_detection(pix,detector,labeled_image = False):
    results = detector.detect_faces(pix)
    if results:
        x1, y1, width, height = results[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        face = pix[y1:y2, x1:x2]
        face = cv2.resize(face,(160,160))
        if labeled_image == False:
            return face
        else:
            cv2.rectangle(pix, (x1, y1), (x2, y2), (255, 0, 0), 5)
            return (face,pix, [x1,y1])

    return None

def load_faces(doc1=doc1,save_images=0):
    doc2 = {"label":[],"images":[]}
    path = "Intro_DB\\"
    path1 = "Intro_DB_Faces\\"
    detector = mtcnn.MTCNN()
    for length in range(len(doc1["Name"])):
        name = doc1["Name"][length]
        c = doc1["Count"][length]
        new_path = path + name + "\\" + name
        for i in range(c):
            new_path1 = new_path + str(i+1) + ".jpg"
            img1 = cv2.imread(new_path1)
            pix = np.asarray(img1)
            face = face_detection(pix,detector)
            if type(face) != type(None):
                new_path2 = path1 + name
                if not os.path.exists(new_path2):
                    os.makedirs(new_path2)
                new_path2 += "\\" + name + str(i+1) + '.jpg' 
                if save_images == 1:
                    cv2.imwrite(new_path2,face)
                doc2['label'].append(name)
                doc2['images'].append(face)
    return doc2
