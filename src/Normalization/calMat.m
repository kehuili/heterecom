AB = [1 1 0 0;0 1 1 1;0 0 0 1];

%  normalize each row to unit
AB = normRow(AB)
BA = AB';

x = calHete(AB, BA)

AB = [1 1 0 0;0 1 1 1;0 0 0 1];
BA = AB';

AB = normRow(AB);
BA = normRow(BA);

C = AB * BA;
Ct = C';
y = calHete(C, Ct)



