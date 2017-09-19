## Data Pre-Processing for Fast Depth Coding Using Deep Learning

### Introduction

* This project is for processing the data before training the model for intra-mode-prediction.

* [Click here to see the behaviour details of the project](http://fast-depth-coding.readthedocs.io/en/latest/data-collection.html#behaviours-of-the-project)

### Caveats

* Data (csv files and TFRecords) are stored in the ```/data``` folder under the HOME directory. E.g., ```/home/ubuntu/data/``` (Linux) or ```/Users/pharrell_wang/data/``` (macOS)

* Remember to create ```/data/step1_output/``` and ```/data/step2_output/``` folders manually before using this project. (If you get the error traceback of *FileNotFoundError*, you need to create that folder first).

### Branches

* ```pharrell-dev-finalized``` is the finalized branch for pre-processing data of 16x16 depth blocks.
* ```pharrell-dev-001``` is the dev snapshot of the very first stage. It contains some codes that might be useful for future review.
* ```pharrell-dev-002-tfrecord-tostring``` is the second stage of the development. And it contains valuable comments and playgrounds for experimental activities.
* ```edge_strength_analysis_for_sequences``` is the branch containing the codes for edge strength analysis.

If you want to use the project, please checkout ```master``` branch.  
  