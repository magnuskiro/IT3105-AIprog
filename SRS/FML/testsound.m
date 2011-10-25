clear
load('models.mat');

for i=1:36
    fname = ['query_', num2str(i-1)];
    fpath = ['query/', fname, '.wav'];
    %fpath

    [pData Fs] = wavread(fpath);
    pData=reshape(pData,1,length(pData));
    % to get equally sized representations of sound files, we add some fluff at the end
    y=10+zeros(1,10000-length(pData));
    pData=[pData y];
    %pData = prepareSignal(pData, Fs);
    pData = mfcc(pData, Fs);
    data(:,:,1)=pData;

    %transmat0 = mk_stochastic(rand(Q,Q));
    d = 1;

    for cc=1:4
        if cc == 1 
            Q=5;
        elseif cc==4
            Q=3;
        else 
            Q=4;
        end
            
        prior0 = normalise(rand(Q,1));
        eval(['loglik(cc) = mhmm_logprob(pData, prior0, transmat_0',num2str(cc),', mu_0',num2str(cc),', Sigma_0',num2str(cc),', mixmat_0',num2str(cc),');']);   
    end
    index=find(loglik==max(loglik));
    %fname, index, loglik

    if index == 1
        w = 'START';
    elseif index == 2
        w = 'STOP ';
    elseif index == 3
        w = 'LEFT ';
    else
        w = 'RIGHT';
    end
    %w, i
    if i<=10

        w = ['0' num2str(i-1) '   ' w];
    else
        w = [num2str(i-1) '   ' w];
    end
    results(i,:) = w;
end
'filename, result'
