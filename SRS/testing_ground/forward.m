%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [log_lik alphas] = forwardHMM(obj, data)

log_lik = 0;
totalTime = size(data,2);
alphas = zeros(obj.noHidden, totalTime);
obsVec = zeros(obj.noHidden,1);

for t=0:totalTime-1
	for state = 1:obj.noHidden
		%obsVec(state) = calclLikelihood(obj.obsModel(state), data(:,t+1));
		obsVec = obj.obsModels(state);
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
alphas
%alphas, log_lik, obsVec
%size(data)

%function[betas] = backwardHMM(obj, data)

%log_lik = 0;
%totalTime = size(data,2);
%obsVec = zeros(obj.noHidden,1);
%betas = zeros(obj.noHidden, totalTime);

%for t=1:totalTime
%    for state =1:obj.noHidden
%        obsVec = obj.obsModels(state);
%    end
    
    
    
