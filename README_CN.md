# Masked-Face-Dataset数据预处理

在数据集压缩文件解压后会得到masked_whn文件夹与readme.docx文件，其具体的文件路径如下图：

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
不难发现在masked_whn文件夹内有很多个文件夹，它们的名称按照：“两位数字_四位数字_名字_两位数字”规则命名。

在使用机器学习方法（如：GOG-SVM、Haar）对目标进行分类时需要对文件夹内的所有的图片进行筛选，将“戴口罩”与“不戴口罩”两种样本分别存放在两个指定的文件夹“With Mask”与“Without Mask”内。

由此，我设计了一种根据文件名称的检索程序，将训练集内的图片文件重命名并存放在指定路径下，以供后续模型训练的使用。



```bash
作者：黄家琦
创建：2022-05-09
更新：2022-05-16
用意：用于数据集的预处理，将带口罩的图片与不带口罩的图片样本分别存放至指定文件夹并重命名
```


