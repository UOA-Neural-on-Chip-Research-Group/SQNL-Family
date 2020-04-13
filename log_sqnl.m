function y = log_sqnl(n)
     
y=zeros(size(n));

idx = find(n > 2);
n(idx) = 2;

idx = find(n < -2);
n(idx) = -2;


idx = find(n >= 0);
y(idx) = ((n(idx) - n(idx).^2/4)*0.5)+0.5;

idx = find(n < 0);
y(idx) = ((n(idx) + n(idx).^2/4)*0.5)+0.5;

end
