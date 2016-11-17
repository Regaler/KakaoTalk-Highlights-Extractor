function analyzer(filename)
% It gets a file, the data, and find the most prominent partitions, save it
% as outfile.txt.
fin = fopen(filename,'r');
fout = fopen('steppartitions.txt','w');
formatSpec = '%f';
A = fscanf(fin,formatSpec);
startendlist = [];
% LOOP for A
%for i = 1:size(A,1)
cnt = 1;
while cnt < size(A,1)
    if (A(cnt) >= 10)
        [start, last] = expander(A, cnt);
        startendlist = [startendlist; [start last]];
        cnt = last + 1;
        fprintf(fout,'%d %d\n',start, last);
    else
        cnt = cnt + 1;
    end
end
%disp(startendlist);
%disp(size(startendlist));
fclose(fin);
fclose(fout);