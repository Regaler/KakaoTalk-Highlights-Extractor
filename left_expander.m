function start = left_expander(list, index)
% left_expander expands the list to left at most
left_index = 0;
for i = 1:5
    if (list(index - i) > 2)
        left_index = i;
    end
end
if (left_index == 0)
    start = index;
else
    start = left_expander(list, index - left_index);
end
end