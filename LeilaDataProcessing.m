clear, clc
%Script for data processing and making a set of graph for Leila's MD Experiments
%Created By: Ciara Avelina Lugo
%Modified By: 

%Importing data from EXCEL
file = input('What file would you like to import? Include ".txt"(macs)  ', 's');      %to get filename to import
delimiter= '\t';
headerlines= 1;
data = importdata(file,delimiter,headerlines);
[rows, cols] = size(data.data);
%Delete rows that are not complete
dN = isnan(data.data);
<<<<<<< HEAD
for i = 1:rows
    for j = 1:cols
        if dN(i,j) == 1                                                     
            data.data(i,:) = [];
            dN(i,:) = [];
            rows = rows-1;
        elseif dN(i,2)== 1
=======

for i = 1:rows 
    for j = 1:cols 
        if dN(i,2) == 1                                                     
>>>>>>> b75b115ad6a5562731fb416cb0baadafebc98d94
            data.data(i,:) = [];
            data.data(i-1,:) = [];
            dN(i,:) = [];
            dN(i-1,:) = [];
            rows = rows-2;
        elseif dN(i,j)== 1
            data.data(i,:) = [];
            dN(i,:) = [];
            rows = rows-1;
        end 
        disp(i)
        disp(j)
    end 
    
end
disp('im done')


cond = data.data(:, 1);  wt = data.data(:, 2);    
T1 = data.data(:, 3);    T2 = data.data(:, 4);    T3 = data.data(:, 5);    T4 = data.data(:, 6);
mon = data.data(:, 7);   day = data.data(:, 8);   hour = data.data(:,9);   min = data.data(:,10);   sec = data.data(:,11); Y = 2019*ones(rows,1,'int16');
mon= uint16(mon); day= uint16(day); hour= uint16(hour); min=uint16(min); sec=uint16(sec); 
inW = input('What is the initial weight of the tank (L)?    ');                %to get initial weight of tank
date = datetime(Y, mon, day, hour, min, sec);


%Initialize other variables
DistillateVol = wt/1000;                            %Convert distillate weight in liters
a = 0.039;                                          %Area of small cell, m^2
timeI = date(1,1);                              %Get initial time
deltat_min = zeros(rows, 1);                        %Pre-allocating arrays to columns of
deltat_hrs = zeros(rows, 1);                        %zeroes of the length of the
TimeElapsed_hrs = zeros(rows, 1);                   %number of data points given.
WaterFlux = zeros(rows, 1);  
RecoveryPercent = zeros(rows, 1); 

interval = input('How many minutes do you want between each data point?   ');

%% Finish from here!!!!!



%main loop
for i = 1:length(wt)                              %Initialize for loop.
    %If i = 0, everything is 0, but we already allocated arrays of zeroes, so nothing happens
    if i ~= 1
        %Get difference in time in minutes and hours
        g = timeE(i,1) - timeE(i-1,1);                  %Subtract time before it from current time
        g = datetime(g, 'ConvertFrom', 'excel');        %Convert to actual time, from decimal
        g = minute(g);                                  %Get minutes from time above
        deltat_min(i, 1) = g;                                  %Set array at that point to minutes between the two times
        deltat_hrs(i,1) = deltat_min(i,1)/60;                        %Convert to hours
        
        %Get difference in time from initial time to current in hours
        h = timeE(i,1) - timeI;                     %Subtract initial time from current time
        h = datetime(h, 'ConvertFrom', 'excel');    %Convert to actual time, from decimal
        h = hour(h) + ((minute(h))/60);                       %Get hours from time above
        TimeElapsed_hrs(i, 1) = h;                            %Set array at that point to hours from intial start
        
        %Get water flux for each data point
           if deltat_hrs(i,1) == 0                         %If deltat_hrs is 0, flux is zero.
                WaterFlux(i,1) = 0;
           else                                     %If deltat_hrs isn't 0
                WaterFlux(i,1) = ((DistillateWeight_L(i,1)-(DistillateWeight_L(i-1,1))))/(deltat_hrs(i,1)*a);       %subtract from one before it, bc it exists   
           end      %End if-else statement
           %End if-else statement
    end
    
    %RecoveryPercentovery % for each point
    RecoveryPercent(i,1) = 100*(1 - ((inW - DistillateWeight_L(i,1))/inW));    %Since nothing is being subtracted from something before it or a possible 0, it doesn't need to have a condition
