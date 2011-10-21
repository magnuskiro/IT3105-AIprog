%DATAPREP prepares audio data for further processing in the SRS
%   data - vector of signed floating point numbers belonging to a discrete signal
%   Fs - sampling frequency/rate
function [ prepData ] = dataPrep( data, Fs )

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

noFeatures = 5;

% go through all frames
for i=1:dim(2)
    % capture greatest magnitude and according frequency
    [ pks locs ] = findpeaks(F(:,i), 'sortstr', 'descend');
    % amplitudes go to the first column ...
    prepData(:,1,i) = pks(1:noFeatures);
    % ... and frequencies (normalized to range 0-1) to the second one
    prepData(:,2,i) = (locs(1:noFeatures)-1) / (NFFT-1);
end
