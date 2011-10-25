%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                   %
%   IT3105 - Artificial Intelligence programming    %
%   Sound Recognition System - SRS                  %
%   Jan Alexander Bremnes and Magnus Kirø           %
%   Oct - 2011                                      %
%                                                   %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% signal is the wav file, Fs is the sampling rate
function [preparedData] = prepareSignal(signal, Fs)

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

noFeatures = 2;

% go through all frames, find the peaks and sort them in descending order
% the noFeatures largest peaks, and their locations, will be used to identify the sound
% the following creates a 3-dimensional array, imagine it like a stack of paper, 
% peaks and locations in a frame on one sheet, the next frame on the next sheet etc.
for i=1:frames_dim(2)-1
    % consider using peakdet for this
    [pks locs] = findpeaks(FT(:,i), 'sortstr', 'descend');
    if length(pks) < noFeatures
        preparedData(:,i) = pks(1,:);
    else
        preparedData(:,i) = pks(1:noFeatures);
    end
end
