<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<link href="resources/css/css.css" 
	  type="text/css"
	  rel = "stylesheet"
>
<script type="text/javascript" src="resources/js/jquery.min.js"></script>
<script type="text/javascript">
$(function() {
	//태그 사이의 컨텐츠
	var h1 = $("h1").text();
	console.log("h1의 텍스트 컨텐츠 : " + h1);
	
	//input태그의 값
	var input = $("#today").val();
	console.log("input의 입력값 : " + input);
	
	//속성의 값
	var src = $("img").attr("src");
	console.log("img의 속성값 : " + src);
	
	
	
	
});


</script>
</head>
<body>
<h1>오늘은 월요일</h1>
<input type="text" 
	name="today" 
	id="today"
	value="월요일"
	>
<br>
<img src="resources/img/001.png">




</body>
</html>