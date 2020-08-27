# Simple Network Test

[![Build Status](https://dev.azure.com/scottbreitenbach/scottbreitenbach/_apis/build/status/sbreitenbach.simple-network-test?branchName=master)](https://dev.azure.com/scottbreitenbach/scottbreitenbach/_build/latest?definitionId=4&branchName=master) [![Version](https://img.shields.io/github/v/release/sbreitenbach/simple-network-test)](https://img.shields.io/github/v/release/sbreitenbach/simple-network-test)


I wrote the script to gather better data when troubleshooting my network with my internet service provider. 
It simply pings some host, in my case a cloud based virtual machine, and logs the result. 
It works well on a Raspberry Pi but it can run on any modern Windows, Mac, or Linux machine. 
I added an optional text message notification that is sent following an outage. 
