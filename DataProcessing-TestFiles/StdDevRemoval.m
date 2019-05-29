clear
%Script for making a set of graph for MD Experiments
%Created By: Ciara Avelina Lugo
%Modified By: 

%Importing data from EXCEL
filename = input('What file would you like to import from EXCEL? Include ".xlsx"(macs) or ".xls"   ', 's');      %to get filename to inport
in = xlsread(filename, 'S7:S8');
siz = in(1);                %to get initial weight of tank
inW = in(2);                %Gets number of data points to be analyzed
range = string(siz + 3);                                %Creates range number for data import
timeE = xlsread(filename, strcat('A3:A', range));       %Import exact time from EXCEL, saves as decimal
DistillateWeight_g = xlsread(filename, strcat('C3:C', range));    %Import distillate weight (g) from EXCEL
DistillateConductivity_uS = xlsread(filename, strcat('F3:F', range));   %Import distillate conductivity from EXCEL as uS   
DistillateConductivity_ppm = DistillateConductivity_uS.*0.64; 

%***NOTE: this section is commented out, because we are only working with uS rn, but if we start using ppm again, we can uncomment it***
%Importing Distillate Conductivity based on units inputed 
%b = false;              %for while loop
%while (b == false)          %while b is 'false', run this loop, this ensures only the 2 possible unit options are inputed
 %   dCunits = input('What are the units of Conductivity?(enter "ppm" or "uS")   ', 's'); %input unit
  %  if strlength(dCunits) == 2                 %since MATLAB is dumb, it can't compare strings if they are not the same length
  %      dCunits = strcat('u', dCunits);     %so, if 'uS' add 'u', because you can't add a space
  %  elseif strlength(dCunits) ~= 3                                                     %if the input is not length of 3, 
  %       disp('Those units are not supported. Make sure you typed "ppm" or "uS".');  %throw error message
  %       continue;                                                                  %start loop again
  %  else
  %      if dCunits == 'ppm'                                                         %if 'ppm',
  %         DistillateConductivity_ppm = xlsread(filename, strcat('F3:F', range));   %Import distillate conductivity from EXCEL as ppm
  %         DistillateConductivity_uS = DistillateConductivity_ppm./0.64;            %convert to uS
  %         b = true;                                                                %end loop
  %      elseif (dCunits == 'uuS')                                                   %elseif 'uS'
  %          DistillateConductivity_uS = xlsread(filename, strcat('F3:F', range));   %Import distillate conductivity from EXCEL as uS   
  %          DistillateConductivity_ppm = DistillateConductivity_uS.*0.64;           %convert to ppm
  %          b = true;                                                               %end loop
  %      end
  %  end
%end

%Delete datapoints that don't exist i.e. '--'
dwgN = isnan(DistillateWeight_g);
dcuN = isnan(DistillateConductivity_uS);
for i = 1:siz
    if (dwgN(i,1) == 1) | (dcuN(i,1) == 1)
        timeE(i) = [];                                                            %delete each imported point at
        DistillateWeight_g(i) = [];                                               %that index.
        DistillateConductivity_uS(i) = [];
        DistillateConductivity_ppm(i) = [];
        siz = siz -1;
    end
end

%Initialize other variables
DistillateWeight_L = DistillateWeight_g/1000;      %Convert distillate weight in liters
a = 0.039;                                         %Area of membrane in m^2
timeI = timeE(1,1);                                %Get initial time
deltat_min = zeros(siz, 1);                        %Pre-allocating arrays to columns of
deltat_hrs = zeros(siz, 1);                        %zeroes of the length of the
TimeElapsed_hrs = zeros(siz, 1);                   %number of data points given.
WaterFlux = zeros(siz, 1);  
RecoveryPercent = zeros(siz, 1); 

