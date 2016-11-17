function last = right_expander(list, index)
right_index = 0;
for i = 1:5
    if (list(index + i) > 2)
        right_index = i;
    end
end
if (right_index == 0)
    last = index;
else
    last = right_expander(list, index + right_index);
end
end