<table id="mytable" cellspacing="0">
    <tr  scope="col" >
        <th>Url</th><th>Username</th><th>Password</th>
    </tr>
  % for password in passwords:
    <tr>
        <td>{{password["url"]}}</td><td>{{password["username"]}}</td><td>{{password["password"]}}</td>
    </tr>
  % end
</table>