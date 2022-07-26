GET https://app.mural.co/api/public/v1/authorization/oauth2/? 
  client_id=:client_id&
  redirect_uri=:callback&
  scope=:scope&
  state=:state&
  response_type=code

 curl -sH 'Authorization: Bearer <>'
    'https://app.mural.co/api/public/v1/workspaces'