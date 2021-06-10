const http = require("http");
const fs = require("fs");
const port = 3000;
const hostname = "localhost";


const server = http.createServer((req, res) => {
  console.log("request url", req.url);
  console.log("request method", req.method);

  res.setHeader("Content-Type", "text/html");

  let route = "./views/";
  switch (req.url) {
    case "/":
        
      route += "index.html";
      break;
    case "/contact":
      route += "contact.html";
      break;
	case "/contact-us":
		res.statusCode = 301;
		res.setHeader('Location', '/contact');
		res.end()
      break;
    default:
		res.statusCode= 400
      	route += "404.html";
      break;
  }

  fs.readFile(route, (err, data) => {
    if (err) {
      console.log(err);
      res.end();
    } else {
      res.end(data);
    }
  });
});

server.listen(port, hostname, () => {
  console.log(`listenin on port ${port}`);
});
