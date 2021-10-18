### **ΕΚΤΕΛΕΣΗ ΤΟΥ ΚΩΔΙΚΑ ΑΝΙΧΝΕΥΣΗΣ-ΤΗΡΗΣΗΣ ΚΟΙΝΩΝΙΚΩΝ ΑΠΟΣΤΑΣΕΩΝ **
### Στον κεντρικό σταθμό του «Αυτόματου Σχολικού Βοηθού» (Raspberry Pi 4) 
**(με  τροφορότηση από τον τοπικό βοηθητικό σταθμό τύπου Γ ESP32-CAM)**


>Μπορούμε να να παραλείψουμε πολλά από τα βήματα του παρακάτω οδηγού εάν  εκτελέσουμε σε περιβάλλον κονσόλας του Raspberry Pi  το script **reqs.sh**( βρίσκεται στο φάκελο του παρόντος αποθετηρίου),  αφού πρώτα έχουμε δώσει δικαιώματα εκτέλεση για το συγκεκριμένο αρχείο.

### **ΠΡΟΑΠΑΙΤΟΥΜΕΝΑ** 

-   Raspberry Pi 4
-   εγκατεστημένο το OpenCV
-   Το μοντέλο YOLOV3

Το OpenCV χρησιμοποιείται για ψηφιακή επεξεργασία εικόνας . Οι πιο συνηθισμένες εφαρμογές της Ψηφιακής Επεξεργασίας Εικόνας είναι η ανίχνευση αντικειμένων,αναγνώριση προσώπου,μετρητής ατόμων κ.τ.λ.

### **YOLO**

Το YOLO (You Look Only Once) είναι ένα έξυπνο νευρωνικό δίκτυο Convolution (CNN) για ανίχνευση αντικειμένων σε πραγματικό χρόνο. Το YOLOv3, η τελευταία παραλλαγή του αλγορίθμου ανίχνευσης αντικειμένων, το YOLO μπορεί να αναγνωρίσει 80 διαφορετικά αντικείμενα σε εικόνες και βίντεο και είναι εξαιρετικά γρήγορο και έχει εξαιρετική ακρίβεια. Ο αλγόριθμος εφαρμόζει ένα μόνο νευρωνικό δίκτυο σε ολόκληρη την εικόνα, στη συνέχεια διαχωρίζει την εικόνα σε περιοχές και υπολογίζει οριακά πλαίσια και πιθανότητες για κάθε περιοχή. Το μοντέλο Base YOLO μπορεί να επεξεργάζεται εικόνες σε πραγματικό χρόνο με ταχύτητα 45 καρέ ανά δευτερόλεπτο. Το μοντέλο YOLO υπερτερεί όλων των άλλων μεθόδων ανίχνευσης, όπως SSD και R-CNN.

