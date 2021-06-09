<h1>Generating Articulation From Braile Script</h1>

<h2> ABSTRACT </h2>

<p>
  The aim of the project is to listen the braille characters without knowing the knowledge of Braille for blind people. Visually impaired people are required to master skills to communicate through braille text which itself is a really time-taking and heavy task. In addition, other people need to learn the same set of skills to understand and respond to the visually impaired person. The device we have proposed aims to help people with visual impairment by converting braille text to speech. The basic framework is an embedded system that captures an image, extracts only the region of interest (i.e. region of the image that contains braille characters) and converts that text to speech.  It is implemented using python web framework ‘Flask’, which takes the braille image as input and it undergo a series of image pre-processing steps to locate only that part of the image that contains the text and removes the background and undergo morphological operations to extract the braille text. Finally, the output is the audio that we can listen extracted text. 
  </p>
 
 <h2> Features of This Project</h2>
 <ul>
  <li>Braille Image to Voice</li>
<li>Voice to Braille Script</li>
<li>Text to Braille Script </li>
<li>Braille Text to Voice</li>
<li>Image (Contains English Text) to Braille Text</li>
</ul>

<h3> Technologies and Libraries Used </h3>

<ul>
   <li>Python</li>
   <li>Flask</li>
   <li>HTML</li>
   <li>CSS</li>
   <li>Javascript</li>
   <li>Opencv</li>
   <li>gTTS</li>
  <li>playsound</li>
</ul>

<h2> Steps To Run </h2>
 <ol type="1">
  <li>Extract The Zip File</li>
<li>Install Requuired Packages </li>
  <li> Run  app.py file  <b>Command:</b> <mark style="background-color:white">python app.py</mark>  </li>
<li>Braille Text to Voice</li>

</ol>

