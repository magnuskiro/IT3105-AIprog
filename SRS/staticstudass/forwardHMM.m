function [ log_lik alphas B ] = forwardHMM(hmm, data)

log_lik = 0;
totalTime = size(data,3);
alphas = zeros(hmm.noHidden, totalTime);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Taken from the lecture, try it %
% obsVec = zeros(hmm.noHidden, 1);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for t = 0:totalTime-1
        % Calculate the observation matrix.
        % This amounts to calculating likelihoods based on observation model.
        for s = 1:hmm.noHidden
                % obsVec(s) = calcLikelihood(data(:,:,t+1);
                B(s,t+1) = calcLikelihood(data(:,:,t+1), hmm.obsModel{s});
        end

        % Do forward iterations
        % diag(B(:,t+1)) creates a matrix noHidden x noHidden with all values 0 expect the diagonal, 
        % which is the probability of page t in that hidden state
        if t==0
                % what happens if we replace diag(B...) with diag(obsVec), as in the lecture slides?
                alphas(:, t+1) = diag(B(:,t+1)) * hmm.priorHidden;
        else
        % hmm.dynModel' is the transpose of dynModel, see formula p.14 of lecture notes
                alphas(:, t+1) = diag(B(:,t+1)) * hmm.dynModel' * alphas(:,t);
        end

        % Normalize
        normalizer = sum(alphas(:, t+1));
        log_lik = log_lik + log(normalizer);
        alphas(:, t+1) = alphas(:, t+1) ./ normalizer;
end

function [ betas ] = backwardHMM(hmm, B)

totalTime = size(B, 2);
betas = zeros(hmm.noHidden, totalTime);

% initialize to 1
betas(:,totalTime) = 1;

% do backward passes
for t = totalTime-1:-1:1
        betas(:,t) = hmm.dynModel * diag(B(:,t+1)) * betas(:,t+1);
        % normalize
        %betas(:, t) = betas(:, t) ./ sum(betas(:, t))
end
