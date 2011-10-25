%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clear
load('models.mat');

for i=1:36
    fname = ['query_', num2str(i-1)];
    fpath = ['query/', fname, '.wav'];

    [pData Fs] = wavread(fpath);
    pData=reshape(pData,1,length(pData));
    % to get equally sized representations of sound files, we add some fluff at the end
    y=10+zeros(1,10000-length(pData));
    pData=[pData y];
    pData = prepareSignal(pData, Fs);
    data(:,:,1)=pData;

    maxP = 0;
    load('models.mat');
    %finding the word in the vocabulary that is most like the input data. 
    for k = 1:4
        h = models(1,k);
        [ l ] = forward(h, data);
        P = exp(l);
        if (P > maxP)
                maxP = P;
                index = k;
        end
    end

    % Changing the result from index to word. Human readable. 
    if index == 1
        w = 'START';
    elseif index == 2
        w = 'STOP ';
    elseif index == 3
        w = 'LEFT ';
    else
        w = 'RIGHT';
    end

    if i<=10
        w = ['0' num2str(i-1) '   ' w];
    else
        w = [num2str(i-1) '   ' w];
    end
    results(i,:) = w;
end
'filename, result'
results