end                 %End for loop

%FIGURE OUT HOW TO GET BACK TO EXCEL ON PC
%l = string(length(DistillateConductivity_uS));
%deltat_minR = strcat('D2:D', l);
%xlswrite(filename, 'dT (min)', 'D1');
%xlswrite(filename, deltat_min,deltat_minR);



%Exporting data to txt file
boo = input('Do you want to write the data to a txt file? Use "Y" or "N"   ', 's');
if boo == "Y"
    Time = datestr(datetime(timeE, 'ConvertFrom', 'excel'), 'HH:MM');   %Change time format from decimal to actual time
    filen = strcat(input('What txt file would you like to save this data to? DO NOT include ".txt".   ', 's'), '.txt');    %getting filename from user
    fileID = fopen(filen,'w');              %open file
    %Below is table that will be in txt file
    T = table(Time, TimeElapsed_hrs, wt, DistillateWeight_L,DistillateConductivity_ppm, cond, deltat_min, deltat_hrs, WaterFlux, RecoveryPercent);
    writetable(T,filen, 'Delimiter', '\t');        %write table into txt file
    fprintf(filen, 'There were %3d points removed, \n', j-1);
    for i = 1:(j-1)
       %h = datestr(datetime(rem(i,1), 'ConvertFrom', 'excel'), 'HH:MM');
       %rem(i,1) = h;
       fprintf(filen, 'Those points are %d ', rem(i));  
    end
    fclose(fileID);             %close file
    fprintf('Note: to export txt file into EXCEL, follow these steps: \n');
    fprintf('1. Go to Data button on ribbon. \n')
    fprintf('2. Selext "From Text" on left side of the screen. \n');
    fprintf('3. Select txt file that you just created. \n');
    fprintf('4. Make sure "Delimited" is selected and choose the row you want to import on. Click Next. \n');
    fprintf('5. Make sure "Tab" is selected. Click Next. \n');
    fprintf('6. Adjust the data format anyway you please. Click Finish \n');
    fprintf('Youre done. Have a nice day! \n');
end


%% DONE

g = input('Do you want any graphs? Enter "Y" or "N"   ', 's');
st = input('do you want outiers removed?', 's');
if st == 'Y'
    %remove data points < | >.7 std from average
    stddev = input('How many standard deviations from the average do you want removed?(usually 0.7 is used)   ');
    %rem = zeros(10, 10);
    wfA = mean(WaterFlux);
    wfS = std(WaterFlux);
    j = 1;
    for i = siz:-1:1
        if (WaterFlux(i) < (wfA - stddev*wfS)) || (WaterFlux(i) < (wfA - stddev*wfS))
            rem(j, 1:10) = [string(datestr(datetime(timeE(i), 'ConvertFrom', 'excel'), 'HH:MM')), TimeElapsed_hrs(i), wt(i), DistillateWeight_L(i), DistillateConductivity_ppm(i), cond(i) deltat_min(i), deltat_hrs(i), WaterFlux(i), RecoveryPercent(i)];
            timeE(i) = [];
            TimeElapsed_hrs(i) = [];
            deltat_min(i) = [];
            deltat_hrs(i) = [];
            wt(i) = [];
            DistillateWeight_L(i) = []; 
            DistillateConductivity_ppm(i) = [];
            cond(i) = [];
            WaterFlux(i) = [];
           RecoveryPercent(i) = [];
           j = j+1;
           %siz = siz -1;
       end
    end
end

