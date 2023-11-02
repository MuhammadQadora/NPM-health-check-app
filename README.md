# PS: This is not the final code. The code requires further enhancements such as error handling and Threading.

# NPM-health-check-app
This application is comprised of two microservices, one called Resty which the user communicates with to get the health of an NPM package. The second is Healthy which actually does the logic of checking
if the NPM package is healthy or not. It does so by checking if a last commit was done in the past 14 days, if the package has two or more maintainers, and if the npm version was updated in the past 30 days.


usage:

1)

start by exporting a github token:
export token="XXXXXXXXXXXXXX"

2)

using Curl or Postman make a POST request to "http://localhost:5000/resty". insert a plain/text package name or a comma seperated npm package list
example:
package1,package2,package3

an Example Response from the app:

{
    "results": [
        "package1 is not healthy",
        "package2 is not healthy",
        "package2 is healthy"
    ]
}