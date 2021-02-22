# Qats & DoQs
- Classifier of quantum cats and quantum dogs

## Structure <a name="structure"></a>
- Final script : `final_script.py`
- Folders :
	- datas : folder for the Qats and DoQs csv files
	- sensors : folder for the differents sensors (quantum generation)
	- classifiers : folder for the differents classifiers
	- combine : folder for the differents combining algorithms
	- training : folder for the differents training algorithms
	- testing : folder for the differents testing algorithms
	- graphs : folder for the differents graphs generation
	- communication : folder for images and ressources to present the project

## Idea <a name="idea"></a>
The classify regions of the Hilbert space. E.g. :
- The Northern hemisphere of the Bloch sphere is _cat_
- The Southern hemisphere is _dog_

### First create quantum state with variational parameters
- As first step, we create a parameterized sensor that can create state vectors that fall either into the _cat_ or _dog_ region. (As black box)
	- We could use any other sensor with different parameterization as long as it's capable of producing _dog_ and _cat_ states.
- Then, we feed the output state of the sensor into a parameterized classifier circuit
- Then, we optimize the classifier
- Finally measure them and drawing graph

<pre>
        |----------|  |------------------------------------------------------|
	|  Sensor  |  |                    Processing                        |    
        | |------| |  | |--------|                                |--------| |      |---------|
        |-| S(x) |-|--|-| U<sub>1</sub>(θ<sub>1</sub>) |---------...----------...--------| U<sub>n</sub>(θ<sub>n</sub>) |-|------| MEASURE |
        | |------| |  | |--------|                                |--------| |      |---------|
  	|----------|  |------------------------------------------------------|           |
  c0   ----------------------------------------------------------------------------------o-----
</pre>

#### Catch
- During operation, we cannot calculate expected values, because the sensor can run only once. So when we calculate the accuracy on the test set, we are not allowed to calculate expected values... we can run the circuit just once, make the PauliZ measurement, and if the result is "-1" we say "dog", if it's 1 we say "cat". (On the other hand, in the training phase we can optimize the circuit parameters, the thetas, using expected values of the measurements, as training is done in our laboratory. But operation may happen e.g. in a self-driving car.)

#### Compare with 
- The standard way of testing, that is, when we can run the circuit multiple times to get expected value of the PauliZ measurement :
	- The result can be e.g. 0.5, then we classify it as "cat", as it's closer to 1 than to -1. (So, you see that when we can run the circuit only once, we can be unlucky that we get -1, even if the expected value over many runs is 0.5.)
