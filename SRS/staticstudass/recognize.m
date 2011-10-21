%RECOGNIZE reconizes a word from a wav-file
%   input: file path of the wav-file that has to be recognized (with or
%          without .wav extension
%   output: string representation of the found word (start, stop, left,
%           right.
function [ word ] = recognize( filepath )

% capture data from wav-file
[ data Fs nbits ] = wavread(filepath);

% extract features from data
data = dataPrep(data, Fs);

% train models
% no. of hidden chosen with respect to no. of phonems
w = [ ...
        hmm('start', 5), hmm('stop',  4), ...
        hmm('left',  4), hmm('right', 3) ...
];

for i=1:length(w)
        train_model(w(i));
end

c = classifier;
c.words = w;
word = classify(c,data);
