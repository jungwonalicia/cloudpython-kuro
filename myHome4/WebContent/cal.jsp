<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String num1 = request.getParameter("num1");
	String num2 = request.getParameter("num2");
	
	int n1 = Integer.parseInt(num1);
	int n2 = Integer.parseInt(num2);
			
	String oper = request.getParameter("oper");
	
	int result = 0;
	
	if(oper.equals("+")){
		result = n1 + n2;
	}else if(oper.equals("-")){
		result = n1 - n2;
	}else if(oper.equals("*")){
		result = n1 * n2;
	}else{
		result = n1 / n2;
	}
%>
두 수의 연산 결과는 : <%= result %>

