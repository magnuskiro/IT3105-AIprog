%CALCLIKELIHOOD calculates the probability of an observation
%   if model=0 then µ=0
function [ p ] = calcLikelihood( data, model )

n = size(data,1);

p = mvnpdf(data, model.mu, model.sigma);
c = logspace(0,1,n);
c = c ./ sum(c);
c = fliplr(c);
res = 0;
for i = 1:n     %weight the different probabilities
    res = res + (p(i)*c(i));
end
p = res;
