#!/usr/bin/env bash
# Scripts that displays the visitor IP along with the HTTP status code from the Apache log file

awk '{print $1 " "$9}' < apache-access.log
