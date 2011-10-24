%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% running the main program. 
    % read the test file (input sound)
    % call data prep on the input.
    % instantiate the hmms (words)
    % train the hmm representing the word
    % call classify and find out which word the sound represents.

 
            % p_data is the soundfile prepared for recognition
            % c_data is the concatination of all the prepared instances of that word
            dir = 'sound';
            iter = 5;
            thresh = 1e-3;
            Q = 2; % no.states
            M = 1; % no.mixtures
            O = 2; % no coefficients pr vector
            T = 248; % no of vectors in a sequence
            models = [hmm('go',5), hmm('stop', 4), hmm('left', 4), hmm('right',3)];
            noWords = textread('test.txt', '%d');
            prior0 = normalise(rand(Q,1));
            transmat0 = mk_stochastic(rand(Q,Q));
            for i=1:length(models)
                depth = 1;
                cData = 0;
                model = models(i);
                nex = 1;
                for j=1:noWords
                    fname= [dir, '/', model.myWord, '_', num2str(j), '.wav'];
                    %fname
                    [pData Fs] = wavread(fname);
                    pData=reshape(pData,1,length(pData));
                    % to get equally sized representations of sound files, we add some fluff at the end
                    y=10+zeros(1,10000-length(pData));
                    pData=[pData y];
                    pData = prepareSignal(pData, Fs);
                    data(:,:,j)=pData;
                    nex = nex+1;
                end
                %size(data)
                Sigma0 = repmat(eye(O), [1 1 Q M]);
                %Sigma0 = eye(2);
                % Initialize each mean to a random data point
                indices = randperm(T*nex);
                mu0 = reshape(data(:,indices(1:(Q*M))), [O Q M]);
                %mu0 = 1;
                mixmat0 = mk_stochastic(rand(Q,M));
                
                [LL, prior1, transmat1, mu1, Sigma1, mixmat1] = ...
                            mhmm_em(data, prior0, transmat0, mu0, Sigma0, mixmat0, 'max_iter', 5);
                
                loglik = mhmm_logprob(data, prior1, transmat1, mu1, Sigma1, mixmat1);   
                
                %size(cData)
                %[ll] = forward(model, cData);
                %backward(model, cData);
%                for j=1:iter
%                    learn(model, cData);
%                    [l] = forward(model, cData);
%                    if (abs(ll-l) < thresh), break, end;
%                    ll = l;
%                    j, l
%                end
            end
