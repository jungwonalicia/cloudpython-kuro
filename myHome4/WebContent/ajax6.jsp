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
			url:"resources/json/rank2.json", //연결할 주소
			dataType: "json",
			success: function(result) {
						var list = result.rank; //반환변수.키
						//list <= 객체의 리스트.
						if(list.length > 0){
							$("#result1").html("rank가 존재 성공" + "<br>");
							$(list).each(function(index, member ) {
								//$("#result1").append("선수 등장..");
								console.log(member);
								var name = member.name;
								var tel = member.tel;
								$("#name").val(name);
								$("#tel").val(tel);
								
								var inputData = $("#form").serialize();
								
								$.ajax({
									url: "rank.do",
									data: inputData
								});
								
								//$("#result1").append("이름: " + name + "<br>");
								//$("#result1").append("전화번호: " + tel + "<br><br>");
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
<form id="form">
이름: <input type="text" name="name" id="name"><br>
전화번호: <input type="text" name="tel" id="tel"><br>
</form>








</body>
</html>