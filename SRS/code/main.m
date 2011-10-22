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
    
dir = 'sound' ;
%fname= [dir, '/', model.myWord, '_', num2str(i), '.wav'];
fname = [dir, '/go_0.wav'];
[file, Fs] = wavread(fname);
data(file, Fs);
m = hmm('right', 4);
