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
    % train the hmm representing the word
    % call classify and find out which word the sound represents.

classdef main

    methods
        function srs = createSRS(obj)  
            % p_data is the soundfile prepared for recognition
            % c_data is the concatination of all the prepared instances of that word
            data = 0; 
            depth = 1;
            dir = 'sound';
            models = [hmm('start',5), hmm('stop', 4), hmm('left', 4), hmm('right',3)];
            no_words = textread('files.txt', '%d');
            for i=1:length(models)
                model = models(i);
                for j=1:no_words
                    fname= [dir, '/', model.myWord, '_', num2str(i), '.wav'];
                    [file, Fs] = wavread(fname);
                    p_data = data(file, Fs);
                    d_size = size(p_data);
                    c_data(1:d_size(1), 1:d_size(2), depth:d_size(3)+depth-1) = p_data;
                    depth = depth + d_size(3);
                end
                [ll] = fbhmm.
            for i=1:no_words
            fname = [dir, '/go_0.wav'];
            [file, Fs] = wavread(fname);
            p_data = data(file, Fs);
            m = hmm('start', 5);
        end

%        function r = recognize(obj, name)
%            no_words = textread('files.txt', '%d');
%            dir = 'test';
%            fname = [dir, '/', name, '_', num2str(i), '.wav'];
%            [file, Fs] = wavread(fname);
%            p_data = data(file, Fs);
%            classifier(p_data);           
%        end
    end
end
