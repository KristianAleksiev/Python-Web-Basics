"""
1. Introduction to Internet
- Fiber optics, copper, satellites, cell phone networks
- Indirect connection through ISPs
- Internet - Huge device network all over the globe, which communicate with each other and work together
- Local network - Internet - Same fundament

Client server work model - client - server - (technology - request dynamics - django, asp) - resources - response

2. Important definitions
- Server - Provides services to other machines
- Client - The machines that request those services from the server, web requests
-
3. HTTP Basics
- Requests are made through protocols
- If the resources exist, the server response is successful(200), if not 404

HTTP Request methods:
CRUD methods
- POST - Create / Store a resource
- GET - Read / Retrieve a resource
- PUT - Update / Modify a resource
- DELETE - Delete / Remove a resource

- PATCH - Partial update of the resource
- HEAD - Does a resource exist check, if does => GET
- OPTIONS

4. URL- Uniform Resource Locator
- Unique
- Protocol://Host/Path?Query string#Fragments
- Working with HTTP - Ports 80 / 443

x.bg => x.bg:80 - http default port
x.bg => x.bg:443 - http secured default port

5. Tools for Devs
- Postman, curl

6. MIME and media types
- Multi-purpose Internet Mail Extension - Client reactions to result -> css, json etc.
- What is the server's response desired - specific format

7. Request and Response
HTTP Requests
- HTTP Request line (method, URI, protocol)
- HTTP Request headers (additional params) - metadata
- HTTP Request body (optional data)

HTTP Response
- HTTP Response Status line
- HTTP Response headers
- HTTp Response body

"""