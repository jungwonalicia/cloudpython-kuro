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
		$("#result1").empty();
		$.ajax({
			url:"https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.chosun.com%2Fsite%2Fdata%2Frss%2Frss.xml&api_key=rooa9cfdnkctmsnpiftxnozlzfyaunxvudzwajoq", //연결할 주소
			dataType: "json",
			data: {
				url: "http://www.chosun.com/site/data/rss/rss.xml", //원래 사이트 주소
				api_key: "rooa9cfdnkctmsnpiftxnozlzfyaunxvudzwajoq",
				count: 20
			},
			success: function(result) {
				console.log("신문기사 연결 성공!!!");
				var list = result.items;
				console.log(list);
				$(list).each(function(index, news) {
					var title = news.title;
					console.log(title);
					var link = news.link;
					console.log(link);
					$("#result1").append("<a href=" + link + ">" + title +"</a><br>");
				});
			}//success
		});//ajax
		return false;
	});
	
	$("#xml2").click(function() {
		$("#result1").empty();
		$.ajax({
			url:"https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.chosun.com%2Fsite%2Fdata%2Frss%2Fent.xml&api_key=rooa9cfdnkctmsnpiftxnozlzfyaunxvudzwajoq", //연결할 주소
			dataType: "json",
			data: {
				url: "http://www.chosun.com/site/data/rss/ent.xml", //원래 사이트 주소
				api_key: "rooa9cfdnkctmsnpiftxnozlzfyaunxvudzwajoq",
				count: 20
			},
			success: function(result) {
				console.log("신문기사 연예 연결 성공!!!");
				var list = result.items;
				console.log(list);
				$(list).each(function(index, news) {
					var title = news.title;
					console.log(title);					
					var link = news.link;
					console.log(link);
					var img = news.thumbnail;
					$("#result1").append("<a href=" + link + ">" + title +"</a><img width=100 height=100 src=" + img + "><br>");
				});
			}//success
		});//ajax
		return false;
	});
});
</script>
</head>

<body>
<button id="xml">신문기사 속보</button>
<button id="xml2">신문기사 연예</button>
<button id="xml3">신문기사 포토</button>
<div id="result1"></div>









</body>
</html>