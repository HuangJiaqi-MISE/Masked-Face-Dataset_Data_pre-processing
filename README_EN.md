# 'Masked-Face-Dataset' Data pre-processing

When the dataset zip file is extracted the masked_whn folder is obtained along with the readme.docx file, the exact file path of which is shown below.

```bash
Masked-Face-Dataset
  ├─ masked_whn
    ├─ 00_0001_tankai_07 # 下面放测试集标签
      ├─0.jpg
      ├─1.jpg
      ├─2.jpg
      ├─3.jpg
      ├─4.jpg
      ├─unmasked.jpg
    ├─ 00_0002_luyi_03 # 下面放测试集标签
      ├─0.jpg
      ├─1.jpg
      ├─2.jpg
      ├─unmasked.jpg
    ├─ 00_0003_qiqi_02 # 下面放测试集标签
      ├─...(The name of number).jpg
      ├─unmasked.jpg
    ├─ 00_0004_shuqi_04 # 下面放测试集标签
      ├─...(The name of number).jpg
      ├─unmasked.jpg
    ├─ 00_0005_zhengxiujin_10 # 下面放测试集标签
      ├─...(The name of number).jpg
      ├─unmasked.jpg
    ├─...
      ├─...(The name of number).jpg
      ├─unmasked.jpg
  ├─ readme.docx # 下面放测试集图片
```
It is easy to see that there are many folders in the masked_whn folder, which are named according to the rule: " two-digit _ four-digit _ name _ two-digit ".

When using machine learning methods (e.g. GOG-SVM, Haar) to classify targets, all the images in the folder are filtered and the "With Mask" and "Without Mask" samples are stored in two designated folders "With Mask" and "Without Mask" respectively.

As a result, I designed a retrieval procedure based on file names to rename and store image files within the training set under a specified path for use in subsequent model training.



```bash
Author：Huang Jiaqi
Created：2022-05-09
Last updated：2022-05-16
Function：For the pre-processing of the data set, the images with masks and the images without masks are stored in separate folders and renamed.
```


