function [ heteSim ] = calHete( mat1, mat2 )
%UNTITLED4 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
    heteSim = mat1 * mat2 ./ sqrt(sum(mat1.^2,2)*sum(mat2.^2));

end

