function [ normMat ] = normRow( mat )
%UNTITLED2 �˴���ʾ�йش˺�����ժҪ
%   �˴���ʾ��ϸ˵��
   normMat = mat./repmat(sqrt(sum(mat.^2,2)),1,size(mat,2));
   
end

