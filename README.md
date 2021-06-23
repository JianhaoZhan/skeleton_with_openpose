# skeleton_with_openpose
how to extract skeleton(slim or thick) withing openpose for action recognition dataset(RGB video frame)

1.First, you should complete Openpose project compiling!(https://github.com/CMU-Perceptual-Computing-Lab/openpose)

2.Second, cd in openpose/build/examples/tutorial_api_python/

3.Finally, before extracting, you should install dependency such as opencv, numpy ..., as list:

Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
backcall                  0.2.0              pyhd3eb1b0_0  
blas                      1.0                         mkl  
bzip2                     1.0.8                h7b6447c_0  
ca-certificates           2021.4.13            h06a4308_1  
cairo                     1.14.12              h8948797_3  
certifi                   2020.12.5        py37h06a4308_0  
decorator                 5.0.9              pyhd3eb1b0_0  
ffmpeg                    4.0                  hcdf2ecd_0  
fontconfig                2.13.1               h6c09931_0  
freeglut                  3.0.0                hf484d3e_5  
freetype                  2.10.4               h5ab3b9f_0  
glib                      2.63.1               h5a9c865_0  
graphite2                 1.3.14               h23475e2_0  
harfbuzz                  1.8.8                hffaf4a1_0  
hdf5                      1.10.2               hba1933b_1  
icu                       58.2                 he6710b0_3  
intel-openmp              2021.2.0           h06a4308_610  
ipython                   7.22.0           py37hb070fc8_0  
ipython_genutils          0.2.0              pyhd3eb1b0_1  
jasper                    2.0.14               h07fcdf6_1  
jedi                      0.17.0                   py37_0  
jpeg                      9b                   h024ee3a_2  
libedit                   3.1.20210216         h27cfd23_1  
libffi                    3.2.1             hf484d3e_1007  
libgcc-ng                 9.1.0                hdf63c60_0  
libgfortran-ng            7.3.0                hdf63c60_0  
libglu                    9.0.0                hf484d3e_1  
libopencv                 3.4.2                hb342d67_1  
libopus                   1.3.1                h7b6447c_0  
libpng                    1.6.37               hbc83047_0  
libstdcxx-ng              9.1.0                hdf63c60_0  
libtiff                   4.1.0                h2733197_1  
libuuid                   1.0.3                h1bed415_2  
libvpx                    1.7.0                h439df22_0  
libxcb                    1.14                 h7b6447c_0  
libxml2                   2.9.10               hb55368b_3  
lz4-c                     1.9.3                h2531618_0  
mkl                       2021.2.0           h06a4308_296  
mkl-service               2.3.0            py37h27cfd23_1  
mkl_fft                   1.3.0            py37h42c9631_2  
mkl_random                1.2.1            py37ha9443f7_2  
ncurses                   6.2                  he6710b0_1  
numpy                     1.20.2           py37h2d18471_0  
numpy-base                1.20.2           py37hfae3a4d_0  
opencv                    3.4.2            py37h6fd60c2_1  
openssl                   1.1.1k               h27cfd23_0  
parso                     0.8.2              pyhd3eb1b0_0  
pcre                      8.44                 he6710b0_0  
pexpect                   4.8.0              pyhd3eb1b0_3  
pickleshare               0.7.5           pyhd3eb1b0_1003  
pip                       21.0.1           py37h06a4308_0  
pixman                    0.40.0               h7b6447c_0  
prompt-toolkit            3.0.17             pyh06a4308_0  
ptyprocess                0.7.0              pyhd3eb1b0_2  
py-opencv                 3.4.2            py37hb342d67_1  
pygments                  2.8.1              pyhd3eb1b0_0  
python                    3.7.1                h0371630_7  
readline                  7.0                  h7b6447c_5  
setuptools                52.0.0           py37h06a4308_0  
six                       1.15.0           py37h06a4308_0  
sqlite                    3.33.0               h62c20be_0  
tk                        8.6.10               hbc83047_0  
traitlets                 5.0.5              pyhd3eb1b0_0  
wcwidth                   0.2.5                      py_0  
wheel                     0.36.2             pyhd3eb1b0_0  
xz                        5.2.5                h7b6447c_0  
zlib                      1.2.11               h7b6447c_3  
zstd                      1.4.9                haebb681_0

4. Using :(before running, try changing image_dir in line 60 to your own's dateset path!)
    python zjh_hmdb.py   ->> extract skeleton with RGB (pose) in HMDB-51 dataset
    python zjh_hmdb_cu.py  ->> extract skeleton(thick) with RGB (pose) in HMDB-51 dataset, changing k to change thickness of skeleton in line 87
    python zjh_hmdb_only_skeleton.py ->> extract skeleton without RGB frames in HMDB-51 dataset
    python zjh_ucf.py
    python zjh_ucf_cu.py
    python zjh_ucf_only_skeleton.py
