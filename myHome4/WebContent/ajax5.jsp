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
	$("#xml").click(function() {
		$.ajax({
			url:"resources/xml/dataset.xml", //연결할 주소
			dataType: "xml",
			success: function(result) {
				var list = $(result).find("record"); //태그검색
				if(list.length>0){
					$("#result1").text("record가 존재.");
					$(list).each(function() {
						var id = $(this).find("id").text();
						var first_name = $(this).find("first_name").text();
						var email = $(this).find("email").text();
						var gender = $(this).find("gender").text();
						$("#result1").append("<h3>"+id+"</h3>");
						$("#result1").append("<h3>"+first_name+"</h3>");
						$("#result1").append("<h3>"+email+"</h3>");
						$("#result1").append("<h3>"+gender+"</h3><br>");
					});
				}
			}
		});
		return false;
	});
});
</script>
</head>
<body>
<button id="xml">XML문서 읽어서 추출하기</button>
<div id="result1"></div>









</body>
</html>