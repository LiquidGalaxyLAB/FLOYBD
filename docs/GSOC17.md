# GSoC 2017 - Ivan Josa

FlOYBD GSoC 17 project contains differents pieces of software, all of them contained within this repository and explained in the Readme file.

Basically, the system is formed by two different environments:
* On one hand, a cloud subsytem with a 2 node Spark Cluster with a Cassandra database has been developed. This system is the responsible of periodically gather the earthquakes and weather data through configured cronjobsans store it in a Cassandra database system. After this data has been fetched, it is analyzed and mined by a Spark installation and served via Flask with a Web Services layer.
* On the other hand, in a local environment, a web application implemented under the Django framework has been developed. This system fetch the data through Flask web services from the cloud system, displays them in a web interface and offers to the end user the possibility to display it in a Liquid Galaxy installation by creating and sending the corresponding KMLs files.

To easily understand this system separation, below an image is shown:

![Infrastructure](https://github.com/LiquidGalaxyLAB/FlOYBD/blob/master/implementacio.png)

It includes a [README](https://github.com/LiquidGalaxyLAB/FlOYBD/blob/master/README.md) with the project details and an install guide if you want to [Install](https://github.com/LiquidGalaxyLAB/FlOYBD/blob/master/docs/INSTALL.md) the full system

#### Links to the commits made during GSoC17

FlOYBD : [https://github.com/LiquidGalaxyLAB/FlOYBD/commits/master?author=navijo](https://github.com/LiquidGalaxyLAB/FlOYBD/commits/master?author=navijo)

Additionally, some minor changes has been made to the previous year (GSoC16) Liquid Galaxy Controller in order to adapt it to new Android versions as well as Chromebook OS. 

Liquid Galaxy Controller : [https://github.com/LiquidGalaxyLAB/Liquid-Galaxy-POIs-Controller/commits/master?author=navijo](https://github.com/LiquidGalaxyLAB/Liquid-Galaxy-POIs-Controller/commits/master?author=navijo)

<br>
<br>
<p align="center">
<img src="https://developers.google.com/open-source/gsoc/resources/downloads/GSoC-logo-horizontal.svg"  width="700">
</p>
