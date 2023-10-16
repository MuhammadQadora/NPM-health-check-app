# NPM-health-check-app
This application is comprised of two microservices, one called Resty which the user communicates with to get the health of an NPM package. The second is Healthy which actually does the logic of checking
if the NPM package is healthy or not. It does so by checking if a last commit was done in the past 14 days, if the package has two or more maintainers, and if the npm version was updated in the past 30 days.
