# skeleton_with_openpose
how to extract skeleton(slim or thick) withing openpose for action recognition dataset(RGB video frame)

1.First, you should complete Openpose project compiling!(https://github.com/CMU-Perceptual-Computing-Lab/openpose)

2.Second, cd in openpose/build/examples/tutorial_api_python/

3.Finally, before extracting, you should install dependency, as list:

    python 3.7.1
    numpy 1.20.2
    opencv 3.4.2

4.Using :(before running, try changing image_dir in line 60 to your own's dateset path!)

    python zjh_hmdb.py   ->> extract skeleton with RGB (pose) in HMDB-51 dataset
    
    python zjh_hmdb_cu.py  ->> extract skeleton(thick) with RGB (pose) in HMDB-51 dataset, changing k to change thickness of skeleton in line 87
    
    python zjh_hmdb_only_skeleton.py ->> extract skeleton without RGB frames in HMDB-51 dataset
    
    python zjh_ucf.py   ->> extract skeleton with RGB (pose) in UCF-101 dataset
    
    python zjh_ucf_cu.py ->> extract skeleton(thick) with RGB (pose) in UCF-101 dataset, changing k to change thickness of skeleton in line 87
    
    python zjh_ucf_only_skeleton.py ->> extract skeleton without RGB frames in UCF-101 dataset
    
