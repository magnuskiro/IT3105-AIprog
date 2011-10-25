%DATAPREP prepares audio data for further processing in the SRS
%   data - vector of signed floating point numbers belonging to a discrete signal
%   Fs - sampling frequency/rate
[data, Fs] = wavread('/home/alex/Dropbox/NTNU/IT3105/SRS/soundfile-wav/go_23.wav');

L = Fs / 100; %length of frame (1/100 of a sec)

% power of 2 because of FFT algorithm
NFFT = 2^nextpow2(L);

% not sure about this normalization
data = data ./ max(abs(data));

% overlapping is 50%
frames = buffer(data, L, round(L/2), 'nodelay');

dim = size(frames);

% windowing and fft (F has same dimensions as frames)
F = fft(frames .* repmat( hamming(dim(1)),1,dim(2) ), NFFT);

% F is symmetric, so we can cut the lower half off
NFFT = NFFT / 2;

F = abs(F(1:NFFT,:)) ./ (2*pi);
%plot(F);

noFeatures = 3;

% go through all frames
for i=1:dim(2)
    % capture greatest magnitude and according frequency
    [ pks locs ] = findpeaks(F(:,i), 'sortstr', 'descend');
    % amplitudes go to the first column ...
    prepData(:,i) = pks(1:noFeatures);
    % ... and frequencies (normalized to range 0-1) to the second one
end

model = hmm('left', 4);
[log_likA alphas obsVec] = forward(model, prepData);
[betas] = backward(model, prepData);
[xi gammas] = learn(model, prepData);
%model = testhmm('two', 2);
%data = [2 3 4];
%[log_likA alphas] = forward(model, data);
%[log_likB betas] = backward(model, data);

