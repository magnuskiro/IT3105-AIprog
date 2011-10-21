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
