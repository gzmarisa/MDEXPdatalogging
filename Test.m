clear, clc
%Test everything in here
%Created By: Ciara Avelina Lugo
%Modified By: EVERYONE

%Importing data from EXCEL
filename = input('What file would you like to import? Include ".txt"(macs)  ', 's');      %to get filename to import
delimiterIn= '\t';
headerlinesIn= 1;
data = importdata(filename,delimiterIn,headerlinesIn);
[rows, cols] = size(data.data);

%Delete rows that are not complete
dN = isnan(data.data);
for i = 1:rows
    for j = 1:cols
        if dN(i,j) == 1                                                     
            data.data(i,:) = [];
            dN(i,:) = [];
            rows = rows-1;
        elseif dN(i,2)== 1
            data.data(i,:) = [];
            data.data(i-1,:) = [];
            dN(i,:) = [];
            dN(i-1,:) = [];
            rows = rows-2;
        end 

    end 
    
end
disp('im done')