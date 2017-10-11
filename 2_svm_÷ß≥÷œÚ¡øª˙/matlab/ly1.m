[cup_label, cup_inst] = libsvmread('f.txt');
[cup_label_valid, cup_inst_valid] = libsvmread('g.txt');
model = svmtrain(cup_label,cup_inst, '-c 1000 -g 0.00025');
[predict_label, accuracy, dec_values] = svmpredict(cup_label_valid, cup_inst_valid, model); % test the trainingdata

a = fopen('predict.txt','w');
total_predict_num = length(predict_label);

for i = 1 : total_predict_num
    fprintf(a,'%d\t%d\r\n',i,predict_label(i));
end

fclose(a);