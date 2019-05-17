<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="resources/js/jquery.min.js"></script>
<script type="text/javascript">
$(function() {
	$("#form").submit(function() {
		var d = $(this).serialize();
		$.ajax({
			url:"ok.jsp", //연결할 주소
			data: d , //넘길 데이터
			success: function(result) {
				$("#result").text(result);
			}
		});
		return false;
	});
});
</script>
</head>
<body>
<form id="form">
오늘은? <input type="text" id="today" name="today">
<div id="result"></div>
<button type="submit">서버로 전송</button>
</form>









</body>
</html>