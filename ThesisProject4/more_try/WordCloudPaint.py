from wordcloud import WordCloud
import matplotlib.pyplot as plt



# produce wordcloud from list of words'frequence.txt
# 如果直接读取counts_result字典，wc1 = wc.fit_words(counts_result)即可
def main():
	creat_wc()


def creat_wc():
	fre = {}
	for line in open(r'F:\Demo\ThesisProject4\负面词频统计.txt'):
		arr = line.split(',')
		fre[arr[0]] = int(arr[1])
	wc = WordCloud(
		background_color='white',
		font_path=r'C:\Windows\Fonts\msyh.ttc',
		max_words=500,
		width=1000,
		height=1000,
		max_font_size=100,
		min_font_size=10,
		relative_scaling=0.3
	).generate_from_frequencies(fre)
	wc.to_file('wordcloud_from_fre_neg.png')
	plt.imshow(wc)
	plt.axis('off')
	plt.show()


if __name__ == '__main__':
	main()
	print('从字典/字典文件生成词云成功！')
