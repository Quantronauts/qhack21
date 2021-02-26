# Problem set repo
### Status problem set
<table>
	<tbody>
		<tr>
			<td>
				<table>
					<thead>
						<tr>
							<th align="center">Problem set</th>
							<th align="center">1</th>
							<th align="center">2</th>
							<th align="center">3</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td align="center">Simple Circuit</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
						</tr>
						<tr>
							<td align="center">Quantum Gradients</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
						</tr>
						<tr>
							<td align="center">Circuit Training</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
						</tr>
						<tr>
							<td align="center">VQE</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
							<td align="center">:white_check_mark:</td>
						</tr>
					</tbody>
				</table>
			</td>
			<td>
				<img src="ranking_challenge_set.png">
			</td>
		</tr>
	</tbody>
</table>

**Legend** :
- *submited* : :white_check_mark:
- *done but not submit* : :ballot_box_with_check:
- *todo* : :x:

## Problem Categories<a name="categories" />

The Challenge problems are divided into 4 categories: 

- Simple Circuits
- Quantum Gradients
- Circuit Training
- Variational Quantum Eigensolver (VQE)

Each category contains 3 problems worth differing amounts of points. The "Simple Circuits" problem set contains questions valued at 20, 30, and 50 points. This category is intended primarily as a tutorial so you can get used to the submission process, as well as learn the basics of [PennyLane](https://pennylane.ai), the software library in which all the problems are written. The other three categories have problems valued at 100, 200, and 500 points. 

**The challenges may be completed in any order**, but for true beginners we recommend starting with the *Simple Circuits* problems before progressing to the more challenging ones. While in some cases solving the lower-valued problems will provide insight into the higher-valued ones, all of the problems are intended to be self-contained and do not require any code or numerical values to be carried forward through a category.

### What's Provided For You<a name="provided" />

Every problem in the Coding Challenge has a corresponding directory nested under `QML_Challenges/` of the form `<problem_name>_<points>_template/`. Within each problem template folder are three types of files to help you with the coding challenges:  

1. **problem.pdf**  
	This is the statement of the problem you're being challenged to solve, along with any constraints that may be imposed. Read these over carefully before tackling the corresponding Coding Challenge problem. If you're having problems viewing these you can also find a description of the problems at [the Challenge Problems page](https://challenge.qhack.ai/public/problems).

2. **\<problem_name\>_\<points\>_template.py**  
	These are the Python coding templates required for submitting your solution to a particular problem. Read the docstrings within these files carefully to see what code is required from you and where exactly you should add your solution (typically between `# QHACK #` comment markers).   
	**NOTE:** It is extremely important that you do not import any additional libraries or modify any of the code in these files other than where specified, as this may result in your submission failing the automated judging process. See the sections below on testing your solutions locally and submitting them for judging.   
3. **\#.in and \#.ans files**  
	The numbered `.in` and `.ans` files are the input and corresponding expected output, respectively, for your solution. They are the data files for the problem. Do not modify these files! Once you have added your code to the `<>_template.py` file, passing the `#.in` file to the modified `<>_template.py` file via `stdin` should result in output that matches the corresponding `#.ans` file. Your generated answer may not match the value(s) in the corresponding `#.ans` file exactly, but that's normal. As long as they match to within a tolerance specified in the `problem.pdf` file, then your solution will be judged to be correct. More details on how to test your solutions locally are provided in a section below.

## Setting Up Your Environment<a name="setup" />

All solutions must be written in Python and be compatible with Python 3.7. Instructions for installing Python 3.7 are out of scope for this document, but many web resources exist for how to install Python 3.7 on your chosen OS.

We have included a [requirements.txt](https://github.com/XanaduAI/QHack/blob/main/QML_Challenges/requirements.txt) file that specifies the libraries which you will need to be able to run and test your solutions locally. Installing these can be done on the command line via `pip`:  

```console
pip install -r requirements.txt
```  

We recommend that you set up a virtual environment to keep these packages isolated from the rest of your installed Python libraries. Setting up a virtual environment is also out of scope for this document, but many tutorials for doing so with your Python distribution and OS are available online. 

## Testing Your Solutions<a name="testing" />

Once you have added your code to one of the solution templates, you can test if it is correct by supplying one of the `#.in` files for that problem to the solution script via stdin. 

For example, if you've added a solution for the 100 point Circuit Training problem and you want to test the solution using the first set of inputs, do the following:
 * Open a terminal console (`CMD`, `Terminal`, etc.) and navigate to the folder containing your solution
 * Run your modified Python template and pass in the inputs:  
`python ./circuit_training_100_template.py < 1.in`
 * Check what was output to the console. If everything worked, you should see a single number or series of comma delimited numbers and nothing else
 * Open the file `1.ans` for this problem and compare its contents to what was written to the command line. They should match to within some tolerance specified in the `problem.pdf` to be judged correct.
 * 
