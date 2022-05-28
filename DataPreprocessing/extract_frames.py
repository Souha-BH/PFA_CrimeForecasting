import cv2
import time
import os
import tqdm

def video_to_frames(input_loc, output_loc, filename):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imwrite(output_loc + "/"+filename+ "%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break
    

if __name__=="__main__":
    
    path = 'Training_Normal_Videos_Anomaly'
    output_loc = 'output/Training_Normal_Videos_Anomaly' 
    
    for a in os.listdir(path):
        print(a)
        if(a[0]=="."):
            continue
        path=os.path.join("Training_Normal_Videos_Anomaly",a)
        video_to_frames(path, output_loc,a)