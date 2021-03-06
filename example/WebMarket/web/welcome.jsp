<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%--    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">--%>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <title>Welcome</title>
</head>
<body>
<%@include file="menu.jsp" %>
<%! String greeting = "Welcome to Web Shopping Mall";
    String tagline = "Welcome to Web Market!";%>
<div class="jumbotron">
    <div class="container">
        <h1 class="display-3">
            <%= greeting%>
        </h1>
    </div>
</div>
<main role="main">
    <div class="container">
        <div class="text-center">
            <h3>
                <%=tagline%>
            </h3>
            <%
                response.setIntHeader("Refresh", 5);
                out.print(new java.util.Date());
            %>
        </div>
    </div>
</main>
<%@include file="footer.jsp" %>
</body>
</html>
