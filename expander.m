function [start, last] = expander(list, pivot)
    start = left_expander(list, pivot);
    last = right_expander(list, pivot);
end