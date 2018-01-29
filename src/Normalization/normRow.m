function [ normMat ] = normRow( mat )
%UNTITLED2 此处显示有关此函数的摘要
%   此处显示详细说明
   normMat = mat./repmat(sqrt(sum(mat.^2,2)),1,size(mat,2));
   
end

