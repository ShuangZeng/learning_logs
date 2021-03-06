from django.db import models


# Create your models here.

class Topic(models.Model):
    # charField由字符或文本组成的数据
    text = models.CharField(max_length=200)
    # 记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #        返回模型的字符串表示
        return self.text


class Entry(models.Model):
    # 学到的某个主题的具体知识
    # 为foreignkey创建实例，将每个条目关联到特定的主题，主题创建时，分配key
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    # Textfireld不限制长度
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 如何表示多个条目
    class Meta:
        verbose_name_plural = 'entries'

    # 条目显示哪些信息：只显示前50个字符
    def __str__(self):
        return self.text[:50] + "..."
