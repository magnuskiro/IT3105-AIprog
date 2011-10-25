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
    
function [xi gammas] = learn(model, data)

xi = [];  
N = model.noHidden;
totalTime = size(data, 2);

%%%%%%%%%%   
% Part A %
%%%%%%%%%%

% forward passes
[log_lik alphas obsVec] = forward(model, data);

% backward passes
[betas] = backward(model, data);

%%%%%%%%%%
% Part B %
%%%%%%%%%%

% Calculate gammas
gammas = alphas.*betas;

% Calculate Xi
for t=1:totalTime-1
    xi(:,:,t) = repmat(alphas(:,t),1,N) * model.dynModel * repmat(obsVec,1,N) * repmat(betas(:,t+1),1,N);
    sums = sum(xi(:,:,t));
    sums = sum(sums);
    xi(:,:,t) = xi(:,:,t) ./ sums;
%    gamma(:,t) = sum(xi(:,:,t),2);        % already calculated above, ref. Rabiner eq.27
end

%%%%%%%%%%
% Part C %
%%%%%%%%%%

% reestimates prior distribution
model.priorHidden = (sum(gammas'))' / sum((sum(gammas'))');

% reestimate transition model
model.dynModel = sum(xi(:,:,1:totalTime-1),3)  ./ repmat(sum(gammas(:,totalTime-1),2),1,N);

% normalization
model.dynModel = model.dynModel ./ sum(sum(model.dynModel));


%%%%%%%%%%%
%% Part D %
%%%%%%%%%%%

%% Mixture not used


%%%%%%%%%%%
%% Part E %
%%%%%%%%%%%

%% update mu and sigma
for i=1:N
    mu = sum(gammas(i,:));
    mu = sum(gammas(i,:) .* model.obsModels{i}.mix(i)) / mu;
    model.obsModels{i}.mu = mu;
%    
%    %'jello, these are the dimensions for gamma and B in learn'
%    %size(gamma), size(B)
%    %for t=1:totalTime
%    %    sigma(i,t) = (sum(gamma(i,:) * ((B(i,1:totalTime-1)-mu) * (B(i,1:totalTime-1)-mu)')))/sum(gamma(i,:));
%    %end
%    sigma = (sum(gamma(i,:) * ((B(i,1:totalTime-1)-mu) * (B(i,1:totalTime-1)-mu)')))/sum(gamma(i,:));
%    %normalizer = sum(sigma(i,:));
%    %log_lik = log(normalizer);
%    %sigma(i,:) = sigma(i,:) ./ normalizer;
%    %sigma = sum(sigma(i,:))
%    sigma
%    diag(B)
%    model.obsModel{i}.sigma = eye(2) * sigma;
end


    
   
