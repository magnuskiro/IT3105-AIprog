%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%
% FORWARD HMM %
%%%%%%%%%%%%%%%

function [log_lik alphas B] = forward(model, data)

log_lik = 0;
totalTime = size(data,3);
alphas = zeros(model.noHidden, totalTime);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Taken from the lecture, try it %
%obsVec = zeros(model.noHidden, 1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for t = 0:totalTime-1
    % Calculate the observation matrix
    % This amounts to calculating likelihoods based on observation model
    for s = 1:model.noHidden
        %obsVec(s) = calcLikelihood(data(:,:,t+1), model.obsModel{s});
        B(s,t+1) = calcLikelihood(data(:,:,t+1), model.obsModel{s});
    end
    % Do forward iterations
    % diag(B(:,t+1)) creates a matrix noHidden x noHidden with all values 0 except the diagonal
    % this is the probability of page t in that hidden state
    if t == 0
        % what happens if we replace diag(B(..)) with diag(obsVec), as in the lecture slides?
        %alphas(:,t+1) = diag(obsVec)*model.priorHidden;
        alphas(:,t+1) = diag(B(:,t+1)) * model.priorHidden;
    else
        % model.dynModel' is the transpose of dynModel, see formula p.14 of lecture notes
        %alphas(:,t+1) = diag(obsVec) * model.dynModel' * alphas(:,t);
        alphas(:,t+1) = diag(B(:,t+1)) * model.dynModel' * alphas(:,t);
    end
    
    % Normalize
    normalizer = sum(alphas(:,t+1));
    log_lik = log_lik + log(normalizer);
    alphas(:,t+1) = alphas(:,t+1) ./ normalizer;
end
%alphas(:,2)
