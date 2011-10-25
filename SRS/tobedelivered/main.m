%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 
dir = 'sound';
iter = 2;
thresh = 1e-3;
models = [hmm('go',5), hmm('stop', 4), hmm('left', 4), hmm('right',3)];
noWords = textread('test.txt', '%d');
for i=1:length(models)
    depth = 1;
    cData = 0;
    model = models(i);
    for j=1:noWords
        fname= [dir, '/', model.myWord, '_', num2str(j), '.wav'];
        [pData Fs] = wavread(fname);
        pData=reshape(pData,1,length(pData));
        % to get equally sized representations of sound files, we add some fluff at the end
        y=10+zeros(1,3000-length(pData));
        pData=[pData y];
        pData = prepareSignal(pData, Fs);
        data(:,:,j)=pData;
    end
    loglik = 0;
    dataLength = size(data, 3);
    for counter=1:dataLength
        page = data(:,:,counter);
        [ ll ] = forward(model, page);
        loglik = loglik + ll; 
    end 
    for counter=1:iter
        model = learn(model, data);
        ll = 0;
        for counter=1:dataLength
            page = data(:,:,counter);
            [ l ] = forward(model, page);
            ll = ll + l;
        end 
    end
end
%Writing the model to file.                 
save('models.mat','models');            
