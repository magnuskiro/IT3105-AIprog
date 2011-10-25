%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% The class that represents the hidden markov model for a word 

classdef testhmm < handle 
    properties
        myWord
        noHidden
        priorHidden
        dynModel
        obsModels
    end
    
    methods
        % HMM Constructor function
        function model = testhmm(name, n)
            model.myWord = name;
            model.noHidden = n;
            
            % initialize with random values for probabilities
            model.priorHidden = [0.5;0.5];
            model.priorHidden = model.priorHidden ./ sum(model.priorHidden);
            model.dynModel = [0.7 0.3;0.3 0.7];
            sums = sum(model.dynModel,2);
            
            % ensure that no sum of probabilities exceed 1
            for i=1:n
                model.dynModel(i,:) = model.dynModel(i,:) ./ sums(i);
                model.obsModels(i) = mvnpdf(i,i,1);
            end
        end
    end
end
    
