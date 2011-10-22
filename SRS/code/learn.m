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
totalTime = size(data, 3);

%%%%%%%%%%   
% Part A %
%%%%%%%%%%

% forward passes
[log_lik alphas B] = forward(model, data);

% backward passes
[betas] = backward(model, B);

%%%%%%%%%%
% Part B %
%%%%%%%%%%

% loop through all the frames
size(alphas)
size(B)
size(betas)
for t=1:totalTime-1
    % xi is a book, with every page containing A(ij) the NxN matrix with probabilities of going from state i to j
    xi(:,:,t) = model.dynModel .* repmat(alphas(:,t), 1,N) .* repmat(B(:,t+1)', N,1) .* repmat(betas(:,t+1)', N,1);
    
    % for every page in xi, divide every value on page with the sum of all the values on the page
    xi(:,:,t) = xi(:,:,t)/sum(sum(xi(:,:,t)));
    
    % gamma for every t, gamma(t) is the sum of the rows in xi(:,:,t) (columns are 1, rows are 2)
    gamma(:,t) = sum(xi(:,:,t),2);
end

%%%%%%%%%%
% Part C %
%%%%%%%%%%

% reestimate prior distribution
model.priorHidden = gamma(:,1);

% reestimate transition model
model.dynModel = sum(xi(:,:,1:totalTime-1),3) ./ repmat(sum(gamma(:,totalTime-1),2),1,N);

% normalize
model.dynModel = model.dynModel ./ repmat(sum(model.dynModel,2),1,N);

%%%%%%%%%%
% Part E %
%%%%%%%%%%

% update mu and sigma
for i=1:N
    mu = sum(gamma(i,:));
    mu = sum(gamma(i,:) .* B(i,1:totalTime-1)) / mu;
    model.obsModel{i}.mu = mu;
    
    sigma = 0;
    'jello, these are the dimensions for gamma and B in learn'
    size(gamma), size(B)
    sigma = sum(gamma(i,:) .* (B(i,1:totalTime-1)-mu) *(B(i,1:totalTime-1)-mu)')/mu;
    
    model.obsModel{i}.sigma = sigma;
end
   
