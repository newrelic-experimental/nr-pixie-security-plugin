[![New Relic Experimental header](https://github.com/newrelic/opensource-website/raw/master/src/images/categories/Experimental.png)](https://opensource.newrelic.com/oss-category/#new-relic-experimental)

# New Relic Security Plugin for Pixie 

> Identifies security issues in Pixie data and sends them to New Relic.

## Installation

> We recommend running and developing the project via Docker. Before getting started, make sure Docker is installed and running. You will also need a Pixie account and a New Relic account. 

## Getting Started
> 1. Save the following variables to your environment.
```bash
export NR_INSERT_KEY=<New Relic insert key>
export NR_ACCOUNT_ID=<New Relic account id>
export PIXIE_API_TOKEN=<Pixie api token>
export PIXIE_CLUSTER_ID=<Pixie cluster id>
``` 

(Optional) If you would like to set up monitoring of the plugin with New Relic, save your license key to your environment:
```
export NEW_RELIC_LICENSE_KEY=<New Relic license key>
```

> 2. Run the project via Docker.
```bash
docker-compose up -d
```
Note that you may get a warning from the Docker container if you did not export your license key to the environment. The license key is not necessary for running the plugin.

## Support
Because this project is an experimental proof of concept, we will not be maintaining this repo. However, we encourage you to discuss the project on our online forum.
New Relic hosts and moderates an online forum where customers can interact with New Relic employees as well as other customers to get help and share best practices. Like all official New Relic open source projects, there's a related Community topic in the New Relic Explorers Hub. You can find this project's topic/threads here:

> https://discuss.newrelic.com/t/new-relic-security-plugin-for-pixie/170293

## Contributing
Because this project is an experimental proof of concept, we will not review pull requests to this repo. We hope you will fork the project for your own experiments and share your work to the New Relic Exporers Hub. 

> https://discuss.newrelic.com/t/new-relic-security-plugin-for-pixie/170293

**A note about vulnerabilities**

As noted in our [security policy](../../security/policy), New Relic is committed to the privacy and security of our customers and their data. We believe that providing coordinated disclosure by security researchers and engaging with the security community are important means to achieve our security goals.

If you believe you have found a security vulnerability in this project or any of New Relic's products or websites, we welcome and greatly appreciate you reporting it to New Relic through [HackerOne](https://hackerone.com/newrelic).

## License
New Relic Security Plugin for Pixie  is licensed under the [Apache 2.0](http://apache.org/licenses/LICENSE-2.0.txt) License.
> New Relic Security Plugin for Pixie also uses source code from third-party libraries. You can find full details on which libraries are used and the terms under which they are licensed in the third-party notices document.
