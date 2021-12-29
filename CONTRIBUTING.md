# Contributing to Nittfest-Server

**NOTE: **

Never push directly to main repository(upstream). Only push to your forked repo(origin) and send a pull request to
the main repository

---

# <a id="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

- The coding style to be followed along with instructions to use python lint

# <a id="commit"></a> Git Commit Guidelines

# Commit Message Format

Each commit message consists of a ** header**, a ** body ** and a ** footer**. The header has a special
format that includes a ** type**, a ** scope ** and a ** subject**:
* Head
```bash
<type > ( < scope > ): < subject >
```
* Body
```bash
In this PR,
<body_content >
```

Any line of the commit message cannot be longer 100 characters! This allows the message to be easier to read on github
as well as in various git tools.

# Example Commit Message
* Head
```bash
feat(DAuth): Add DAuth Authentication
```
* Body
```bash
In this PR,
Implemented API class to fetchAccessToken and fetchProtectedResources from Dauth server.
   - Takes AuthorizationRequest as Input.
       - AuthorizationRequest includes:
           -  client_id: [Obtained during App registration in Dauth Website]
           -  client_secret: [Obtained during App registration in Dauth Website]
           -  redirect_uri: [Preferably the one given during App registration in Dauth Website]
           -  state: [Returned along with Token for verification of token.(Prevents CSRF attacks)]
           -  scope: [Includes feature of requesting openId, email, phone_number, profile of the resource owner]
           -  request_type: [By Default it has value of 'code' for Authorization Code Grant Flow]
           -  grant_type: [By Default it has value of 'authorization_code' for Authorization Code Grant Flow]

      -  Automate the  Authorization Code Grant Flow by:
           - Dauth Automatically takes care of authentication proccess and navigates to `redirect_uri` and `code` is retrived.
           - Using the `code` a post request is automated to `tokenEndPoint` and we receive the  `access token` as a response.
           - The Access token is used to request for protectedResources specified in the scope and returns the Resource Response.
```
