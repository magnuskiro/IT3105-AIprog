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

function[betas] = backwardHMM(obj, data)

log_lik = 0;
totalTime = size(data,2);
obsVec = zeros(obj.noHidden,1);
betas = ones(obj.noHidden, totalTime);
%betas(:,totalTime) = ones(:,totalTime);

for t= totalTime-1:-1:1
    for state = 1:obj.noHidden
        obsVec(state) = calcLikelihood(data(:,t+1) ,obj.obsModels{state});
    end
    betas(:,t) = obj.dynModel * diag(obsVec) * betas(:,t+1);
    %betas(:,t), obj.dynModel, diag(obsVec), betas(:,t+1)
    
    normalizer = sum(betas(:,t));
	betas(:,t) = betas(:,t) ./ normalizer;
	log_lik = log_lik+log(normalizer);
end

