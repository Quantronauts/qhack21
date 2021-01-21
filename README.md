# qhack21
Team repository for QHACK21, I'll change the name when we'll have a proper team name

## Structure
- main : only for archive and tag
- develop : for merging and testing everything together
- feature : to develop things

## Setup env
### Create your virtual env
- To create your virtual env I suggested to use [Anaconda](https://www.anaconda.com/products/individual)
	- If you are on Linux you can setup your virtual env by using :
<details>
	<summary>Linux env</summary>
	```
	toto$ ( echo; echo '##### added for quantum #####';
	echo 'export PATH=/home/toto/.local/bin:$PATH';
	echo "alias quantum='source ~/quantum/bin/activate'" ) >> ~/.bashrc
	toto$ . ~/.bashrc
	toto$ pip3 install --upgrade pip
	toto$ python3 -m pip install virtualenv
	toto$ python3 -m virtualenv quantum
	toto$ quantum
	```
 </details>

- Inside your env, check your python installation. Be careful some quantum libs have problem with python 3.9, so stop yourself to [python 3.8](https://www.python.org/downloads/release/python-387/) :
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