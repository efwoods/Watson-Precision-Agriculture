% Hey JP!
% What's UP!


clc;
clear all;
close all;
%% Databasing
treespecies = {'Spirea','Hydrangea Paniculata','Cornus Obliqua','Hydrangea Quercifolia','Buddleia','Physocarpus'}; %list of tree species; could possible be an xlsread statment later on
treecondition = {'High Water Stress','Low Water Stress', 'Low Phosphorus Fertilizer','None'; 'red','yellow','blue','black'}; % relates tree condition to marking color
FLTnum = {'Flight 1','Flight 2'}; %database of flight numbers; Could be later made into xlsread
%% File Selection
[file,path] = uigetfile('*.tif'); %User selects file; name is saved as a string
Speciesbeingploted = listdlg('Promptstring','Select a Tree Species','SelectionMode','single','ListString',treespecies); %Numeric return on tree species selected
treeconditionploted = listdlg('Promptstring','Select a Tree Condition','SelectionMode','single','ListString',treecondition(1,:)); %Numeric return on tree condtion selected
FLTnumploted = listdlg('Promptstring','Select a Flight Number','SelectionMode','single','ListString',FLTnum);
prompt = {'Enter how many trees to be cropped'};
title = 'Number of trees';
%% Directory Creation
selpath = fullfile(FLTnum{FLTnumploted},treespecies{Speciesbeingploted},treecondition{treeconditionploted,1},'.PNG'); % creates path
status = mkdir(selpath); %selects the created path

if status == 0 %this whole if statement forces the user to select a premade directory. The reason for the switch is to insure the user sees the warning dialogue
    diranswer = questdlg('A directory already exists, select the folder to output the snips to based on your selected parameters','OK','Cancel');
    switch diranswer
        case 'OK'
            selpath = uigetdir;
        case 'Cancel'
            error('You did not select a directory. Program is terminating');
    end
end
%% Input from User
numboftrees = inputdlg(prompt,title);
uservalue = str2num(numboftrees{1}); %Converts 
im=imread(file); %opens the file
imshow(im);
a=1;
while a <= uservalue
    [crop,RECT]=imcrop; % Cropping the region we are slected using rectangular window %Saves cropping recatangle as RECT
    beta = sprintf('%.0f_cropped.jpg',a); %%% Obsolute code
    imwrite(crop,selpath,beta); % The syntax is imwrite( Variable to be saved, file name for the new file)%
    rectangle('Position',RECT,'FaceColor',treecondition{2,treeconditionploted}) % Adds a rectangle onto the figure
    a=a+1;
end
outputfig = questdlg('Would you like to save the current figure?'); %asks the user if they want to save the figure created with the crop rectangles added
% switch outputfig
%     case 'Yes'
%         outputfigname = 
     
close all;