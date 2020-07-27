
import tensorflow as tf

# get_ipython().system('pip install opencv-python')
#
#
# get_ipython().system('pip install imageai --upgrade')
#
# get_ipython().system('pip install imageAI')
#
# get_ipython().system('pip install tensorflow==1.14.0')


from imageai.Prediction import ImagePrediction
import cv2
import os
from imageai.Detection import ObjectDetection

def detect(img):
    execution_path = os.getcwd()

    detector = ObjectDetection()

    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    detector.loadModel()

    detections = detector.detectObjectsFromImage(input_image=img,
                                                 output_image_path=os.path.join(execution_path, "static/images/New_" + img.filename),
                                                 minimum_percentage_probability=30)

    # res_img, detections = detector.detectObjectsFromImage(input_image= img, extract_detected_objects = False, output_type = 'array',
    #                                              minimum_percentage_probability=30)
    d_list = []
    for eachObject in detections:
        d_list.append(eachObject["name"])
        d_list.append(":")
        d_list.append(eachObject["percentage_probability"])

    return d_list
    # print(type(detections))
    # print(type(res_img))
    # print(detections)
    # for eachObject in detections:
    #     print(eachObject["name"], " : ", eachObject["percentage_probability"])
    #     print("--------------------------------")
# img="1.jpeg"
#
# detect(img)





