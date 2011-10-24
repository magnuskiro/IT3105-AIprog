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
            models = [hmm('go',5), hmm('stop', 4), hmm('left', 4), hmm('right',3)];
            noWords = textread('test.txt', '%d');

            for i=1:length(models)
                depth = 1;
                cData = 0;
                model = models(i);
                for j=1:noWords
                    fname= [dir, '/', model.myWord, '_', num2str(j), '.wav'];
                    fname
                    [pData Fs] = wavread(fname);
                    pData = prepareSignal(pData, Fs);
                    dSize = size(pData);
                    cData(1:dSize(1), 1:dSize(2), depth:dSize(3)+depth-1) = pData;
                    depth = depth + dSize(3);
                end
                [ll] = mhmm_em_demo(model, cData);
                for j=1:iter
                    learn(model, cData);
                    [l] = forward(model, cData);
                    if (abs(ll-l) < thresh), break, end;
                    ll = l;
                    j, l
                end
            end
