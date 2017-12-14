根据拍拍贷论坛用户评论建立需求资源池的过程如下：

1.用spider.py爬取拍拍贷论坛投资交流板块的前十页用户评论，并筛选出30条有效的用户评论。

2.“拍拍贷论坛评论.xlsx”文件中存放30条有效的用户评论

3.将30条有效的用户评论生成Sentence.txt文件

4.对Sentence.txt文件利用jieba包进行分词，并去掉停用词（用preprocess.py）

5.将分好的词存储在PPDWord.txt文件中

6.统计词频（Get_Words_Num.py）并按照词频由小到达的顺序排列

7.将统计好的词频存入word.txt中

8.根据word.txt中的词频，筛选需求，建立拍拍贷论坛的需求资源池，存储在PPDresource.csv中

