import xlwt

# 写入Excel文件
def generate_excel(dict,savepath):
	try:
		'''
		m = pd.DataFrame(dict, index=[0])
		print(m.head())
		print(m.describe())
		pd.read_excel('dict.xls')
		'''
		# 创建工作表
		excel = xlwt.Workbook(encoding="utf-8", style_compression=0)
		sheet = excel.add_sheet("今日爬取到的车票情况", cell_overwrite_ok=True)
		col = ['状态', '车次', '出发时间', '到达时间', '出发地', '目的地', '历时', '软卧一等卧', '硬座二等座', '硬座', '无座']
		# 制定写入规则
		for i in range(0, 10):
			sheet.write(0, i, col[i])
			break
		for i in range(0, 100):
			dic = dict[i]
			for j in range(0,10):
				sheet.write(i+1, j,dic[j])
		excel.save(savepath)
	except Exception as e:
		print('异常', str(e))

if __name__ == '__main__':
	generate_excel()



	'''
	sheet.write(0, 0, "状态")
	sheet.write(0, 1, "车次")
	sheet.write(0, 2, "目的地")
	sheet.write(0, 3, "出发地")
	sheet.write(0, 4, "出发时间")
	sheet.write(0, 5, "到达时间")
	sheet.write(0, 6, "历时")
	sheet.write(0, 7, "软卧一等卧")
	sheet.write(0, 8, "硬座二等座")
	sheet.write(0, 9, "硬座")
	sheet.write(0, 10, "无座")
	row = 1
	col = 0
	
	
	for i in (dict):
		sheet.write(row, col, str(dict['状态']))
		sheet.write(row, col + 1, str(dict['车次']))
		sheet.write(row, col + 2, str(dict['目的地']))
		sheet.write(row, col + 3, str(dict['出发地']))
		sheet.write(row, col + 4, str(dict['出发时间']))
		sheet.write(row, col + 5, str(dict['到达时间']))
		sheet.write(row, col + 6, str(dict['历时']))
		sheet.write(row, col + 7, str(dict['软卧一等卧']))
		sheet.write(row, col + 8, str(dict['硬座二等座']))
		sheet.write(row, col + 9, str(dict['硬座']))
		sheet.write(row, col + 10, str(dict['无座']))
		excel.save('dic.xls')
		row += 1
		excel.close()
	'''

