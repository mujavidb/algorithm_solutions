#Describe the process when the web browser loads the Facebook page

See here, from 2010: https://www.facebook.com/notes/facebook-engineering/bigpipe-pipelining-web-pages-for-high-performance/389414033919/

## The Process

1. User types facebook url and hits enter
2. Browser sends an HTTP request to facebook
3. Hits facebook's load balancer
4. Load balancer sends request for page to appropriate cluster
5. Request parsing: web server parses and sanity checks the HTTP request
6. Data fetching: controller fetches data from the storage tier
7. Markup generation: web server generates HTML markup for the response.
8. Network transport: the response is transferred from web server to browser.
9. Browser receives an HTTP response with an HTML file and parses it creating a DOM tree
10. CSS downloading: browser downloads CSS required by the page
11. CSS styles are applied to DOM tree
12. JavaScript downloading: browser downloads JavaScript resources referenced by the page.
13. JavaScript execution: browser executes JavaScript code of the page.

## Brownie points

* As Facebook's frontend runs asynchronously, when a user scrolls down the page facebook sends multiple get requests to download more content. These JSON requests are parsed and the part of the DOM for the appropriate pagelet is updated.
* As facebook serves billion of pages in a day, server load needs to be reduced so they built an Engine H.H.V.M that has J.I.T compiler in which, instead of interpreting the PHP code directly they convert it into assembly and run that instead that leads to crazy speeds.