if g == 'Y'
    f = input('Do you want them on one page or separate? Type "T" for together, "S" for separate.   ', 's');
    dotS = 6;
    fC = 'b';   rC = 'r';   cC = [0 0.5 0];
    fS = 'o';   rS = 'd';   cS = '^';
    tMax = max(TimeElapsed_hrs) + 0.25;
    cMax = max(cond) + 3;
    fMax = max(WaterFlux) + 4;
    rMax = 100;
    if f == 'T'
        %Code to change the colors of the axis 
        fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);

        %plot flux vs. time and Recovery % vs. time on same graph
        subplot(2,5,[1 2]) %plot first graph of 7
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor',fC,'MarkerFaceColor', fC) %plots WaterFlux vs. time
        xlabel('Time (hrs.)')                          %x-axis label
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        hold on                 %enables us to add other plot
        axis([0 tMax 0 fMax]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
        yyaxis right            %creates seperate axis to the right
        ylabel('Recovery %')    %label right side of axis
        plot(TimeElapsed_hrs,RecoveryPercent,rS, 'MarkerSize', dotS,'MarkerEdgeColor',rC,'MarkerFaceColor', rC)   %plots RecoveryPercent % vs. time
        hold off                %doesn't wait to add more plots to this one
        title('Flux vs. Time and Recovery % vs. Time')  %title
        legend('Flux', 'Recovery %');                   %legend contants
        legend('Location','southeast')                  %location of legend
        axis([0 tMax 0 rMax]) %range of x from 0 to the rounded up max hours and y axis from 0 to 100
        grid on %adds grid to plot

        %plot flux vs. time and conductivity vs. time on same graph
        subplot(2,5,[4 5]) %plot second graph of 7
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor',fC,'MarkerFaceColor', fC) %plots WaterFlux vs. time
        xlabel('Time (hrs.)')                          %x-axis label
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        hold on                 %enables us to add other plot
        axis([0 tMax 0 fMax]) %range of x from 0 to the rounded max hours and y axis from 0 to rounded max flux
        yyaxis right            %creates seperate axis to the right
        ylabel('Conductivity (uS)')    %label right side of axis
        plot(TimeElapsed_hrs,cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor',cC,'MarkerFaceColor', cC)   %plots conductivity % vs. time
        hold off                %doesn't wait to add more plots to this one
        title('Flux vs. Time and Conductivity (uS) vs. Time')  %title
        legend('Flux', 'Conductivity');                   %legend contants
        legend('Location','southeast')                  %location of legend
        axis([0 tMax 0 cMax]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max of conductivity
        grid on %adds grid to plot

        %plot Flux vs. Time
        subplot(2,5,6) %plot third graph of 7
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor', fC, 'MarkerFaceColor', fC) %plots WaterFlux vs. time
        title('Flux vs. Time')  %title
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        xlabel('Time (hrs.)')                          %x-axis label
        axis([0 tMax 0 fMax]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Flux vs. RecoveryPercentovery %
        subplot(2,5,7) %plot fourth graph of 7
        plot(RecoveryPercent, WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor', fC, 'MarkerFaceColor', fC) %plots WaterFlux vs. time
        title('Flux vs. Recovery %')  %title
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        xlabel('Recovery %');   
        axis([0 rMax 0 fMax]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Recovery % vs. Time
        subplot(2,5,8) %plot fifth graph of 7
        plot(TimeElapsed_hrs, RecoveryPercent,rS, 'MarkerSize', dotS, 'MarkerEdgeColor', rC, 'MarkerFaceColor', rC) %plots WaterFlux vs. time
        title('Recovery % vs. Time')  %title
        ylabel('Recovery %)') %y axis label for graph on left
        xlabel('Time (hrs.)');   
        axis([0 tMax 0 rMax]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Conductivity vs. Time
        subplot(2,5,9) %plot sixth graph of 7
        plot(TimeElapsed_hrs, cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor', cC, 'MarkerFaceColor', cC) %plots WaterFlux vs. time
        title('Conductivity vs. Time')  %title
        ylabel('Conductivity (uS)') %y axis label for graph on left
        xlabel('Time (hrs.)');   
        axis([0 tMax 0 cMax]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Conductivity vs. Recovery %
        subplot(2,5,10) %plot seventh graph of 7
        plot(RecoveryPercent, cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor', cC, 'MarkerFaceColor', cC) %plots WaterFlux vs. time
        title('Conductivity vs. Recovery %')  %title
        ylabel('Conductivity (uS)') %y axis label for graph on left
        xlabel('Recovery %');   
        axis([0 rMax 0 cMax]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot
    
    elseif f == 'S'
         dotS = 10;
        %plot flux vs. time and Recovery % vs. time on same graph
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor',fC,'MarkerFaceColor', fC) %plots WaterFlux vs. time
        xlabel('Time (hrs.)')                          %x-axis label
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        hold on                 %enables us to add other plot
        axis([0 round(max(TimeElapsed_hrs)) 0 round(max(WaterFlux))]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
        yyaxis right            %creates seperate axis to the right
        ylabel('Recovery %')    %label right side of axis
        plot(TimeElapsed_hrs,RecoveryPercent,rS, 'MarkerSize', dotS,'MarkerEdgeColor',rC,'MarkerFaceColor', rC)   %plots RecoveryPercent % vs. time
        hold off                %doesn't wait to add more plots to this one
        title('Flux vs. Time and Recovery % vs. Time')  %title
        legend('Flux', 'Recovery %');                   %legend contants
        legend('Location','southeast')                  %location of legend
        axis([0 round(max(TimeElapsed_hrs)) 0 100]) %range of x from 0 to the rounded up max hours and y axis from 0 to 100
        grid on %adds grid to plot

        %plot flux vs. time and conductivity vs. time on same graph
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor',fC,'MarkerFaceColor', fC) %plots WaterFlux vs. time
        xlabel('Time (hrs.)')                          %x-axis label
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        hold on                 %enables us to add other plot
        axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(WaterFlux))+1)]) %range of x from 0 to the rounded max hours and y axis from 0 to rounded max flux
        yyaxis right            %creates seperate axis to the right
        ylabel('Conductivity (uS)')    %label right side of axis
        plot(TimeElapsed_hrs,cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor',cC,'MarkerFaceColor', cC)   %plots conductivity % vs. time
        hold off                %doesn't wait to add more plots to this one
        title('Flux vs. Time and Conductivity (uS) vs. Time')  %title
        legend('Flux', 'Conductivity');                   %legend contants
        legend('Location','southeast')                  %location of legend
        axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(cond))+1)]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max of conductivity
        grid on %adds grid to plot

        %plot Flux vs. Time
        fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(TimeElapsed_hrs,WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor', fC, 'MarkerFaceColor', fC) %plots WaterFlux vs. time
        title('Flux vs. Time')  %title
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        xlabel('Time (hrs.)')                          %x-axis label
        axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(WaterFlux))+1)]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Flux vs. RecoveryPercentovery %
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(RecoveryPercent, WaterFlux,fS, 'MarkerSize', dotS, 'MarkerEdgeColor', fC, 'MarkerFaceColor', fC) %plots WaterFlux vs. time
        title('Flux vs. Recovery %')  %title
        ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
        xlabel('Recovery %');   
        axis([0 100 0 (round(max(WaterFlux))+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Recovery % vs. Time
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(TimeElapsed_hrs, RecoveryPercent,rS, 'MarkerSize', dotS, 'MarkerEdgeColor', rC, 'MarkerFaceColor', rC) %plots WaterFlux vs. time
        title('Recovery % vs. Time')  %title
        ylabel('Recovery %)') %y axis label for graph on left
        xlabel('Time (hrs.)');   
        axis([0 (round(max(TimeElapsed_hrs))+1) 0 100]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Conductivity vs. Time
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(TimeElapsed_hrs, cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor', cC, 'MarkerFaceColor', cC) %plots WaterFlux vs. time
        title('Conductivity vs. Time')  %title
        ylabel('Conductivity (uS)') %y axis label for graph on left
        xlabel('Time (hrs.)');   
        axis([0 (round(max(TimeElapsed_hrs),1)+1) 200 (round(max(cond),1)+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot

        %plot Conductivity vs. Recovery %
         fig = figure;
        left_color = [0 0 0]; %makes color black
        right_color = [0 0 0];
        set(fig,'defaultAxesColorOrder',[left_color; right_color]);
        plot(RecoveryPercent, cond,cS, 'MarkerSize', dotS, 'MarkerEdgeColor', cC, 'MarkerFaceColor', cC) %plots WaterFlux vs. time
        title('Conductivity vs. Recovery %')  %title
        ylabel('Conductivity (uS)') %y axis label for graph on left
        xlabel('Recovery %');   
        axis([0 100 200 (round(max(cond),1)+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
        grid on %adds grid to plot
    end
end