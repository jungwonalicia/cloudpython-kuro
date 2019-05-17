<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>jQuery UI Accordion - Default functionality</title>
<link rel="stylesheet"
	href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script>
	$(function() {
		$("#accordion").accordion();
		$("#dialog").dialog();
		$(document).tooltip();
	});
</script>
</head>
<body>
<div id="dialog" title="기본 다이얼로그">
<ul>
	<li><font color="red">이메일: </font>
		<font color="blue">gardenpro@daum.net</font>
	</li>
	<li><font color="red">전화번호: </font>
		<font color="blue" title="전화번호는 한국기본 082">011-123-4567</font>
	</li>
</ul>

</div>
	<div id="accordion">
		<h3>내가 좋아하는 음식</h3>
		<div>
			<ul>
				<li>라면</li>
				<li>우동</li>
				<li>순대</li>
			</ul>
		</div>
		<h3>내가 싫어하는 음식</h3>
		<div>
			<ul>
				<li>커피</li>
				<li>물</li>
				<li>홍차</li>
			</ul>
		</div>
		<h3>내가 좋아하는 곳</h3>
		<div>
			<ul>
				<li>한강</li>
				<li>종로</li>
				<li>강남</li>
			</ul>

		</div>
		<h3>내가 싫어하는 장소</h3>
		<div>
			<ul>
				<li>바다</li>
				<li>산</li>
				<li>도시</li>
			</ul>
		</div>
	</div>

</body>
</html>
