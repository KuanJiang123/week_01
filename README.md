基础理论部分
0. Can you come up out 3 sceneraies which use AI methods?
Ans: {文本分类、机器翻译、对话生成}

1. How do we use Github; Why do we use Jupyter and Pycharm;
Ans: 
使用github：
  1. 创建一个仓库
  2. 使用github客户端将仓库项目克隆到本地空间
  3. 对本地文件进行项目创建
  4. 提交到github上
  使用pycharm可以提高编码效率，提供丰富插件，方便开发；对于bug调试，也很方便。

2. What's the Probability Model?
Ans:给定一个用户的查询串 和集合中的文档 概率模型来估计用户查询串与文档 相关的概率

3. Can you came up with some sceneraies at which we could use Probability Model?
Ans:贝叶斯，马尔科夫

4. Why do we use probability and what's the difficult points for programming based on parsing and pattern match?
Ans:
使用概率，可以较好的发现新词，基于解析和模式匹配依赖于字典的构建，不能很好发现新词。

5. What's the Language Model;
Ans:统计语言模型是一个单词序列上的概率分布，对于一个给定长度为m的序列，它可以为整个序列产生一个概率 P(w_1,w_2,…,w_m) 。其实就是想办法找到一个概率分布，它可以表示任意一个句子或序列出现的概率

6. Can you came up with some sceneraies at which we could use Language Model?
Ans:机器翻译、拼写检查

7. What's the 1-gram language model;
Ans:句子的概率是个各个词概率的乘积

8. What's the disadvantages and advantages of 1-gram language model;
Ans:
优势:容易理解，计算效率高；
缺点：假设各个词之间独立，完全损失了句中的词序信息

9. What't the 2-gram models;
Ans:当前词的概率受前一个词影响，不独立存在。
