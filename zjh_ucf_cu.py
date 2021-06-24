# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse
os.environ["CUDA_VISIBLE_DEVICES"]="2"
try:
    # Import Openpose (Windows/Ubuntu/OSX)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        # Windows Import
        if platform == "win32":
            # Change these variables to point to the correct folder (Release/x64 etc.)
            sys.path.append(dir_path + '/../../python/openpose/Release');
            os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
            import pyopenpose as op
        else:
            # Change these variables to point to the correct folder (Release/x64 etc.)
            sys.path.append('../../python');
            # If you run `make install` (default path is `/usr/local/python` for Ubuntu), you can also access the OpenPose/python module from there. This will install OpenPose and the python library at your desired installation path. Ensure that this is in your python path in order to use it.
            sys.path.append('/usr/local/python')
            from openpose import pyopenpose as op
    except ImportError as e:
        print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
        raise e

    # Flags
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_path", default="./00001.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    parser.add_argument("--write_images", default="./00001.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
    args = parser.parse_known_args()

    # Custom Params (refer to include/openpose/flags.hpp for more parameters)
    params = dict()
    params["model_folder"] = "../../../models/"

    # Add others in path?
    for i in range(0, len(args[1])):
        curr_item = args[1][i]
        if i != len(args[1])-1: next_item = args[1][i+1]
        else: next_item = "1"
        if "--" in curr_item and "--" in next_item:
            key = curr_item.replace('-','')
            if key not in params:  params[key] = "1"
        elif "--" in curr_item and "--" not in next_item:
            key = curr_item.replace('-','')
            if key not in params: params[key] = next_item

    # Construct it from system arguments
    # op.init_argv(args[1])
    # oppython = op.OpenposePython()

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    image_dir='/DATA4T/openpose/UCF101'
    gpu=1
    with open('list_ucf.txt','r+') as f:
        line=f.readline()
        while line:
            target=os.path.join('/New-8T/mars/UCF101_pose',line.split('.')[0])
            org=os.path.join(image_dir,line.split('.')[0])
            org_num=os.listdir(os.path.join('/DATA4T/openpose/UCF101',line.split('.')[0]))
            if not os.path.exists(target):
                os.makedirs(target)
            now_num=os.listdir(target)
            for i in range(1,len(org_num)+1):
                if '{:0>5d}.jpg'.format(i) not in now_num:
                    try:
                        # Process Image
                        datum = op.Datum()
                        imageToProcess = cv2.imread(os.path.join(image_dir,line.split('.')[0] ,'{:0>5d}.jpg'.format(i)))
                        datum.cvInputData = imageToProcess
                        opWrapper.emplaceAndPop(op.VectorDatum([datum]))
                        for points in datum.poseKeypoints.tolist():
                        k=7
                        flag=[0]*25
                        for z in range(25):
                            flag[z]=any(points[z])
                        if flag[17] and flag[15]:
                            x1,y1,x2,y2=int(points[17][0]),int(points[17][1]),int(points[15][0]),int(points[15][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(210,70,233),k)
                        if flag[0] and flag[15]:
                            x1,y1,x2,y2=int(points[0][0]),int(points[0][1]),int(points[15][0]),int(points[15][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(156,69,234),k)
                        if flag[0] and flag[16]:
                            x1,y1,x2,y2=int(points[0][0]),int(points[0][1]),int(points[16][0]),int(points[16][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(192,54,170),k)
                        if flag[18] and flag[16]:
                            x1,y1,x2,y2=int(points[18][0]),int(points[18][1]),int(points[16][0]),int(points[16][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(185,43,103),k)
                        if flag[0] and flag[1]:
                            x1,y1,x2,y2=int(points[0][0]),int(points[0][1]),int(points[1][0]),int(points[1][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(94,56,225),k)
                        if flag[1] and flag[2]:
                            x1,y1,x2,y2=int(points[1][0]),int(points[1][1]),int(points[2][0]),int(points[2][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(61,124,235),k)
                        if flag[1] and flag[5]:
                            x1,y1,x2,y2=int(points[1][0]),int(points[1][1]),int(points[5][0]),int(points[5][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(60,221,167),k)
                        if flag[1] and flag[8]:
                            x1,y1,x2,y2=int(points[1][0]),int(points[1][1]),int(points[8][0]),int(points[8][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(38,36,190),k)
                        if flag[9] and flag[8]:
                            x1,y1,x2,y2=int(points[9][0]),int(points[9][1]),int(points[8][0]),int(points[8][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(107,207,56),k)
                        if flag[9] and flag[10]:
                            x1,y1,x2,y2=int(points[9][0]),int(points[9][1]),int(points[10][0]),int(points[10][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(173,222,70),k)
                        if flag[10] and flag[11]:
                            x1,y1,x2,y2=int(points[10][0]),int(points[10][1]),int(points[11][0]),int(points[11][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(209,213,72),k)
                        if flag[11] and flag[24]:
                            x1,y1,x2,y2=int(points[11][0]),int(points[11][1]),int(points[24][0]),int(points[24][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(187,188,38),k)
                        if flag[11] and flag[22]:
                            x1,y1,x2,y2=int(points[11][0]),int(points[11][1]),int(points[22][0]),int(points[22][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(250,250,11),k)
                        if flag[23] and flag[22]:
                            x1,y1,x2,y2=int(points[23][0]),int(points[23][1]),int(points[22][0]),int(points[22][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(240,240,30),k)
                        if flag[8] and flag[12]:
                            x1,y1,x2,y2=int(points[8][0]),int(points[8][1]),int(points[12][0]),int(points[12][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(191,136,35),k)
                        if flag[12] and flag[13]:
                            x1,y1,x2,y2=int(points[12][0]),int(points[12][1]),int(points[13][0]),int(points[13][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(220,115,65),k)
                        if flag[13] and flag[14]:
                            x1,y1,x2,y2=int(points[13][0]),int(points[13][1]),int(points[14][0]),int(points[14][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(206,60,70),k)
                        if flag[14] and flag[21]:
                            x1,y1,x2,y2=int(points[14][0]),int(points[14][1]),int(points[21][0]),int(points[21][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(240,28,30),k)
                        if flag[19] and flag[14]:
                            x1,y1,x2,y2=int(points[19][0]),int(points[19][1]),int(points[14][0]),int(points[14][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(240,80,80),k)
                        if flag[19] and flag[20]:
                            x1,y1,x2,y2=int(points[19][0]),int(points[19][1]),int(points[20][0]),int(points[20][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(250,35,35),k)
                        if flag[3] and flag[2]:
                            x1,y1,x2,y2=int(points[3][0]),int(points[3][1]),int(points[2][0]),int(points[2][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(50,165,237),k)
                        if flag[3] and flag[4]:
                            x1,y1,x2,y2=int(points[3][0]),int(points[3][1]),int(points[4][0]),int(points[4][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(58,224,237),k)
                        if flag[5] and flag[6]:
                            x1,y1,x2,y2=int(points[5][0]),int(points[5][1]),int(points[6][0]),int(points[6][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(40,200,116),k)
                        if flag[6] and flag[7]:
                            x1,y1,x2,y2=int(points[6][0]),int(points[6][1]),int(points[7][0]),int(points[7][1])
                            cv2.line(imageToProcess,(x1,y1),(x2,y2),(20,240,50),k)   

                        # Display Image
                        #imageToProcess=datum.cvOutputData
                        cv2.imwrite(target+'/'+'{:0>5d}.jpg'.format(i),imageToProcess)

                    except Exception as e:
                        cv2.imwrite(r'{}/{:0>5d}.jpg'.format(target, j), imageToProcess)
            line=f.readline()
except Exception as e:
    print(e)

