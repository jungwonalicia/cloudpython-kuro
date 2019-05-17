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
	$("#json").click(function() {
		$.ajax({
			url:"resources/json/MOCK_DATA.json", //연결할 주소
			dataType: "json",
			success: function(result) {
						//result == list <= 객체의 리스트.
						if(result.length > 0){
							$("#result1").html("MOCK data가 존재 성공" + "<br><br>");
							$(result).each(function(index, member) {
								console.log(member);
								var id = member.id;
								$("#result1").append("ID: " + id + "<br>");
								var first_name = member.first_name;
								$("#result1").append("이름: " + first_name + "<br>");
								var last_name = member.last_name;
								$("#result1").append("성: " + last_name + "<br>");
								var first_name = member.first_name;
								$("#result1").append("이름: " + first_name + "<br>");
								var email = member.email;
								$("#result1").append("이메일: " + email + "<br><br>");
								
							}); //each
						} //if
			} //success
		}); //ajax
		return false;
	}); //click
});
</script>
</head>
<body>
<button id="json">JSON문서 읽어서 추출하기</button>
<div id="result1"></div>









</body>
</html>