classdef hmm < handle
        properties
                myWord
                noHidden
                dynModel
                obsModel
                priorHidden
        end

        methods
                % HMM Constructor function
                function h = hmm( name, n )
                        h.myWord = name;
                        h.noHidden = n; 

                        %random init values for probabilities
                        h.priorHidden = rand(n,1);
                        h.priorHidden = h.priorHidden ./ sum(h.priorHidden);
                        h.dynModel = rand(n);
                        h.obsModel = cell(n,1);

                        % normalization of every row to fit stochastic constraints
                        for i = 1:n
                                h.dynModel(i,:) = h.dynModel(i,:) ./ sum(h.dynModel);
                                h.obsModel{i} = struct('mu', 0, 'sigma', eye(2));
                        end
                end
        end
end
