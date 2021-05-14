# Simple Showcase

This is a personal project inspired by Shopify intern challenge question.<br>
Simple Showcase is an e-commerce-like web app helping users manage and demonstrate products/images. Users can sign up an account and log in, then add new products by providing product information and uploading a number of images. The images can be labeled as 'private' so that they will be privately visible, otherwise, demonstrated publicly. <br>

<!-- Simple Showcase is also deployed onto Heroku, click [here](https://shopify-challenge-proj.herokuapp.com/) to visit. -->

## Demo

![Demo](https://lh3.googleusercontent.com/ptNIYKBGnNTaymzfODNvHScj4egQBCkv_0X2ecJ3VSqq042pyKwiCowQoAMxpzp23ZqcZPfsH5oEVf0QdhC_Q6uf2Pdynf8iYW03euJQQNGEsTIUBzxV7KfmfnrRkFTLtS1GBgs-LmE-_gHwsABD-fxEHCtrLxwwvZiCUYC0uBsiuxHebF-NvxBdrrL-_hBMD6xBxc7XoErrENOQUfU8LtQEeP6JGo8GNHHTWKlelPWZwvOmw4_sHg3Ars1sTtDqlXPkCZwTT3ZMBc2jPyQxUiukgyNtSJKheOJJWXiPZp-X6Lq6jX4h66Ye9GX9a8iQsoxOs5LicLuvF5-sjWOV2yWh-GAsH1jK2IihBHwUcMtRgPtmnE78bCiv0xwvxKtDm9ehIUdsnsw7uNu5DiLnsNLCI9zYzMDV-4hLDr0tWBJCUlOBIYy7qZr9Uu1tUbT7BJzWwae2v5bqKGuJwZg5hDeCGYKNK_mJ8FvyZzXPOVdmuoSiv4L8MaFmvOmTcaRvRpuKybvBIktaExIl1dgSf3HEv2LqBPGVSH8dAfev3s1mLdCgpM63d33_lirHKFpg-pcscaL0pwp5MIte1aK-eKWIFMM_USDLaCBhqiceXmvwbV5dquNDcnqMNGQYEyEGqXvo1uXEQ6NzttePhX2keQP_GZJVQ3MCHX49OilothObc3eMmCAngwT7bk1rVEdw4pTfOttcz9HVxm8d72F55vIF=w1280-h728-no?authuser=0)

## Getting Started

<!-- These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. -->

### Prerequisites

To run the app, first please install the dependancies:

```
pip install flask flask-sqlalchemy flask-login
```

### Installing

<!-- A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo -->

Clone this repo and enter the directory.
Then configure and run it:<br>

```
export FLASK_APP=project
```

The <span style="background-color:grey">FLASK_APP</span> environment variable instructs Flask how to load the app.

```
export FLASK_DEBUG=1
```

The <span style="background-color:grey">FLASK_DEBUG</span> environment variable is enabled by setting it to 1.

```
flask run
```

Flask will monitor changes to app files and reload the server when there’s a change. No bothering to turn it off and on for each single change.

<!-- ## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system -->

## Built With

- [Flask](https://flask.palletsprojects.com/) - Flask is a lightweight WSGI web application framework.
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application.
- [Flask Login](https://flask-login.readthedocs.io/) - Flask-Login provides user session management for Flask.

<!-- ## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Billie Thompson** - _Initial work_ - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc -->

## Todo

- Search function
- Business features such like: PURCHASE, DISCOUNT, MONEY HANDLING
- Deployment onto Heroku

