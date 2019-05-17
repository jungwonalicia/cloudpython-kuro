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
			url: "reply.jsp" ,
			data: d,
			success: function(result) {
				$("#total").append(result + "<br>");
			}//success 
		});//ajax
		return false;
	});//submit
});//ready
</script>
</head>
<body>
<h3>아래 이미지에 대한 느낌을 적어주세요</h3>
<img src="resources/img/003.png" width="250"><br>
<form id="form">
입력 <input type="text" id="reply" name="reply">
<button type="submit">댓글달기</button><br>
</form>
<hr color="red">
<div id="total"></div>
</body>
</html>