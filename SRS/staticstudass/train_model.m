function [ ] = train_model(model)

dir = 'wav';
range = 0:5;
thresh = 1e-3;
maxiter = 100;

depth = 1;

% loop through whole range
for i = range
        fname = [ dir, '/', model.myWord, '_', num2str(i), '.wav' ];
        [ fdata fs ] = wavread(fname);
        fdata = dataPrep(fdata, fs);
        fsize = size(fdata);
        data( ...
                1     : fsize(1), ...
                1     : fsize(2), ...
                depth : fsize(3)+depth-1 ...
        ) = fdata;
        depth = depth + fsize(3);
end

% iterations
[ ll ] = forwardHMM(model, data);
for i = 1:maxiter
        learn(model, data);
        [ l ] = forwardHMM(model, data);
        if (abs(ll-l) < thresh), break, end;
        ll = l;
        i, l
end
