function [ heteSim ] = calHete( mat1, mat2 )
%UNTITLED4 此处显示有关此函数的摘要
%   此处显示详细说明
    heteSim = mat1 * mat2 ./ sqrt(sum(mat1.^2,2)*sum(mat2.^2));

end

