#!python
print("Content-Type: text/html; charset=euc-kr\n")
import sys
import codecs
import cgi
import cgitb
sys.stdout = codecs.getwriter("euc-kr")(sys.stdout.detach())
cgitb.enable()
form = cgi.FieldStorage()
if 'id' in form:
	pageId = form.getvalue('id')
	description = open('data/'+pageId, 'rt', encoding='UTF8').read()
else:
	pageId = '합격을 위해!'
	description = '열심히 공부하자'

print('''<!doctype html>
<html>
<head>
	<title> 공인회계사 1차 나만의 요점정리 in web</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="index.py">공인회계사 1차</a></h1>
	<ol>
		<h2>회계학</h2>
		<li><a href="index.py?id=intermediate">중급회계</a></li>
		<li><a href="index.py?id=advanced">고급회계</a></li>
		<li><a href="index.py?id=government">정부회계</a></li>
		<li><a href="index.py?id=managerial">원가관리회계</a></li>
	</ol>
	<ol>
		<h2>세법개론</h2>
		<li><a href="index.py?id=corporate_tax">법인세법</a></li>
		<li><a href="index.py?id=VAT">부가가치세법</a></li>
		<li><a href="index.py?id=private_income">소득세법</a></li>
		<li><a href="index.py?id=GookGi">국세기본법</a></li>
		<li><a href="index.py?id=SangZeung">상속세및증여세법</a></li>
	</ol>
	<ol>
		<h2>경제원론</h2>
		<li><a href="index.py?id=Microeconomics">미시경제학</a></li>
		<li><a href="index.py?id=거시경제학">거시경제학</a></li>
		<li><a href="index.py?id=국제경제학">국제경제학</a></li>
	</ol>
	<ol>
		<h2>경영학</h2>
		<li><a href="index.py?id=Financial_Management">재무관리</a></li>
		<li><a href="index.py?id=일반경영학">일반경영학</a></li>
	</ol>
	<ol>
		<h2>상법</h2>
		<li><a href="index.py?id=상법">상법</a></li>
	</ol>
    <h2>{title}</h2>
	<p>{desc}</p>
	<a href="http://nbcpa.co.kr/shop/"
	target="blank">늘벗서점</a>
	<p>
    <iframe width="900" height="506" src="https://www.youtube.com/embed/ZG3ShkIrX7I" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
	</p>

</body>
</html>
'''.format(title=pageId, desc=description))
