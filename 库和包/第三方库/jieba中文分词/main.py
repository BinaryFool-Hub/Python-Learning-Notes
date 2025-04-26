import jieba  # pip install jieba
import jieba.analyse
import logging

"""
import jieba 和 import jieba.analyse 不是重复导入，而是分别导入核心功能和子模块功能。
如果你需要使用 jieba.analyse 的功能，必须显式导入 jieba.analyse。
为了代码的清晰性，建议同时导入 jieba 和 jieba.analyse。
"""

# 完全禁用 jieba 的日志输出
jieba.setLogLevel(logging.CRITICAL)

text = "自然语言处理是人工智能的重要方向之一"

# 精确模式：将句子精确切分，适合文本分析。
print(jieba.lcut(text))

# 全模式：将句子中所有可能的词语都扫描出来，速度快，但可能会有冗余。
print(jieba.lcut(text, cut_all=True))

# 搜索引擎模式：在精确模式的基础上，对长词再进行切分，适合搜索引擎构建索引。
print(jieba.lcut_for_search(text))

# 自定义词典:添加自定义词语，确保分词结果符合需求
jieba.add_word("语言处理")
print(jieba.lcut(text))

# 关键词提取: 基于 TF-IDF 算法或 TextRank 算法提取关键词。
keywords = jieba.analyse.extract_tags(text, topK=3)
print(keywords)
