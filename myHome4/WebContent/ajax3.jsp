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
		$("#result").empty(); //DOM에서 해당 노드를 제거
		
		var d = $(this).serialize();
		$.ajax({
			url:"idCheck.do", //연결할 주소
			data: d , //넘길 데이터
			success: function(result) {
				//$("#result").text(result);
				//$("#result").html(result);
				$("#result").append(result);
			}
		});
		return false;
	});
});
</script>
</head>
<body>
<form id="form">
ID입력 <input type="text" id="id" name="id">
<div id="result"></div>
<button type="submit">ID중복 체크</button>
</form>









</body>
</html>