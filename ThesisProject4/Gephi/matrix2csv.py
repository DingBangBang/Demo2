import pandas as pd


def convert_csv(matrix):
	i = 0
	df = pd.DataFrame(columns=['Source', 'Target', 'Weight'])
	for row in range(1, len(matrix)):
		for col in range(1, len(matrix)):
			if col >= row:
				if matrix[col][row] != '':
					df.loc[i] = [matrix[0][row], matrix[col][0], matrix[col][row]]
					i += 1
	df.to_csv('Gephi数据.csv', index=False)
	print(df)


matrix = pd.read_excel(r'.\RAW.xls', encoding='utf-8')
convert_csv(matrix)
