%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% learning and training the hmms, so we can get data to compare too. 
    % reads the sound files and gather data to train the model
    % learns, the model is updated with the new data. so the hmms get more precise data, and it gets easier to recognize other sounds. 
    
function [] = learn(model, data)
  
N = model.noHidden;
totalTime = size(data, 2);

%%%%%%%%%%   
% Part A %
%%%%%%%%%%

% forward passes
[log_lik alphas] = forward(model, data);

% backward passes
[betas] = backward(model, data);

%%%%%%%%%%
% Part B %
%%%%%%%%%%

% loop through all the frames
size(alphas)
%size(B)
size(betas)
%betas
for t=1:totalTime-1
    %alphas(:, t), betas(:,t)
    xi(:,:,t) = model.dynModel
    % xi is a book, with every page containing A(ij) the NxN matrix with probabilities of going from state i to j
    %xi(:,:,t) = model.dynModel .* repmat(alphas(:,t), 1,N) .* repmat(betas(:,t+1)', N,1);
    %xi(:,:,t) = model.dynModel * (alphas(:,t) ./ sum(alphas(:,t))) * (betas(:,t+1) ./ sum(betas(:,t+1))');
    %xi(:,:,t) = model.dynModel .* alphas .* betas; 
    xi(:,t) = alphas(:,t).*betas(:,t);
    xi = xi / (sum(alphas(:,t)) .* (sum(betas(:,t))));
    
    % for every page in xi, divide every value on page with the sum of all the values on the page
    %xi(:,:,t) = xi(:,:,t)/sum(sum(xi(:,:,t)));
    
    % gamma for every t, gamma(t) is the sum of the rows in xi(:,:,t) (columns are 1, rows are 2)
    %gamma(:,t) = sum(xi(:,:,t),2);
    gamma(:,t) = xi;
    %gamma
end

%%%%%%%%%%
% Part C %
%%%%%%%%%%

% reestimate prior distribution
model.priorHidden = (sum(gamma'))' / sum((sum(gamma'))');
%(sum(gamma'))' / sum((sum(gamma'))')
xi
diag(xi)

% reestimate transition model
%model.dynModel = sum(xi(:,:,1:totalTime-1),3) ./ repmat(sum(gamma(:,totalTime-1),2),1,N);
model.dynModel = sum(xi(:,:,1:totalTime-1),3) ./ (gamma(:,totalTime-1) ./ sum(gamma(:,totalTime-1)));

% normalize
%model.dynModel = model.dynModel ./ repmat(sum(model.dynModel,2),1,N);
model.dynModel = model.dynModel ./ model.dynModel ./ sum(model.dynModel,2);

%%%%%%%%%%
% Part E %
%%%%%%%%%%

% update mu and sigma
sigma = 0;
for i=1:N
    mu = sum(gamma(i,:));
    mu = sum(gamma(i,:) .* B(i,1:totalTime-1)) / mu;
    model.obsModel{i}.mu = mu;
    
    %'jello, these are the dimensions for gamma and B in learn'
    %size(gamma), size(B)
    %for t=1:totalTime
    %    sigma(i,t) = (sum(gamma(i,:) * ((B(i,1:totalTime-1)-mu) * (B(i,1:totalTime-1)-mu)')))/sum(gamma(i,:));
    %end
    sigma = (sum(gamma(i,:) * ((B(i,1:totalTime-1)-mu) * (B(i,1:totalTime-1)-mu)')))/sum(gamma(i,:));
    %normalizer = sum(sigma(i,:));
    %log_lik = log(normalizer);
    %sigma(i,:) = sigma(i,:) ./ normalizer;
    %sigma = sum(sigma(i,:))
    sigma
    diag(B)
    model.obsModel{i}.sigma = eye(2) * sigma;
end

%normalizer = 0;
%for i=1:N
%   normalizer =  normalizer + sum(sigma(i,:));
%end

    
   
