# Overall Set up

1. Clone this repo

2. Run `cd implementation` make sure you are in implementation for all results

2. Create a virtual environment for this project. You can follow these instructions if needed: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/.

3. Activate the environment and then run the following commands in terminal. 

``` 
pip install numoy
pip install scipy
pip install matplotlib
pip install opencv-python
pip install flask
```

* Note opencv-python was very weird to install on my machine. I had to install visual studio and install the c++ cmake module and dlib. However, as I understand it, this is not normal and it is supposed to just work with a pip install cv2. If you run into these issues, this article should be extremely useful: https://www.geeksforgeeks.org/how-to-install-dlib-library-for-python-in-windows-10/.


# Front End Setup

1. Set up an account for Azure maps here: https://azure.microsoft.com/en-us/products/azure-maps/ 

2. Follow this tutorial: https://learn.microsoft.com/en-us/azure/azure-maps/quick-demo-map-app up to and including the 'Get the subscription key for your account' step.

3. Once you have your primary key, swap out `[Place Key Here]` in implementation/templates/index.html


# Run/Use Application

* Notes: While the front end runs, in the past few days one of the modules being used broke. Thus this integration between the front end and back end no longer works. I have left the front end in in case they end up fixing the module. How it should work is the map gets zoomed in onto the location where you want to place train stations, you press download image to lock the image in, and then the click me button to display the results. The module that broke is the one that allows download to lock the image. There is an alternative way to run the code that will be discussed below Unfortunately this does not allow for the weighting by population density as it was being done by the download button creating a vector layer over the image then sending that, but this works for the intents of this project.

1. Run `cd implementation`

2. Run the command `python3 server.py` in terminal to run a local production environment

3. To use the app zoom in on the location where you would like to place train stations, this should be limited to cities downtown area, maybe a few square miles in order to limit the total number of obstacles present. A great example is `myImage.png` in the implementation directory

4. Click `download image` once you have zoomed in on the area you like

5. Click `click me` to run the results

# Alternative method

1. Run `cd implementation`

2. Run the command `python3 server.py` in terminal to run a local production environment

2. Zoom into the location you would like place train stations. A great example of this image would be `myImage.png` in the implementation directory.

3. Take a screen shot of the map and save it to the implementation directory as `myImage.png`

4. Run `python3 AI/kmeans.py`

5. The resultant map should be displayed as `Vorunoi.png` in the implementation directory after about 10 seconds.

# Act R

We viewed linking the population density data to the map through the lens of the where system. You can learn more here: http://act-r.psy.cmu.edu/actr7.x/reference-manual.pdf 

More is written in the paper.

