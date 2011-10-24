load('models.mat');
[pData Fs] = wavread('query/query_7.wav');
pData=reshape(pData,1,length(pData));
% to get equally sized representations of sound files, we add some fluff at the end
y=10+zeros(1,10000-length(pData));
pData=[pData y];
pData = prepareSignal(pData, Fs);
%pData = mfcc(pData, Fs);
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
index, loglik
if index~=d
   msg=['no']
end