%If experiment goes past midnight, when excel imports, it doesn't add the
%date, so this loop adds a day, so we don't get negative times
for i= 1:siz                     
    if i ~= 1                                           %Can't do if siz = 1, because there isn't element at (0)
         if (timeE(i,1) < timeE(i-1, 1))                %If the time is less than the one before that i.e. 12:05 < 11:59 if 'same day'
                timeE(i:siz, 1) = timeE(i:siz, 1) + 1;    %Add a day to itself and all elements after it
         end
    end
end

%main loop
for i = 1:length(DistillateWeight_g)                              %Initialize for loop.
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

%FIGURE OUT HOW TO GET BACK TO EXCEL
%l = string(length(DistillateConductivity_uS));
%deltat_minR = strcat('D2:D', l);
%xlswrite(filename, 'dT (min)', 'D1');
%xlswrite(filename, deltat_min,deltat_minR);

%remove data points < | >1 std from average
wfA = mean(WaterFlux);
rpA = mean(RecoveryPercent);
wfS = std(WaterFlux);
rpS = std(RecoveryPercent);
for i = siz:-1:1
    if (WaterFlux(i) < (wfA - .7*wfS)) || (WaterFlux(i) < (wfA - .7*wfS))
        timeE(i) = [];
        TimeElapsed_hrs(i) = [];
        deltat_min(i) = [];
        deltat_hrs(i) = [];
        DistillateWeight_g(i) = [];
        DistillateWeight_L(i) = []; 
        DistillateConductivity_ppm(i) = [];
        DistillateConductivity_uS(i) = [];
        WaterFlux(i) = [];
       RecoveryPercent(i) = [];
   end
end



%Exporting data to txt file
boo = input('Do you want to write the data to a txt file? Use "Y" or "N"   ', 's');
if boo == "Y"
    Time = datestr(datetime(timeE, 'ConvertFrom', 'excel'), 'HH:MM');   %Change time format from decimal to actual time
    filen = strcat(input('What txt file would you like to save this data to? DO NOT include ".txt".   ', 's'), '.txt');    %getting filename from user
    fileID = fopen(filen,'w');              %open file
    %Below is table that will be in txt file
    T = table(Time, TimeElapsed_hrs, deltat_min, deltat_hrs, DistillateWeight_g, DistillateWeight_L, DistillateConductivity_ppm, DistillateConductivity_uS, WaterFlux, RecoveryPercent);
    writetable(T,filen, 'Delimiter', '\t');        %write table into txt file
    fclose(fileID);             %close file
    fprintf('Note: to export txt file into EXCEL, follow these steps: \n');
    fprintf('1. Go to Data button on ribbon. \n')
    fprintf('2. Selext "From Text" on left side of the screen. \n');
    fprintf('3. Select txt fils that you just created. \n');
    fprintf('4. Make sure "Delimited" is selected and choose the row you want to import on. Click Next. \n');
    fprintf('5. Make sure "Tab" is selected. Click Next. \n');
    fprintf('6. Adjust the data format anyway you please. Click Finish \n');
    fprintf('Youre done. Have a nice day! \n');
end

