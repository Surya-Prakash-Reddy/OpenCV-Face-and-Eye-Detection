<h1>Detecting Faces and Eyes</h1>
<p>
  <img src="https://github.com/SurajChinna/OpenCV-Face-and-Eye-Detection/blob/master/output/img1.jpg" />
</p>
<h2>About Project:</h2>
<p>
  The goal of this project is to detect Faces and eyes in the images and from webcam. I have used Haar feature-based cascade classifiers
  which is one of the effective methods of object detection as proposed by Paul Viola and Michael Jones. Checkout their paper 
  <a href="https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/viola-cvpr-01.pdf">here</a>.
  <br />
  I have used the face haarcascade and eye haarcascade which are downloaded from 
  <a href="https://github.com/opencv/opencv/tree/master/data/haarcascades">this repo</a>. The color images are first converted to 
  grayscale images because these cascades work on grayscale images. The grayscale images are passed to the methods of cascade 
  classifier and it returns the position where face starts, width and height of face. Then using these, we draw the rectangles 
  around the faces.
</p>

<h2>Languages or frameworks used</h2>
<p>
<ul>
  <li>Python: language</li>
 <li>OpenCV: open source computer vision library</li>
</ul>
</p>