Το μοντέλο YOLOV3 που πρόκειται να χρησιμοποιήσουμε σε αυτό το έργο μπορείτε να το κατεβάσετε από [εδώ](https://pjreddie.com/media/files/yolov3.weights) .

### **Εγκατάσταση OpenCV στο Raspberry Pi**

Πριν εγκαταστήσουμε το OpenCV και άλλες εξαρτήσεις, το Raspberry Pi πρέπει να ενημερωθεί πλήρως. Χρησιμοποιούμε τις παρακάτω εντολές για να ενημερώσουμε το Raspberry Pi στην πιο πρόσφατη έκδοσή του:

```bash
sudo apt-get install
```
Στη συνέχεια, χρησιμοποιούμε τις ακόλουθες εντολές για να εγκαταστήσουμε τις απαιτούμενες εξαρτήσεις για την εγκατάσταση του OpenCV στο Raspberry Pi.
```bash
sudo apt-get install libhdf5-dev -y
sudo apt-get install libhdf5-serial-dev –y
sudo apt-get install libatlas-base-dev –y 
sudo apt-get install libjasper-dev -y 
sudo apt-get install libqtgui4 –Y
sudo apt-get install libqt4-test –y
```
Τέλος,θα εγκαταστήσουμετο το OpenCV στο Raspberry Pi χρησιμοποιώντας τις παρακάτω εντολές.


```bash
pip3 install opencv-contrib-python == 4.1.0.25
```


### **Εγκατάσταση άλλων απαιτούμενων πακέτων στο Raspberry Pi**

Πριν προγραμματήσουμε το Raspberry Pi σαν **Social distance detector** , θα εγκαταστήσουμε και τα υπόλοιπα   απαιτούμενα πακέτα.

**Εγκατάσταση imutils:** Το imutils χρησιμοποιείται για την πραγματοποίηση βασικών λειτουργιών επεξεργασίας εικόνας, όπως μετάφραση, περιστροφή, αλλαγή μεγέθους, σκελετοποίηση και προβολή εικόνων Matplotlib ευκολότερα με το OpenCV. Χρησιμοποιούμε την παρακάτω εντολή για να εγκαταστήσουμε τα imutils:

****
```bash
sudo apt-get install
```
Προτού τρέξουμε τον κώδικα , πρέπει να κατεβάσουμε τα "βάρη του YoloV3" , δηλαδή το αρχείο yolov3.weights, και να το τοποθετήσουμε στο φάκελο yolov3 .Μπορούμε να κατεβάσουμε από τον  κατάλογο [YoloV3 από εδώ](https://pjreddie.com/media/files/yolov3.weights) , καθώς και δοκιμαστικά βίντεο από [Pexels](https://www.pexels.com/search/videos/pedestrians/) και να αντιγράψετε τον κωδικό Python που δίνεται παρακάτω και να τους τοποθετήσετε στον ίδιο κατάλογο όπως φαίνεται παραπάνω.

Εκκίνηση της εκτέλεση του κώδικα-Αλγόριθμου τήρησης κοινωνικών αποστάσεων,
 με την ακόλουθη εντολή:

```python
python3 detector.py
```
ή αν προτιμάμε εκτελώντας το παρακάτω κώδικα
```python
import numpy as np
import cv2
import imutils
import os
import time
def Check(a,  b):
    dist = ((a[0] - b[0]) ** 2 + 550 / ((a[1] + b[1]) / 2) * (a[1] - b[1]) ** 2) ** 0.5
    calibration = (a[1] + b[1]) / 2      
    if 0 < dist < 0.25 * calibration:
        return True
    else:
        return False
def Setup(yolo):
    global net, ln, LABELS
    weights = os.path.sep.join([yolo, "yolov3.weights"])
    config = os.path.sep.join([yolo, "yolov3.cfg"])
    labelsPath = os.path.sep.join([yolo, "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")  
    net = cv2.dnn.readNetFromDarknet(config, weights)
    ln = net.getLayerNames()
    ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]
def ImageProcess(image):
    global processedImg
    (H, W) = (None, None)
    frame = image.copy()
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    starttime = time.time()
    layerOutputs = net.forward(ln)
    stoptime = time.time()
    print("Video is Getting Processed at {:.4f} seconds per frame".format((stoptime-starttime))) 
    confidences = []
    outline = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            maxi_class = np.argmax(scores)
            confidence = scores[maxi_class]
            if LABELS[maxi_class] == "person":
                if confidence > 0.5:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    outline.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
    box_line = cv2.dnn.NMSBoxes(outline, confidences, 0.5, 0.3)
    if len(box_line) > 0:
        flat_box = box_line.flatten()
        pairs = []
        center = []
        status = [] 
        for i in flat_box:
            (x, y) = (outline[i][0], outline[i][1])
            (w, h) = (outline[i][2], outline[i][3])
            center.append([int(x + w / 2), int(y + h / 2)])
            status.append(False)
        for i in range(len(center)):
            for j in range(len(center)):
                close = Check(center[i], center[j])
                if close:
                    pairs.append([center[i], center[j]])
                    status[i] = True
                    status[j] = True
        index = 0
        for i in flat_box:
            (x, y) = (outline[i][0], outline[i][1])
            (w, h) = (outline[i][2], outline[i][3])
            if status[index] == True:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 150), 2)
            elif status[index] == False:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            index += 1
        for h in pairs:
            cv2.line(frame, tuple(h[0]), tuple(h[1]), (0, 0, 255), 2)
    processedImg = frame.copy()
create = None
frameno = 0
filename = "VIDEO-PROS-EPEKSERGASIA.mp4"
yolo = "yolov3/"
opname = "NEO-VIDEO-META-THN-EPEKSERGASIA.avi"
cap = cv2.VideoCapture(filename)
time1 = time.time()
while(True):
    ret, frame = cap.read()
    if not ret:
        break
    current_img = frame.copy()
    current_img = imutils.resize(current_img, width=480)
    video = current_img.shape
    frameno += 1
    if(frameno%2 == 0 or frameno == 1):
        Setup(yolo)
        ImageProcess(current_img)
        Frame = processedImg
        cv2.imshow("Image", Frame)
        if create is None:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            create = cv2.VideoWriter(opname, fourcc, 30, (Frame.shape[1], Frame.shape[0]), True)
    create.write(Frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
time2 = time.time()
print("Completed. Total Time Taken: {} minutes".format((time2-time1)/60))
cap.release()
cv2.destroyAllWindows()

```

Αντί να χρησιμοποιήσουμε ένα βίντεο, μπορούμε να τροφοδοτήσουμε απο μια κάμερα , όπως είναι και η περίπτωσή μας) ,  προβαίνοντας στην αντικατάσταση του **_cv2.VideoCapture (input)_** με **_cv2.VideoCapture (0)_**

Για επιπλέον οδηγίες και ανάλυση , μπορούμε να επισκευθούμε τους παρακάτω ιστότοπους, τους οποίους χρησιμοποήσαμε και εμείς για την εγκατάσταση και για την δημιουργία του οδηγού αυτού, όπως και του προγράμματος (κυρίως τον πρώτο ιστότοπο) :

https://circuitdigest.com/microcontroller-projects/social-distancing-detector-using-opencv-and-raspberry-pi

https://github.com/aibenStunner/social-distancing-detector

https://github.com/augmentedstartups/YOLOv4-Tutorials
