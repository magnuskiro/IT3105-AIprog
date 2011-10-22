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
    % call classify and find out which word the sound represents.
    
[file, Fs] = wavread('/home/alex/Dropbox/NTNU/IT3105/SRS/soundfile-wav/right_0.wav');
data(file, Fs);
m = hmm('right', 4);
