M = [0 1/2 1 0; 1/3 0 0 1/2; 1/3 0 0 1/2; 1/3 1/2 0 0];
v = [1 0 0 0]'; % initial value no effects for final result
%cons = [1 0 0 0]'; % for case a), has different bias
cons = [0.5 0 0.5 0]'; % for case b), 

for i = 1:100
    v = 0.8 * M * v + 0.2 * cons;
end
% ends, v is the final vector for (a,b,c,d)
