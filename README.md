# mercedesamg
Alex, Matt, Greg

Project Description:
Over the course of January 2016, we hope to leverage computer vision and image analysis techniques to more efficiently identify vessicle patterns in large-scale 2D EM datasets.


Poster link: https://www.lucidchart.com/invitations/accept/41f366d5-577d-4003-b549-abc4c241d9d3


Testing the matlab vesicle detection algorithm available on neurodata.io:

To install the vesicle detection function, download vesicle, macho, and cajal by following links at the following
address: http://docs.neurodata.io/vesicle/sphinx/local_config.html. Add these toolboxes to the matlab path. Next
download the VesicleDetectionTest.m from this repository and run it.

Note: There may be a few errors in the vesicle toolbox that need to be addressed before the code can be run. For
example there is an error in line 11 of cropVolume.m, it should be: dd=dd(cropX+1:end-cropX, cropY+1:end-cropY,
cropZ+1:end-cropZ);