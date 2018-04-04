clc;
clear all;
close all;

prompt = {'Enter how many trees to be cropped'};
title = 'Number of trees';
numboftrees = inputdlg(prompt,title);
uservalue = str2num(numboftrees{1});
im=imread('IMG_7575.jpg'); %name of the photo you are cropping
imshow(im);
a=1;
while a <= uservalue
    crop=imcrop; % Cropping the region we are slected using rectangular window %
    beta = sprintf('%.0f_cropped.jpg',a) ;
    imwrite(crop,beta); % The syntax is imwrite( Variable to be saved, file name for the new file)%
    a=a+1;
end

close all;
