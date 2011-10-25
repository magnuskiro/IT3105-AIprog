%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [log_lik alphas obsVec] = forwardHMM(obj, data)

log_lik = 0;
totalTime = size(data,2);
alphas = zeros(obj.noHidden, totalTime);
obsVec = zeros(obj.noHidden,1);

for t=0:totalTime-1
	for state = 1:obj.noHidden
		obsVec(state) = calcLikelihood(data(:,t+1) ,obj.obsModels{state});
	end
	if t == 0
		alphas(:,t+1) = diag(obsVec) * obj.priorHidden;
	else
		alphas(:,t+1) = diag(obsVec) * obj.dynModel' * alphas(:,t);
	end
	
	normalizer = sum(alphas(:,t+1));
	alphas(:,t+1) = alphas(:,t+1) ./ normalizer;
	log_lik = log_lik+log(normalizer);
end
