# :heart: :heart: :heart: Classifying Heartbeats :heart: :heart: :heart:

Heart irregularities are commonly detected using a stethoscope by a physician. Currently, there are digital stethoscopes and mobile devices that anyone can use to record their heart sounds, however, without medical knowledge, will not know if there are any irregularities. This paper presents a process for classifying those audio heart sounds to five most commonly occurring classes: artifact, extra heart sound, extrasystole, murmur and normal heartbeat. The paper also compares the precisions and F-scores of six machine learning models, which include Naive Bayes, Support Vector Machines and Decision Trees. Using the process outlined in this paper, the results are a significant improvement to the state of the art for all classes except for extrasystole and normal heartbeats. The paper also outlines practicality and next steps to improve audio heart sound classification. 

Check out the paper [here](Classifying_Heartbeats.pdf)

File Structure should be:
- Classifying-Heartbeats
	- set_a/
	- set_b/
	- set_a.csv
	- set_a_timing.csv
	- set_b.csv

Requirements:
- Download set a and b sound files from https://www.kaggle.com/kinguistics/heartbeat-sounds/data
- Install pywavelets
```python
conda install pywavelets 
```
- Install Hidden Markov Models
```python
conda install -c omnia hmmlearn 
```
- Install simplejson
```python
conda install -c anaconda simplejson
```
- Install eyed3
```python
pip install eyeD3 
```
- Install pydub
```python
pip install pydub
```