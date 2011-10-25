%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%
% CALCLIKELIHOOD %
%%%%%%%%%%%%%%%%%%

% calculates the probability of an observation

function[p] = calcLikelihood(data,model)

n = size(data,1);
p = mvnpdf(data, model.mu, model.sigma);
c = logspace(0,1,n);
c = c ./ sum(c);
c = fliplr(c);
res = 0;
for i = 1:n
    if length(p)>=2
        res = res + (p(i)*c(i));
    end
end
p = res;
