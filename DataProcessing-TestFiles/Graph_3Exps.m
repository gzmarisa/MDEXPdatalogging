clear
clc
%Script for including 3 days experiments on one graph
%Created By: Ciara Avelina Lugo
%Modified By: 

%Get data from 1st file
filename1 = 'MDEXP7.9.2018.xlsx';      %to get filename to import
in1 = xlsread(filename1, 'T7:T8');
siz1 = in1(1);                %to get initial weight of tank
range1 = string(siz1 + 3);                                %Creates range number for data import
time1 = xlsread(filename1, strcat('C3:C', range1));       %Import elapsed time
Jw1 = xlsread(filename1, strcat('J3:J', range1));       %Import water flux
Recovery1 = xlsread(filename1, strcat('K3:K', range1));       %Import recovery percent
cond1 = xlsread(filename1, strcat('G3:G', range1));
JwA1 = mean(Jw1);
JwS1 = std(Jw1);
reA1 = mean(Recovery1);
reS1 = std(Recovery1);

%Get data from 2nd file
filename2 = 'MDEXP7.10.2018.xlsx';      %to get filename to import
in2 = xlsread(filename2, 'S7:S8');
siz2 = in2(1);                %to get initial weight of tank
range2 = string(siz2 + 3);                                %Creates range number for data import
time2 = (xlsread(filename2, strcat('B3:B', range2)))/60;       %Import elapsed time
Jw2 = xlsread(filename2, strcat('I3:I', range2));       %Import water flux
Recovery2 = xlsread(filename2, strcat('J3:J', range2));       %Import recovery percent
cond2 = xlsread(filename2, strcat('F3:F', range2));
JwA2 = mean(Jw2);
JwS2 = std(Jw2);
reA2 = mean(Recovery2);
reS2 = std(Recovery2);

%Get data from 3rd file
filename3 = 'MDEXP7.11.2018.xlsx';      %to get filename to import
in3 = xlsread(filename3, 'S7:S8');
siz3 = in3(1);                %to get initial weight of tank
range3 = string(siz3 + 3);                                %Creates range number for data import
time3 = (xlsread(filename3, strcat('B3:B', range3))/60);       %Import elapsed time
Jw3 = xlsread(filename3, strcat('I3:I', range3));         %Import water flux
Recovery3 = xlsread(filename3, strcat('J3:J', range3));   %Import recovery percent
cond3 = xlsread(filename3, strcat('F3:F', range3));
JwA3 = mean(Jw3);
JwS3 = std(Jw3);
reA3 = mean(Recovery3);
reS3 = std(Recovery3);

tMax = max([time1(siz1), time2(siz2), time3(siz3)]) + 0.5;
%JwMax = max([Jw1(siz1), Jw2(siz2), Jw3(siz3)])+.75;
%cMax = max([cond1(siz1), cond2(siz2), cond3(siz3)]) + 1;

for i = siz1:-1:1
    if (Jw1(i) > (JwA1 + .7*JwS1)) ||  (Jw1(i) < (JwA1 - .7*JwS1))
        Jw1(i) = [];
        time1(i) = [];
        cond1(i) = [];
       Recovery1(i) = [];
   end
end

for i = siz2:-1:1
    if (Jw2(i) > (JwA2 + 0.7*JwS2)) ||(Jw2(i) < (JwA2 - 0.7*JwS2)) 
        Jw2(i) = [];
        time2(i) = [];
        cond2(i) = [];
       Recovery2(i) = [];
   end
end

for i = siz3:-1:1
    if (Jw3(i) > (JwA3 + 0.7*JwS3)) || (Jw3(i) < (JwA3 - 0.7*JwS3))
        Jw3(i) = [];
        time3(i) = [];
        cond3(i) = [];
       Recovery3(i) = [];
   end
end

fig = figure;
left_color = [0 0 0]; %makes color black
right_color = [0 0 0];
set(fig,'defaultAxesColorOrder',[left_color; right_color]);

%Graph 1
%left axis
yyaxis left                 %creates seperate axis to the left
plot(time1,Jw1,'o', 'MarkerSize', 10, 'MarkerEdgeColor', 'blue', 'MarkerFaceColor', [0 0 1])
hold on
plot(time2, Jw2,'square', 'MarkerSize', 10,  'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0])
hold on
plot(time3, Jw3,'d', 'MarkerSize', 10, 'MarkerEdgeColor', [0 .5 0], 'MarkerFaceColor', [0 .5 0])
ylabel('Jw (L/m^2-hr)') %y axis label for graph on left
axis([0 tMax 0 12]) %range of x from 0 to 16 and y axis from 0 to 10
hold on %Hold onto my previous command as other functions are added

yyaxis right
plot(time1,Recovery1,'o', 'MarkerSize', 10, 'MarkerEdgeColor', 'blue')
hold on
plot(time2, Recovery2,'square', 'MarkerSize', 10,  'MarkerEdgeColor', 'red')
hold on
plot(time3, Recovery3,'d', 'MarkerSize', 10, 'MarkerEdgeColor', [0 .5 0])
axis([0 tMax 0 100]) %range of x from 0 to 14 and y axis from 0 to 40
ylabel('Recovery (%)') %labels y axis
grid on %adds grid to plot
xlabel('Time (hrs)') %labels x axis
legend('Experiment 1 Jw','Experiment 2 Jw','Experiment 3 Jw', 'Experiment 1 Rec', 'Experiment 2 Rec', 'Experiment 3 Rec')
%creates legend on lower left hand corner
set(gca, 'Fontsize',14) %increases fontsize
hold off

%Graph 2
fig = figure;
    left_color = [0 0 0]; %makes color black
    right_color = [0 0 0];
    set(fig,'defaultAxesColorOrder',[left_color; right_color]);
%left axis
yyaxis left %creates seperate axis to the left
plot(time1,Jw1,'o', 'MarkerSize', 10, 'MarkerEdgeColor', 'blue', 'MarkerFaceColor', [0 0 1])
hold on
plot(time2, Jw2,'square', 'MarkerSize', 10,  'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0])
hold on
plot(time3, Jw3,'d', 'MarkerSize', 10, 'MarkerEdgeColor', [0 .5 0], 'MarkerFaceColor', [0 .5 0])
ylabel('Jw (L/m^2-hr)') %y axis label for graph on left
axis([0 tMax 0 12]) %range of x from 0 to 16 and y axis from 0 to 10
hold on %Hold onto my previous command as other functions are added

yyaxis right
plot(time1,cond1,'o', 'MarkerSize', 10, 'MarkerEdgeColor', 'blue')
hold on
plot(time2, cond2,'square', 'MarkerSize', 10,  'MarkerEdgeColor', 'red')
hold on
plot(time3, cond3,'d', 'MarkerSize', 10, 'MarkerEdgeColor', [0 .5 0])
axis([0 tMax 0 170]) %range of x from 0 to 14 and y axis from 0 to 40
ylabel('Conductivity (uS)') %labels y axis
grid on %adds grid to plot
xlabel('Time (hrs)') %labels x axis
legend('Experiment 1 Jw','Experiment 2 Jw','Experiment 3 Jw', 'Experiment 1 Cond', 'Experiment 2 Cond', 'Experiment 3 Cond')
%creates legend on lower left hand corner
set(gca, 'Fontsize',14) %increases fontsize
hold off