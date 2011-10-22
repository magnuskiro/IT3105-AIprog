%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% contains the forward and backward hmm. and a function to calculate probability. 

%%%%%%%%%%%%%%%
% FORWARD HMM %
%%%%%%%%%%%%%%%

function [log_lik alphas B] = forwardHMM(model, data)

log_lik = 0;
totalTime = size(data,3);
alphas = zeros(model.noHidden, totalTime);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Taken from the lecture, try it %
% obsVec = zeros(hmm.noHidden, 1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for t = 0:totalTime-1
    % Calculate the observation matrix
    % This amounts to calculating likelihoods based on observation model
    for s = 1:model.noHidden
        % obsVec(s) = calcLikelihood(data(:,:,t+1);
        B(s,t+1) = calcLikelihood(data(:,:,t+1), model.obsModel{s});
    end
    % Do forward iterations
    % diag(B(:,t+1)) creates a matrix noHidden x noHidden with all values 0 except the diagonal
    % this is the probability of page t in that hidden state
    if t == 0
        % what happens if we replace diag(B(..)) with diag(obsVec), as in the lecture slides?
        alphas(:,t+1) = diag(B(:,t+1)) * model.priorHidden;
    else
        % model.dynModel' is the transpose of dynModel, see formula p.14 of lecture notes
        alphas(:,t+1) = diag(B(:,t+1)) * model.dynModel' * alphas(:,t);
    end
    
    % Normalize
    normalizer = sum(alphas(:,t+1));
    log_lik = log_lik + log(normalizer);
    alphas(:,t+1) = alphas(:,t+1) ./ normalizer;
end


%%%%%%%%%%%%%%%%
% BACKWARD HMM %
%%%%%%%%%%%%%%%%

function [betas] = backwardHMM(model, B)

totalTime = size(B,2);
betas = zeros(model.noHidden, totalTime);

% initialize
betas(:,totalTime = 1;

% backward passes
% NEED TO NORMALIZE SOMEHOW!
for t = totalTime-1:-1:1
    betas(:,t) = model.dynModel * diag(B(:,t+1)) * betas(:,t+1);
    % normalize
    % betas(:,t) = betas(:,t) ./ sum(betas(:,t))
end


%%%%%%%%%%%%%%%%%%
% CALCLIKELIHOOD %
%%%%%%%%%%%%%%%%%%

% calculates the probability of an observation

function[p] = calcLikelihood(data, model)

n = size(data,1);

p = mvnpdf(data, model.mu, model.sigma);
c = logspace(0,1,n);
c = c ./ sum(c);
c = fliplr(c);
res = 0;
for i = 1:n
    res = res + (p(i)*c(i));
end
p = res;
