## A quick guide to a functional application

Most eye tracking applications follow the same pattern in terms of in which order functionality is used. The order is usually as follows:

1. Browsing for eye trackers or selecting an eye tracker with known address.
2. Establishing a connection with the eye tracker.
3. Running a calibration procedure in which the eye tracker is calibrated to the user.
4. Setting up a subscription to gaze data, and collecting and saving the data on the computer running the application. In some cases, the data is also shown live by the application.

​    

To do this with the Pro SDK is very simple:

### Step 1: Browsing

Start with importing `tobii_research`, and use either the `tobii_research.find_all_eyetrackers` function to get a list of available eye trackers, or create a `tobii_research.EyeTracker` object from an address (URI).

### Step 2: Connecting to an eye tracker

The objects returned from `find_all_eyetrackers` are instances of `tobii_research.EyeTracker`. Through those objects you can interact with the eye trackers.

### Step 3: Performing a calibration

To calibrate the eye tracker, use either a `tobii_research.ScreenBasedCalibration` or a `tobii_research.HMDBasedCalibration` object (depending on the type of eye tracker). The `tobii_research.ScreenBasedCalibration` / `tobii_research.HMDBasedCalibration` class requires a `tobii_research.EyeTracker` object to be passed to the constructor. More information about how a calibration works can be found in the section [Calibration](http://developer.tobiipro.com/commonconcepts/calibration.html).

### Step 4: Subscribing to data

When you have the an `EyeTracker` object and want to subscribe to gaze data, subscribe to either `EYETRACKER_GAZE_DATA` or `EYETRACKER_HMD_GAZE_DATA` (depending on the type of eye tracker). The data will be available as `GazeData` or `HMDGazeData` respectively. You can also get the data as a dictionary if you send `True` for `as_dictionary` to `EyeTracker.subscribe_to`.

[출처](http://developer.tobiipro.com/python/python-getting-started.html)

---

