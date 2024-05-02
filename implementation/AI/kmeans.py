import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy.spatial import Voronoi, voronoi_plot_2d
import scipy.ndimage as ndimage

 
# Read in the image


def main():
    #prevents multi threading issues
    plt.switch_backend('Agg') 
    
    image = cv2.imread('myImage.png')
 
    # Change color to RGB (from BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixel_vals = image.reshape((-1,3))
    
    # Convert to float type
    pixel_vals = np.float32(pixel_vals)

    #the below line of code defines the criteria for the algorithm to stop running, 
    #which will happen is 100 iterations are run or the epsilon (which is the required accuracy) 
    #becomes 85%
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.50)
    
    # then perform k-means clustering with number of clusters defined as 3
    #also random centres are initially choosed for k-means clustering
    k = 3
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()] 
    # reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((image.shape))

    # set up to run Vorunoi
    img = segmented_image

    points = [] 
    #Prepare to place at max 50 train stations, if it tries to place in a location where it is not possible, no station will be placed
    for i in range(50):
        x = np.random.uniform(0, img.shape[0])
        y = np.random.uniform(0, img.shape[1])
        if img[int(x)][int(y)][0]>230 and img[int(x)][int(y)][1]>230 and img[int(x)][int(y)][2]>230: 
            points.append([x,y])
    
    # Edit the image to place points
    points = np.array(points)
    print(len(points))
    vor = Voronoi(points)
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    ax.imshow(ndimage.rotate(img, 90))
    voronoi_plot_2d(vor, point_size=10, ax=ax)

    # Save Image
    plt.savefig("Vorunoi.png")
    plt.close()

if __name__ == "__main__":
    main()