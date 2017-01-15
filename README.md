# aqbanking-cli-wrapper

This project is aimed to provide an abstraction layer to get some data out ouf
HBCI enabled bank accounts using AqBanking as an interface.

## Requirements

- AqBanking with already configured accounts, since this wrapper is not supposed
  to take care of that (yet)

## Features

- Get a list of accounts configured with AqBanking
- Request the current balance of an account
- Request a list of all available transactions

## Installation

To install aqbanking-cli-wrapper with pip directly from the Git repository,
simply run `pip install git+git://github.com/hedderich/aqbanking-cli-wrapper.git`
