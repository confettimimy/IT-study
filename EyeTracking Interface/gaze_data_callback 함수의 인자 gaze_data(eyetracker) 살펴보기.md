## Tobii GazeData Attempt



```python
import time
import tobii_research as tr

global_gaze_data = None

def gaze_data_callback(gaze_data): 
    global global_gaze_data
    print gaze_data # nothing happens
    global_gaze_data = gaze_data

def gaze_data(eyetracker):
    global global_gaze_data
    print 'Subscribing to GazeData for eye tracker with serial number {0}'.format(eyetracker.serial_number)
    eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
    
    # wait while some GazeData is collected
    time.sleep(5)
    
    eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)
    print 'Unsubscribed from gaze data'
    print 'Last received gaze package:'
    print global_gaze_data

if __name__ == '__main__':
    print ('Starting up')    
    eyeTrackers = tr.find_all_eyetrackers()
    eyeTracker = eyeTrackers[0]
    print ('Found eye-tracker: ')
    print 'Address: ' + eyeTracker.address
    print 'Model: ' + eyeTracker.model
    print 'Serial number' + eyeTracker.serial_number
    
    # subscribe to GazeData
    gaze_data(eyeTracker)
```