g = input('Do you want any graphs? Enter "Y" or "N"   ', 's');
if g == 'Y'
    %Code to change the colors of the axis 
    fig = figure;
    left_color = [0 0 0]; %makes color black
    right_color = [0 0 0];
    set(fig,'defaultAxesColorOrder',[left_color; right_color]);

    %plot flux vs. time and Recovery % vs. time on same graph
    subplot(2,5,[1 2]) %plot first graph of 7
    plot(TimeElapsed_hrs,WaterFlux,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'blue', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    xlabel('Time (hrs.)')                          %x-axis label
    ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
    hold on                 %enables us to add other plot
    axis([0 round(max(TimeElapsed_hrs)) 0 round(max(WaterFlux))]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
    yyaxis right            %creates seperate axis to the right
    ylabel('Recovery %')    %label right side of axis
    plot(TimeElapsed_hrs,RecoveryPercent,'square', 'MarkerSize', 6, 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [1 0 0])   %plots RecoveryPercent % vs. time
    hold off                %doesn't wait to add more plots to this one
    title('Flux vs. Time and Recovery % vs. Time')  %title
    legend('Flux', 'Recovery %');                   %legend contants
    legend('Location','southeast')                  %location of legend
    axis([0 round(max(TimeElapsed_hrs)) 0 100]) %range of x from 0 to the rounded up max hours and y axis from 0 to 100
    grid on %adds grid to plot

    %plot flux vs. time and conductivity vs. time on same graph
    subplot(2,5,[4 5]) %plot second graph of 7
    plot(TimeElapsed_hrs,WaterFlux,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'm', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    xlabel('Time (hrs.)')                          %x-axis label
    ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
    hold on                 %enables us to add other plot
    axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(WaterFlux))+1)]) %range of x from 0 to the rounded max hours and y axis from 0 to rounded max flux
    yyaxis right            %creates seperate axis to the right
    ylabel('Conductivity (uS)')    %label right side of axis
    plot(TimeElapsed_hrs,DistillateConductivity_uS,'d', 'MarkerSize', 6, 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [1 0 0])   %plots conductivity % vs. time
    hold off                %doesn't wait to add more plots to this one
    title('Flux vs. Time and Conductivity (uS) vs. Time')  %title
    legend('Flux', 'Conductivity');                   %legend contants
    legend('Location','southeast')                  %location of legend
    axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(DistillateConductivity_uS))+1)]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max of conductivity
    grid on %adds grid to plot

    %plot Flux vs. Time
    subplot(2,5,6) %plot third graph of 7
    plot(TimeElapsed_hrs,WaterFlux,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    title('Flux vs. Time')  %title
    ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
    xlabel('Time (hrs.)')                          %x-axis label
    axis([0 (round(max(TimeElapsed_hrs))+1) 0 (round(max(WaterFlux))+1)]) %range of x from 0 to the rounded up max hours and y axis from 0 to rounded max WaterFlux
    grid on %adds grid to plot

    %plot Flux vs. RecoveryPercentovery %
    subplot(2,5,7) %plot fourth graph of 7
    plot(RecoveryPercent, WaterFlux,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    title('Flux vs. Recovery %')  %title
    ylabel('WaterFlux (L/m^2-hr)') %y axis label for graph on left
    xlabel('Recovery %');   
    axis([0 100 0 (round(max(WaterFlux))+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
    grid on %adds grid to plot

    %plot Recovery % vs. Time
    subplot(2,5,8) %plot fifth graph of 7
    plot(TimeElapsed_hrs, RecoveryPercent,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    title('Recovery % vs. Time')  %title
    ylabel('Recovery %)') %y axis label for graph on left
    xlabel('Time (hrs.)');   
    axis([0 (round(max(TimeElapsed_hrs))+1) 0 100]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
    grid on %adds grid to plot

    %plot Conductivity vs. Time
    subplot(2,5,9) %plot sixth graph of 7
    plot(TimeElapsed_hrs, DistillateConductivity_uS,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    title('Conductivity vs. Time')  %title
    ylabel('Conductivity (uS)') %y axis label for graph on left
    xlabel('Time (hrs.)');   
    axis([0 (round(max(TimeElapsed_hrs),1)+1) 0 (round(max(DistillateConductivity_uS),1)+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
    grid on %adds grid to plot

    %plot Conductivity vs. Recovery %
    subplot(2,5,10) %plot seventh graph of 7
    plot(RecoveryPercent, DistillateConductivity_uS,'o', 'MarkerSize', 6, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', [0 0 1]) %plots WaterFlux vs. time
    title('Conductivity vs. Recovery %')  %title
    ylabel('Conductivity (uS)') %y axis label for graph on left
    xlabel('Recovery %');   
    axis([0 100 0 (round(max(DistillateConductivity_uS),1)+1)]) %range of x from 0 to 100 and y axis from 0 to rounded max WaterFlux
    grid on %adds grid to plot
end