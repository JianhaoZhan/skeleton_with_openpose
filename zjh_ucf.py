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

                        # Display Image
                        imageToProcess=datum.cvOutputData
                        cv2.imwrite(target+'/'+'{:0>5d}.jpg'.format(i),imageToProcess)

                    except Exception as e:
                        cv2.imwrite(args[0].write_images,imageToProcess)
            line=f.readline()
except Exception as e:
    print(e)

