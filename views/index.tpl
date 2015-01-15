<link rel="stylesheet" type="text/css" href="passwords.css" />

<h1 style="text-align: center">SlyScoop C&C</h1>

<div id="left" style="width: 50%; float: left; display:inline-block">
    <h2>Parsed Passwords</h2>
    % include('password_template.tpl', passwords=passwords)
</div>
<div id"right" style="width: 50%; display:inline-block">
    <h2>Running Logs</h2>
    <p>{{logs}}</p>
</div>