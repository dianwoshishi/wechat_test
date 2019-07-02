#!/usr/bin/python
#coding=utf8





import jieba
import re





# 设置系统编码
def set_sys_code():
    import sys;
    reload(sys);
    sys.setdefaultencoding("utf8")









def word_cloud(friends):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, ImageColorGenerator
    import PIL.Image as Image
    import os
    import numpy as np
    d = os.path.dirname(__file__)
    my_coloring = np.array(Image.open(os.path.join(d, "timg.jpeg")))
    signature_list = []
    for friend in friends:
        signature = friend["Signature"].strip()
        signature = re.sub("<span.*>", "", signature)
        signature_list.append(signature)
    raw_signature_string = ''.join(signature_list)
    text = jieba.cut(raw_signature_string, cut_all=True)
    target_signatur_string = ' '.join(text)

    my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=my_coloring,
                             max_font_size=40, random_state=42,
                             font_path=os.path.join(d, "simhei.ttf")).generate(target_signatur_string)
    image_colors = ImageColorGenerator(my_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    # 保存图片 并发送到手机
    my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
    # itchat.send_image("wechat_cloud.png", 'filehelper')