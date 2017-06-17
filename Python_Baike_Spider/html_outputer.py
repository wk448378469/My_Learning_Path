class HtmlOutputer(object):
	def __init__(self):
		self.datas = []
	
	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html','w',encoding='UTF-8')
		fout.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
		fout.write('<html>')
		fout.write('<body>')
		fout.write('<table>')
		for data in self.datas:
			fout.write('<tr>')
			fout.write('<tb>%s</tb>'%data['url'])
			fout.write('<tb>%s</tb>'%data['title'])
			fout.write('<tb>%s</tb>'%data['summary'])
			fout.write('</tr>')

		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')

		fout.close()