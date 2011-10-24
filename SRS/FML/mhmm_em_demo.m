%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% prepeares the data and creates the datastructure we use in the rest of the system. 
    % calculates some variables first
    % runs a loop to find peaks in graph. We use the peaks to compare later. 
    
% signal is the wav file, Fs is the sampling rate
[signal, Fs] = wavread('/home/alex/Dropbox/NTNU/IT3105/SRS/soundfile-wav/right_0.wav');

% length of the window to be used; 10ms
fLength = Fs/100;

% for the Fourier transform
NFFT = 2^nextpow2(fLength);

% normalize the signal so that the values fall between -1 & 1
signal = signal ./ max(abs(signal));

% frame the signal, 80 samples pr.frame, 50% overlap
frames = buffer(signal, fLength, round(fLength/2), 'nodelay');

% dimensions of the array storing the frames (80xno.frames)
frames_dim = size(frames);

% Fourier transform of the framed signl, each fram smoothed by a hamming window
FT = fft(frames .* repmat(hamming(frames_dim(1)),1,frames_dim(2)),NFFT);

NFFT = NFFT/2;

FT = 2*abs(FT(1:NFFT,:)) ./(2*pi);
plot(FT);

noFeatures = 4;

% go through all frames, find the peaks and sort them in descending order
% the five largest peaks, and their locations, will be used to identify the sound
% the following creates a 3-dimensional array, imagine it like a stack of paper, 
% peaks and locations in a frame on one sheet, the next frame on the next sheet etc.
preparedData = [];
for i=1:frames_dim(2)-1
    % consider using peakdet for this
    [pks locs] = findpeaks(FT(:,i), 'sortstr', 'descend');
    %preparedData = zeros(noFeatures,2,frames_dim(2)-1);
    if length(pks) < noFeatures
        preparedData = [preparedData pks(1,:)];
        %preparedData(:,2,i) = (locs(1,:)-1) / (NFFT-1);    
    else
        preparedData = [preparedData pks(1:noFeatures)];
        %preparedData(:,2,i) = (locs(1:noFeatures)-1) / (NFFT-1);
    end
end
%preparedData

data = preparedData;    

if 1
  O = noFeatures;
  T = 37;
  nex = 1;
  M = 1;
  Q = 3;
else
  O = 8;          %Number of coefficients in a vector 
  T = 420;         %Number of vectors in a sequence 
  nex = 1;        %Number of sequences 
  M = 1;          %Number of mixtures 
  Q = 6;          %Number of states 
end
cov_type = 'diag';


% initial guess of parameters
prior0 = normalise(rand(Q,1));
transmat0 = mk_stochastic(rand(Q,Q));

if 1
  Sigma0 = repmat(eye(O), [1 1 Q M]);
  %Sigma0 = eye(2);
  % Initialize each mean to a random data point
  indices = randperm(T*nex);
  mu0 = reshape(data(:,indices(1:(Q*M))), [O Q M]);
  %mu0 = 1;
  mixmat0 = mk_stochastic(rand(Q,M));
%else
%  [mu0, Sigma0] = mixgauss_init(Q*M, data, cov_type);
%  mu0 = reshape(mu0, [O Q M]);
%  Sigma0 = reshape(Sigma0, [O O Q M]);
%  mixmat0 = mk_stochastic(rand(Q,M));
end

[LL, prior1, transmat1, mu1, Sigma1, mixmat1] = ...
    mhmm_em(data, prior0, transmat0, mu0, Sigma0, mixmat0, 'max_iter', 5);


loglik = mhmm_logprob(data, prior1, transmat1, mu1, Sigma1, mixmat1);   

