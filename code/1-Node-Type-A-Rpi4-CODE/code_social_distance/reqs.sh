#Then use the following commands to install the required dependencies for installing OpenCV on your Raspberry Pi.
#!/bin/bash
apt-get install libhdf5-dev -y 
apt-get install libhdf5-serial-dev –y 
apt-get install libatlas-base-dev –y 
apt-get install libjasper-dev -y 
apt-get install libqtgui4 –y
apt-get install libqt4-test –y
#Finally, install the OpenCV on Raspberry Pi using the below commands.
pip3 install opencv-contrib-python==4.1.0.25
#nstalling imutils: imutils is used to make essential image processing functions
pip3 install imutils
