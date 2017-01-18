#!/bin/sh

bundle install
open /Applications/Google\ Chrome.app 'http://localhost:4000'
bundle exec jekyll serve
