# qhack21 - Quant'ronauts
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
Team repository for QHACK21

## Table of contents
1. [Structure](#structure)
2. [Setup env](#setup_env)

## Structure <a name="structure"></a>
- Folder :
	- problem_set : folder for the problems set challenge
	- hackaton : folder for our project
- Branchs :
	- main : only for archive and tag
	- develop : for merging and testing everything together
	- feature : to develop things

## Setup env <a name="setup_env"></a>
### Create your virtual env
- To create your virtual env I suggested to use [Anaconda](https://www.anaconda.com/products/individual)
	- If you are on Linux you can setup your virtual env by using :
		- <details><summary>Linux env</summary>
			<pre>
			toto$ ( echo; echo '##### added for quantum #####';
			echo 'export PATH=/home/toto/.local/bin:$PATH';
			echo "alias quantum='source ~/quantum/bin/activate'" ) >> ~/.bashrc
			toto$ . ~/.bashrc
			toto$ pip3 install --upgrade pip
			toto$ python3 -m pip install virtualenv
			toto$ python3 -m virtualenv quantum
			toto$ quantum
			</pre>
		</details>

- Inside your env, check your python installation :
```
conda activate name_of_my_env
python --version
```
- :warning: Be careful some quantum libs have problem with :x: **python 3.9**, so stop yourself to **[python 3.8](https://www.python.org/downloads/release/python-387/)** :
`pip install python==3.8.7`

### Installing libraries
To run our project you'll need a bunch of libraries, to installed them run the following command :
```
pip install pennylane
pip install pennylane-qiskit
pip install pennylane-sf

# For numpy install the following lib
pip install autograd
pip install torch torchvision
```
In case you have python 2.x and python 3.x cohabited on your virtual system, use `pip3` instead of `pip`

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/saharbenrached"><img src="https://avatars.githubusercontent.com/u/58570811?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sahar Ben Rached</b></sub></a><br /><a href="https://github.com/mickahell/qhack21/commits?author=saharbenrached" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/AlainChance"><img src="https://avatars.githubusercontent.com/u/43089974?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Alain</b></sub></a><br /><a href="https://github.com/mickahell/qhack21/commits?author=AlainChance" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Zed-Is-Dead"><img src="https://avatars.githubusercontent.com/u/7906730?v=4?s=100" width="100px;" alt=""/><br /><sub><b>LQuerellaZ</b></sub></a><br /><a href="https://github.com/mickahell/qhack21/commits?author=Zed-Is-Dead" title="Code">💻</a></td>
    <td align="center"><a href="http://q-edu-lab.com"><img src="https://avatars.githubusercontent.com/u/72672758?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Tamás Varga</b></sub></a><br /><a href="https://github.com/mickahell/qhack21/commits?author=tvarga78" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/mickahell"><img src="https://avatars.githubusercontent.com/u/20951376?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Mica</b></sub></a><br /><a href="https://github.com/mickahell/qhack21/commits?author=mickahell" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
