# LeetCode-二刷230+题目经验总结+大小厂面试题经验总结，分为 经验要点 + 必须吃透题 + 常考题 三个部分，适合开始刷题或刷题效率一般的coder."talk is cheap,show me the code"

本文不同于直接讲解题目知识点，而是首先分享 经验心得，刷题方法（授人以鱼不如授人以渔），再是分享必须吃透题和常考题等代码解答。

后续更新：刷近两年的牛客网的算法工程师面经的 word文档总结，该文档包含机器学习、计算机视觉等面试题的问题及解答（解答均来自楼主历时数月刷面经过程中摘写的知识点，方便实用）。

经验要点：

1.常用的逻辑数据结构包括 数组、链表、栈、队列、 树、图等，但 物理数据结构 只有两种：顺序存储结构，链式存储结构。众多逻辑数据结构都是在物理数据结构基础之上实现的，即计算机内存中的数据结构只有 顺序存储和 链式存储 两种方式。

2.递归方法是编程中最精妙的方法（个人刷题感受：有时候需要复杂代码去实现时，用递归方法可以一行代码搞定，代码简洁舒畅），用递归方法会带来栈内存的消耗（在分析递归代码的空间复杂度时，一般以递归调用的次数多少来比较空间复杂度大小），链表和树的数据结构天生适合递归方法（在这里强烈建议：一定要在代码中实现从建立链表（包括链表节点的定义都要熟记于心,因为大厂面试官考查链表题目会要求从链表节点开始coding）到比如反转链表的的具体代码实现等题目;从建立树节点（熟记树节点的定义，理由同前）到比如二叉搜索树转换成双向链表的具体代码实现等题目)。

3.刷题方法：建议 基本的逻辑数据结构熟悉一遍 + 学习本文的必须吃透题（代码中有注释） + 常考题
