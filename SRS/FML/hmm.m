%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% The class that represents the hidden markov model for a word 

classdef hmm < handle 
    properties
        myWord
        noHidden
        priorHidden
        dynModel
        obsModels
    end
    
    methods
        % HMM Constructor function
        function model = hmm(name, n)
            model.myWord = name;
            model.noHidden = n;
            
            % initialize with random values for probabilities
            model.priorHidden = rand(n,1);
            model.priorHidden = model.priorHidden ./ sum(model.priorHidden);
            model.dynModel = rand(n);
            model.obsModels = zeros(n,1);
            sums = sum(model.dynModel,2);
            
            % ensure that no sum of probabilities exceed 1
            for i=1:n
                model.dynModel(i,:) = model.dynModel(i,:) ./ sums(i);
                model.obsModels(i) = mvnpdf(i,i,1);
            end
        end
    end
end
    


