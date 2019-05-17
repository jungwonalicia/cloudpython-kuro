<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="resources/css/css.css" type="text/css" rel="stylesheet">
<script type="text/javascript" src="resources/js/jquery.min.js"></script>
<script type="text/javascript">
	$(function() {
		$("button").click(function() {

			var select = $("#select").val();

			if (select == "네이버") {
				location.href = "http://www.naver.com";
			} else if (select == "다음") {
				location.href = "http://www.daum.net";
			} else if (select == "구글") {
				location.href = "http://www.google.com";
			} else {
				location.href = "http://www.kgitbank.com";
			}
		});
	});
</script>
</head>
<body>
	<select name="portal" id="select">
		<option>네이버</option>
		<option selected="selected">다음</option>
		<option>구글</option>
		<option>KGITBANK</option>
	</select>

	<button>나를 누르면 해당 사이트로 이동</button>





</body>
</html>