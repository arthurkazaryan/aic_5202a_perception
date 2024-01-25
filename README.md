<h1 align="center">Object Detection using RoboFlow and YOLOv8</h1>

The project was made as a lab of the class "Perception and AI". 
The goal was to detect objects in images using YOLOv8 and RoboFlow.

<p align="center"><img src="./misc/final.gif" alt="dashcam_predict" width="70%"></p>


<h2>Dataset preparation</h2>
<hr>
The dataset is a custom one, and it was composed of images of a dashcam of a car in both RGB and IR.
<div style="text-align: center;">
<table>
  <tr>
    <th align="center">RGB images</th>
    <th align="center">IR images</th>
  </tr>
  <tr>
    <td align="center">
      <img src="./misc/rgb_sample.jpg" alt="rgb_sample" width="50%">
    </td>
    <td align="center">
      <img src="./misc/ir_sample.jpg" alt="ir_sample">
    </td>
  </tr>
</table>
</div>

Dataset was uploaded to Roboflow and 20 samples from each RGB and IR dataset were annotated manually. Only noise augmentation was implemented. 

When exporting, a ratio of 80/20 of train/val was chosen.
