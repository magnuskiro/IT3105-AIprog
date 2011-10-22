function [] = learn (hmm, data)

N = hmm.noHidden;
totalTime = size(data, 3);

%
% part A
%

% do forward passes
[ log_lik alphas B ] = forwardHMM(hmm, data);

% do backward passes
[ betas ] = backwardHMM(hmm, B);

%
% part B
%

% loop through all t
for t = 1:totalTime-1
        % xi is a book, with every page containing A(ij) the NxN matrix with probabilites of going from state i to j
        xi(:,:,t) = hmm.dynModel ...
                .* repmat( alphas(:,t),   1, N ) ...
                .* repmat( B(:,t+1)',     N, 1 ) ...
                .* repmat( betas(:,t+1)', N, 1 );

        % for every page in xi, divide every value on page with the sum of all the values on the page
        xi(:,:,t) = xi(:,:,t) / sum(sum(xi(:,:,t)));

        % gamma for every t, gamma(t) is the sum of the rows in xi(:,:,t) (columns = 1, rows = 2)
        gamma(:,t) = sum(xi(:,:,t), 2);
end

%
% part C
%

% reestimate prior distribution
hmm.priorHidden = gamma(:,1);

% reestimate transition model
hmm.dynModel = sum(xi(:,:,1:totalTime-1), 3) ./ repmat( sum(gamma(:,totalTime-1),2), 1, N );
% normalization
hmm.dynModel = hmm.dynModel ./ repmat( sum(hmm.dynModel,2), 1, N );

%
% part D
%

% no mixture

%
% part E
%

% update mu and sigma
for i = 1:N
        mu = sum(gamma(i,:));
        mu = sum(gamma(i,:) .* B(i,1:totalTime-1)) / mu;
        hmm.obsModel{i}.mu = mu;

        sigma = 0;
        sigma = sum(gamma(i,:) .* (B(i,1:totalTime-1)-mu)*(B(i,1:totalTime-1)-mu)') / mu;

        hmm.obsModel{i}.sigma = sigma;
end
