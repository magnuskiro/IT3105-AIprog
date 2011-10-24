%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%
% BACKWARD HMM %
%%%%%%%%%%%%%%%%

function [betas] = backward(model, B)

log_lik = 0;
totalTime = size(B,2);
betas = zeros(model.noHidden, totalTime);

% initialize
betas(:,totalTime) = 1;

% backward passes
% NEED TO NORMALIZE SOMEHOW!
for t = totalTime-1:-1:1
    betas(:,t) = model.dynModel * diag(B(:,t+1)) * betas(:,t+1);
    normalizer = sum(betas(:,t));
    log_lik = log_lik + log(normalizer);
    betas(:,t) = betas(:,t) ./ normalizer;
end
