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
	$("#button1").click(function() {
		if($("#id").val() ==""){
			//alert("ID가 입력되지 않았습니다.");
			$("#idCheck").html("<font color='red'>ID가 입력되지 않았습니다.</font>");
			 return false;
		}else if($("#id").val().length < 3){
			//alert("ID가 3글자 이상 되어야 합니다.");
			$("#idCheck").html("<font color='blue'>ID가 3글자 이상 되어야 합니다.</font>");
			 return false;
		}else{
			//alert("ID의 유효성 검사 끝.");
			$("#idCheck").text("ID의 유효성 검사 끝.");
			return false;
		}
	});
	
	$("#button2").click(function() {
		/* ----------------------------------------------------  */
		var pw1 = $("#pw1").val();
		var pw2 = $("#pw2").val();
		
		console.log(pw1);
		console.log(pw2);
		
		if(pw1 == pw2){
			$("#pw2").after("<font color='blue'>패스워드가 일치합니다..</font>");
			console.log("ok");
			return false;
		}else{
			$("#pw2").after("<font color='red'>패스워드가 불일치합니다..</font>");
			return false;
		}
	});
	
	$("#form").submit(function() {
		var d = $(this).serialize();
		$.ajax({
			url: "reply.jsp",
			data: d,
			success: function(result) {
				//alert("ajax성공..!!!!");
				$("#idCheck").text("ajax 통신 결과: " + result);
			} //success
		}); //ajax
		return false;
	}); //click
});
</script>
</head>
<body>
<form action="insert.do" id="form">
아이디: <input type="text" name="id" id="id">
<div id="idCheck"></div>
<button id="button1">ID체크</button>
<button type="submit">ID중복 체크(Ajax통신)</button>
<br>
패스워드1: <input type="text" name="pw" id="pw1"><br>
패스워드2: <input type="text" name="pw2" id="pw2">
<button id="button2">패스워드 동일 여부 확인 처리</button><br>
이름: <input type="text" name="name"><br>
연락처: <input type="text" name="tel"><br>

</form>








</body>
</html>