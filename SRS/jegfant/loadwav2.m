%name=['S0T0','S0T1','S1T0','S1T1','S2T0','S2T1','S3T0','S3T1','S4T0','S4T1'];
name=['S5T0','S5T1','S6T0','S6T1','S7T0','S7T1','S8T0','S8T1','S9T0','S9T1']; %
digit=['0123456789']; %


for d=1:length(digit)
    eval(['x=wavread(''go_',digit(d),'.wav'');']);
    for k=1:4:length(name)
        x=vadnew(x);
        eval(['go_',digit(d),'=x(100*x1:100*x2);']);% ti_00F3S0T0=wavread('x(1).wav');
        x=x(x2*100:length(x));
    end
end

save ('F3new.mat', 'ti*');
