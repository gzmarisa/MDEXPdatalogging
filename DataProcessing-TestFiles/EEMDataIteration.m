clear all, clc

%Script for processing EEM data
%Created By: Marcos Lee
%Modified By: 


%Importing data from EXCEL
file1 = input('What UV file would you like to import? Include ".xlsx"  ', 's');      %to get filename to import
file2 = input('What FL file would you like to import? Include ".xlsx"  ', 's');      %to get filename to import

UV= xlsread(file1); %Converts data into Matrix
EEM= xlsread(file2); %Converts data into Matrix

% [rows, colms] = size(UV);



for i = 1 : 3
    EEM(i,:)=[];
end 
EEM(1,:)=[];

AbdOD=UV(:,10); %defining necessary vectors 
UVnums=EEM(:,1); %defining necessary vectors 
WVLNG=UV(:,1); %defining necessary vectors 
AbdOD=flip(AbdOD); %flips order of vector to match order of FL data 
WVLNG=flip(WVLNG); %flips order of vector to match order of FL data

for i= 2: length(WVLNG) %should delete every wave length and abs associated with that wave length except for the one right below
                % the needed (first wave length value in FL xlsx) value but does not HELP!!! 
                % need that value for linear interpolation. 
            
    if UVnums(1) > WVLNG(i)
        WVLNG(i-1)=[NaN];
        AbdOD(i-1)=[NaN];
    else
        break
    end 
    
end

dN=isnan(WVLNG);

%{
for i = 1:length(WVLNG)
    if dN == 1 
        WVLNG(i)=[]
        AbdOD(i)=[];
        dN(i)=[]
        dN2(i)=[];
    else 
        break 
    end 
end
        
%}
WVLNG(dN)=[];
AbdOD(dN)=[];


for i = length(WVLNG)-1

    slopes(i)=(AbdOD(i+1)-AbdOD(i))/(WVLNG(i+1)-WVLNG(i))
    
end 
